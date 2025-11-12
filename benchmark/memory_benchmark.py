#!/usr/bin/env python3
"""
Memory usage benchmark comparing TOON vs JSON.
Shows actual memory consumption when working with serialized data.
"""

import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from toon import encode, decode


def get_memory_size(obj):
    """
    Get approximate memory size of a Python object in bytes.
    This uses sys.getsizeof recursively for nested structures.
    """
    import sys
    from collections.abc import Mapping, Iterable

    seen = set()

    def sizeof(o):
        if id(o) in seen:
            return 0
        seen.add(id(o))

        size = sys.getsizeof(o)

        if isinstance(o, Mapping):
            size += sum(sizeof(k) + sizeof(v) for k, v in o.items())
        elif isinstance(o, Iterable) and not isinstance(o, (str, bytes, bytearray)):
            size += sum(sizeof(item) for item in o)

        return size

    return sizeof(obj)


def format_size(size_bytes: int) -> str:
    """Format bytes in human-readable format."""
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f}KB"
    else:
        return f"{size_bytes / (1024 * 1024):.2f}MB"


def benchmark_memory(name: str, data: dict):
    """Benchmark memory usage for a dataset."""
    print(f"\n{'='*60}")
    print(f"Memory Benchmark: {name}")
    print(f"{'='*60}")

    # Python object memory
    obj_memory = get_memory_size(data)
    print(f"\n📦 Python Object:")
    print(f"  Memory: {format_size(obj_memory):>10} ({obj_memory:,} bytes)")

    # JSON string memory
    json_str = json.dumps(data, indent=2)
    json_str_memory = sys.getsizeof(json_str)
    json_bytes = json_str.encode('utf-8')
    json_bytes_memory = len(json_bytes)

    print(f"\n📄 JSON Format:")
    print(f"  String object memory: {format_size(json_str_memory):>10} ({json_str_memory:,} bytes)")
    print(f"  UTF-8 bytes size:     {format_size(json_bytes_memory):>10} ({json_bytes_memory:,} bytes)")

    # TOON string memory
    toon_str = encode(data)
    toon_str_memory = sys.getsizeof(toon_str)
    toon_bytes = toon_str.encode('utf-8')
    toon_bytes_memory = len(toon_bytes)

    print(f"\n🎯 TOON Format:")
    print(f"  String object memory: {format_size(toon_str_memory):>10} ({toon_str_memory:,} bytes)")
    print(f"  UTF-8 bytes size:     {format_size(toon_bytes_memory):>10} ({toon_bytes_memory:,} bytes)")

    # Calculate savings
    string_savings = ((json_str_memory - toon_str_memory) / json_str_memory) * 100
    bytes_savings = ((json_bytes_memory - toon_bytes_memory) / json_bytes_memory) * 100

    print(f"\n💾 Memory Savings:")
    print(f"  String memory: {string_savings:.1f}% smaller")
    print(f"  Bytes size:    {bytes_savings:.1f}% smaller")

    # Practical impact
    print(f"\n💡 Practical Impact:")
    print(f"  If you send this data to an LLM API:")
    print(f"    • JSON uses {json_bytes_memory:,} bytes of network bandwidth")
    print(f"    • TOON uses {toon_bytes_memory:,} bytes of network bandwidth")
    print(f"    • You save {json_bytes_memory - toon_bytes_memory:,} bytes per request!")

    return {
        'name': name,
        'obj_memory': obj_memory,
        'json_str_memory': json_str_memory,
        'json_bytes_memory': json_bytes_memory,
        'toon_str_memory': toon_str_memory,
        'toon_bytes_memory': toon_bytes_memory,
        'string_savings': string_savings,
        'bytes_savings': bytes_savings,
    }


def main():
    """Run memory benchmarks."""
    from sample_datasets import DATASETS

    print("="*60)
    print("TOON Memory Usage Benchmark")
    print("="*60)
    print("\nThis benchmark shows actual memory consumption when")
    print("working with JSON vs TOON serialized data.")

    results = []

    # Test a subset of datasets for memory benchmarks
    test_datasets = {
        "E-commerce Products": DATASETS["E-commerce Products"],
        "Database Results": DATASETS["Database Results"],
        "Large Inventory (100 items)": DATASETS["Large Inventory (100 items)"],
    }

    for dataset_name, dataset in test_datasets.items():
        result = benchmark_memory(dataset_name, dataset)
        results.append(result)

    # Summary
    print(f"\n{'='*60}")
    print("MEMORY SAVINGS SUMMARY")
    print(f"{'='*60}")
    print(f"\n{'Dataset':<35} {'Bytes Saved':<15} {'% Saved':<10}")
    print("-" * 60)

    for result in results:
        bytes_saved = result['json_bytes_memory'] - result['toon_bytes_memory']
        print(f"{result['name']:<35} {format_size(bytes_saved):<15} {result['bytes_savings']:>6.1f}%")

    total_json = sum(r['json_bytes_memory'] for r in results)
    total_toon = sum(r['toon_bytes_memory'] for r in results)
    total_saved = total_json - total_toon
    avg_savings = ((total_json - total_toon) / total_json) * 100

    print("-" * 60)
    print(f"{'TOTAL':<35} {format_size(total_saved):<15} {avg_savings:>6.1f}%")

    print(f"\n🎉 Key Findings:")
    print(f"  • TOON reduces serialized data size by {avg_savings:.1f}% on average")
    print(f"  • This means less memory usage, faster network transfers")
    print(f"  • And most importantly: lower LLM API costs!")
    print(f"\n✅ Memory benchmark completed successfully!")


if __name__ == "__main__":
    main()
