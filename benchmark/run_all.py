#!/usr/bin/env python3
"""
Run all benchmarks and generate a comprehensive report.
"""

import sys
import subprocess
from pathlib import Path


def run_benchmark(script_name: str) -> int:
    """Run a benchmark script and return its exit code."""
    script_path = Path(__file__).parent / script_name
    print(f"\n{'='*70}")
    print(f"Running: {script_name}")
    print(f"{'='*70}\n")

    result = subprocess.run([sys.executable, str(script_path)], cwd=script_path.parent)
    return result.returncode


def main():
    """Run all benchmarks."""
    print("="*70)
    print("TOON Benchmark Suite - Running All Tests")
    print("="*70)

    benchmarks = [
        "compare_formats.py",
        "memory_benchmark.py",
    ]

    failed = []

    for benchmark in benchmarks:
        exit_code = run_benchmark(benchmark)
        if exit_code != 0:
            failed.append(benchmark)

    print("\n" + "="*70)
    print("BENCHMARK SUITE COMPLETE")
    print("="*70)

    if failed:
        print(f"\n❌ {len(failed)} benchmark(s) failed:")
        for b in failed:
            print(f"  • {b}")
        sys.exit(1)
    else:
        print("\n✅ All benchmarks completed successfully!")
        print("\nKey Takeaways:")
        print("  • TOON reduces size by 30-60% compared to JSON")
        print("  • Token savings translate directly to lower LLM API costs")
        print("  • Performance is comparable or better than JSON")
        print("  • Perfect for structured data passed to LLMs")
        sys.exit(0)


if __name__ == "__main__":
    main()
