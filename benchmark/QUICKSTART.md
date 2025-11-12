# Benchmark Quick Start

## Run All Benchmarks

The fastest way to see the memory savings:

```bash
python benchmark/run_all.py
```

This will run all benchmarks and provide a comprehensive summary.

## Run Individual Benchmarks

### 1. Compare Sizes and Tokens

```bash
python benchmark/compare_formats.py
```

This shows:
- File size comparison (JSON vs TOON)
- Token count comparison (for LLM APIs)
- Encoding/decoding performance
- Example outputs

### 2. Measure Memory Usage

```bash
python benchmark/memory_benchmark.py
```

This shows:
- Actual memory consumption
- Network bandwidth savings
- Practical cost impact

## Expected Results

You should see:
- **~58% average size reduction**
- **~50% average token reduction**
- **Up to 71% savings for tabular data**

## What This Means

If you're sending structured data to LLM APIs:
- **50% fewer tokens** = **50% lower costs**
- **Faster network transfers** = better performance
- **Same data quality** = no loss of information

## Examples

### Before (JSON)
```json
{
  "products": [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Mouse", "price": 29}
  ]
}
```
**Size: 134 bytes, 48 tokens**

### After (TOON)
```toon
products[2]{id,name,price}:
  1,Laptop,999
  2,Mouse,29
```
**Size: 52 bytes, 23 tokens**

**Savings: 61.2% size, 52.1% tokens**

## Requirements

```bash
pip install tiktoken  # For token counting
```

## Troubleshooting

If you get import errors, make sure you're in the project root:

```bash
cd /path/to/toonify
python benchmark/run_all.py
```

Or install the package:

```bash
pip install -e .
python benchmark/run_all.py
```
