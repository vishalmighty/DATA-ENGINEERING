### Key Differences:

| Feature              | `approx_count_distinct`             | `countDistinct`               |
|----------------------|-------------------------------------|--------------------------------|
| Result               | Approximate distinct count          | Exact distinct count           |
| Algorithm            | HyperLogLog++ (probabilistic)       | Deterministic aggregation      |
| Accuracy             | Controlled by `rsd` (default ~5%)   | Fully accurate                 |
| Performance          | Faster, lower memory usage          | Slower, higher memory usage    |

### When to Use:
- Use `approx_count_distinct`:
  - When working with massive datasets where performance and memory efficiency are critical.
  - When an approximation is sufficient for decision-making (e.g., analytics, dashboards).
- Use `countDistinct`:
  - When working with smaller datasets or when precise distinct counts are required.

This tradeoff allows you to choose the function best suited for your specific requirements.