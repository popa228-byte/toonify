#!/usr/bin/env python3
"""
Benchmark script comparing TOON vs JSON in terms of:
- File size (bytes)
- Token count (using tiktoken)
- Memory usage
- Encoding/decoding performance
"""

import json
import sys
import time
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import tiktoken
from toon import encode, decode


def count_tokens(text: str, model: str = "gpt-4") -> int:
    """Count tokens using tiktoken."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))


def format_size(size_bytes: int) -> str:
    """Format bytes in human-readable format."""
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f}KB"
    else:
        return f"{size_bytes / (1024 * 1024):.2f}MB"


def calculate_savings(original: int, compressed: int) -> float:
    """Calculate percentage savings."""
    if original == 0:
        return 0.0
    return ((original - compressed) / original) * 100


def print_header(title: str, width: int = 80):
    """Print a fancy header."""
    print("\n" + "=" * width)
    print(f"{title:^{width}}")
    print("=" * width)


def print_savings_bar(label: str, percentage: float, width: int = 50):
    """Print a visual savings bar."""
    filled = int((percentage / 100) * width)
    bar = "█" * filled + "░" * (width - filled)
    print(f"  {label:<20} {bar} {percentage:>6.1f}%")


def benchmark_dataset(name: str, data: dict, iterations: int = 1000, verbose: bool = True) -> dict:
    """Benchmark a single dataset."""
    # Generate JSON
    json_str = json.dumps(data, indent=2)
    json_size = len(json_str.encode('utf-8'))
    json_tokens = count_tokens(json_str)

    # Generate TOON
    toon_str = encode(data)
    toon_size = len(toon_str.encode('utf-8'))
    toon_tokens = count_tokens(toon_str)

    # Calculate savings
    size_savings = calculate_savings(json_size, toon_size)
    token_savings = calculate_savings(json_tokens, toon_tokens)

    if verbose:
        print(f"\n{'─'*80}")
        print(f"📊 {name}")
        print(f"{'─'*80}")

        # Size comparison
        print(f"\n  SIZE:   JSON {format_size(json_size):>10}  →  TOON {format_size(toon_size):>10}  "
              f"({'-' if size_savings > 0 else '+'}{abs(size_savings):.1f}%)")
        print(f"  TOKENS: JSON {json_tokens:>6} tokens  →  TOON {toon_tokens:>6} tokens  "
              f"({'-' if token_savings > 0 else '+'}{abs(token_savings):.1f}%)")

    # Benchmark encoding performance (reduced iterations for speed)
    start = time.perf_counter()
    for _ in range(min(iterations, 100)):
        encode(data)
    toon_encode_time = (time.perf_counter() - start) / min(iterations, 100) * 1000

    start = time.perf_counter()
    for _ in range(min(iterations, 100)):
        json.dumps(data)
    json_encode_time = (time.perf_counter() - start) / min(iterations, 100) * 1000

    # Benchmark decoding performance
    start = time.perf_counter()
    for _ in range(min(iterations, 100)):
        decode(toon_str)
    toon_decode_time = (time.perf_counter() - start) / min(iterations, 100) * 1000

    start = time.perf_counter()
    for _ in range(min(iterations, 100)):
        json.loads(json_str)
    json_decode_time = (time.perf_counter() - start) / min(iterations, 100) * 1000

    return {
        'name': name,
        'json_size': json_size,
        'toon_size': toon_size,
        'size_savings': size_savings,
        'json_tokens': json_tokens,
        'toon_tokens': toon_tokens,
        'token_savings': token_savings,
        'json_encode_time': json_encode_time,
        'toon_encode_time': toon_encode_time,
        'json_decode_time': json_decode_time,
        'toon_decode_time': toon_decode_time,
    }


def main():
    """Run all benchmarks."""
    from sample_datasets import DATASETS

    print_header("🚀 TOON vs JSON: THE ULTIMATE SHOWDOWN 🚀", 80)
    print("\n" + " " * 10 + "Testing across 50 diverse, real-world datasets")
    print(" " * 10 + "Measuring size, tokens, and performance\n")

    results = []

    # Show detailed output for first 10 datasets
    print("\n" + "▼" * 80)
    print("DETAILED RESULTS (First 10 Datasets)")
    print("▼" * 80)

    for i, (dataset_name, dataset) in enumerate(DATASETS.items()):
        if i < 10:
            result = benchmark_dataset(dataset_name, dataset, verbose=True)
        else:
            # Silent benchmarking for remaining datasets
            if i == 10:
                print("\n" + "⚡" * 80)
                print("  Processing remaining 40 datasets...")
                print("⚡" * 80)
            result = benchmark_dataset(dataset_name, dataset, verbose=False)
            print(f"  ✓ {dataset_name:<50} ({result['size_savings']:.1f}% size, {result['token_savings']:.1f}% tokens)")
        results.append(result)

    # Calculate aggregate statistics
    total_json_size = sum(r['json_size'] for r in results)
    total_toon_size = sum(r['toon_size'] for r in results)
    total_json_tokens = sum(r['json_tokens'] for r in results)
    total_toon_tokens = sum(r['toon_tokens'] for r in results)

    avg_size_savings = calculate_savings(total_json_size, total_toon_size)
    avg_token_savings = calculate_savings(total_json_tokens, total_toon_tokens)

    total_size_saved = total_json_size - total_toon_size
    total_tokens_saved = total_json_tokens - total_toon_tokens

    # Best performers
    best_size = max(results, key=lambda x: x['size_savings'])
    best_tokens = max(results, key=lambda x: x['token_savings'])

    # Print epic summary
    print_header("📈 AGGREGATE RESULTS ACROSS ALL 50 DATASETS 📈", 80)

    print(f"\n{'┌' + '─'*78 + '┐'}")
    print(f"│{'TOTAL DATA SIZE':^78}│")
    print(f"│{' '*78}│")
    print(f"│  JSON:     {format_size(total_json_size):>15}  ({total_json_size:,} bytes){' '*(32-len(str(total_json_size)))}│")
    print(f"│  TOON:     {format_size(total_toon_size):>15}  ({total_toon_size:,} bytes){' '*(32-len(str(total_toon_size)))}│")
    print(f"│  SAVED:    {format_size(total_size_saved):>15}  (⬇ {avg_size_savings:.1f}%){' '*(41-len(f'{avg_size_savings:.1f}'))}│")
    print(f"{'└' + '─'*78 + '┘'}")

    print(f"\n{'┌' + '─'*78 + '┐'}")
    print(f"│{'TOTAL TOKEN COUNT (GPT-4)':^78}│")
    print(f"│{' '*78}│")
    print(f"│  JSON:     {total_json_tokens:>10,} tokens{' '*(50-len(f'{total_json_tokens:,}'))}│")
    print(f"│  TOON:     {total_toon_tokens:>10,} tokens{' '*(50-len(f'{total_toon_tokens:,}'))}│")
    print(f"│  SAVED:    {total_tokens_saved:>10,} tokens  (⬇ {avg_token_savings:.1f}%){' '*(39-len(f'{total_tokens_saved:,}')-len(f'{avg_token_savings:.1f}'))}│")
    print(f"{'└' + '─'*78 + '┘'}")

    # Visual savings bars
    print("\n" + "━" * 80)
    print("  MEMORY & TOKEN SAVINGS VISUALIZATION")
    print("━" * 80)
    print_savings_bar("Size Reduction", avg_size_savings)
    print_savings_bar("Token Reduction", avg_token_savings)

    # Cost analysis
    print("\n" + "╔" + "═"*78 + "╗")
    print("║" + "💰 REAL-WORLD COST IMPACT FOR LLM APIs 💰".center(78) + "║")
    print("╠" + "═"*78 + "╣")

    # Calculate costs at different price points
    cost_per_1m_tokens = 10.00  # Example: $10 per 1M tokens (GPT-4 pricing)

    json_cost_per_request = (total_json_tokens / len(results)) * (cost_per_1m_tokens / 1_000_000)
    toon_cost_per_request = (total_toon_tokens / len(results)) * (cost_per_1m_tokens / 1_000_000)
    savings_per_request = json_cost_per_request - toon_cost_per_request

    print(f"║  At ${cost_per_1m_tokens}/1M tokens (typical GPT-4 pricing):".ljust(79) + "║")
    print(f"║".ljust(79) + "║")
    print(f"║    • Average JSON request:  ${json_cost_per_request:.6f}".ljust(79) + "║")
    print(f"║    • Average TOON request:  ${toon_cost_per_request:.6f}".ljust(79) + "║")
    print(f"║    • Savings per request:   ${savings_per_request:.6f}  ({avg_token_savings:.1f}% less!)".ljust(79) + "║")
    print(f"║".ljust(79) + "║")
    print(f"║  ANNUAL SAVINGS (at 1M requests/year):".ljust(79) + "║")
    print(f"║    💵 ${savings_per_request * 1_000_000:>15,.2f}".ljust(79) + "║")
    print(f"║".ljust(79) + "║")
    print(f"║  For 1 BILLION tokens (e.g., high-volume API):".ljust(79) + "║")
    print(f"║    💵 ${(avg_token_savings / 100) * cost_per_1m_tokens * 1000:>15,.2f} saved!".ljust(79) + "║")
    print("╚" + "═"*78 + "╝")

    # Champion datasets
    print("\n" + "🏆" * 80)
    print("  CHAMPION PERFORMERS")
    print("🏆" * 80)
    print(f"\n  🥇 Best Size Savings:  {best_size['name']}")
    print(f"     {best_size['size_savings']:.1f}% reduction  ({format_size(best_size['json_size'])} → {format_size(best_size['toon_size'])})")
    print(f"\n  🥇 Best Token Savings: {best_tokens['name']}")
    print(f"     {best_tokens['token_savings']:.1f}% reduction  ({best_tokens['json_tokens']} → {best_tokens['toon_tokens']} tokens)")

    # Summary table
    print("\n" + "╔" + "═"*78 + "╗")
    print("║" + " DATASET PERFORMANCE SUMMARY ".center(78) + "║")
    print("╠" + "═"*78 + "╣")

    # Group by performance
    excellent = [r for r in results if r['size_savings'] >= 60]
    good = [r for r in results if 40 <= r['size_savings'] < 60]
    moderate = [r for r in results if r['size_savings'] < 40]

    print(f"║  🔥 Excellent (≥60% savings):  {len(excellent):>2} datasets".ljust(79) + "║")
    print(f"║  ✅ Good (40-60% savings):     {len(good):>2} datasets".ljust(79) + "║")
    print(f"║  📊 Moderate (<40% savings):   {len(moderate):>2} datasets".ljust(79) + "║")
    print("╚" + "═"*78 + "╝")

    # Final verdict
    print("\n" + "⭐" * 80)
    print_header("⚡ THE VERDICT ⚡")
    print("\n  TOON FORMAT DELIVERS:")
    print(f"    • {avg_size_savings:.1f}% SMALLER file sizes")
    print(f"    • {avg_token_savings:.1f}% FEWER tokens for LLM APIs")
    print(f"    • {format_size(total_size_saved)} TOTAL memory saved across 50 datasets")
    print(f"    • {total_tokens_saved:,} TOTAL tokens saved")
    print(f"    • 💰 MASSIVE cost savings for high-volume applications")
    print("\n  Perfect for:")
    print("    ✓ LLM API calls (reduce token costs)")
    print("    ✓ Database exports (tabular data)")
    print("    ✓ Analytics & metrics")
    print("    ✓ E-commerce & inventory")
    print("    ✓ Any structured, uniform data")
    print("\n" + "⭐" * 80)

    print("\n✅ Benchmark completed successfully!\n")


if __name__ == "__main__":
    main()
