

# AGDB Time Series Graphs and Query Structure

Active Graph Databases (AGDBs) are designed to handle structured, time-series data efficiently through predefined relationships and synthetic relationships that allow rapid traversal across time. This document explains the architecture, query structure, and examples of how AGDBs work within the context of time series data.

## Overview of AGDB Time Series Structure

AGDBs organize time series data hierarchically, leveraging time nodes (year, month, day, hour, minute) to form a structured graph that supports efficient data navigation and querying. This structure allows users to traverse through time nodes to reach specific points in time quickly. Each time node is connected with predefined relationships that serve as "checkpoints" for easier access and faster queries.

The goal of this structure is to:
1. **Enhance Query Efficiency**: By using checkpoints and synthetic relationships, AGDBs allow for quicker retrieval of data points.
2. **Support Scalable Data Relationships**: Nodes within the graph are defined by both temporal and contextual relationships, which are either predefined (hard-baked) or synthetic.
3. **Enable Complex Queries**: Queries can specify paths through temporal dimensions, allowing for rapid navigation of time series data without complex computation or GPU requirements.

---

## Structure of AGDB Time Series Graphs

In an AGDB time series graph, each node represents a specific point in time. Nodes are structured as follows:

1. **Time Nodes**: These are the hierarchical nodes representing the temporal dimensions—Year, Month, Day, Hour, and Minute.
2. **Data Nodes**: These nodes contain specific data points for a given time. They are linked to the corresponding time nodes, which act as the entry point for querying data at a specific timestamp.
3. **Synthetic Relationships**: Generated relationships between time nodes allow for inferred traversal across the graph, enabling faster access based on checkpoints.

### Example Node Schema

Each node has a unique identifier and stores attributes relevant to the time series data.

- **Entity ID**: Encoded as a timestamp (e.g., "2024-11-04 10:45").
- **Attributes**: Metadata specific to AGN (Active Graph Network) such as type, description, features, etc.
- **Relationships**: Defined by AGDB policies; relationships can be pre-defined (static) or synthetic (inferred).

#### Sample Data Node

```yaml
- id: 03-01-01-00-17
  type: ts (time-series)
  name: Temperature Data Point
  feature_1: Temperature
  feature_2: Humidity
  feature_3: Pressure
  timestamp: "2024-11-04 10:45"
```

---

## Navigating AGDB Time Series Graphs

AGDBs use both predefined and synthetic relationships to traverse time nodes. For example, querying a specific minute within an hour follows a structured path from **Year -> Month -> Day -> Hour -> Minute**.

### Example: Traversing Time Nodes

To retrieve data at `10:45 AM` on `2024-11-04`:
1. Start at the **Year** node (2024).
2. Navigate to **Month** (November).
3. Move to **Day** (4th).
4. Access **Hour** (10).
5. Reach the **Minute** checkpoint (e.g., 10:40, a predefined checkpoint).
6. Use synthetic relationship to increment to `10:45`.

---

## Query Structure and Syntax

AGDB's query structure allows users to request specific nodes using a path-based syntax that references the temporal dimensions. Queries can leverage both direct paths and inferred paths using synthetic relationships to improve efficiency.

### Query Syntax

- **Basic Query Structure**: `get-node-type ts-path {domain}/year/month/day/hour/minute`
- **Inferred Path Query**: Uses checkpoints to jump ahead, reducing traversal steps.

### Example Query 1: Basic Time Node Retrieval

Querying data for a Bitcoin dataset at `10:45 AM` on `2024-11-04`:

```plaintext
get-node-type ts-path BTC/2024/11/04/10/45
```

**Explanation**:
- `BTC` refers to the domain of data (e.g., cryptocurrency).
- The path navigates sequentially through the hierarchical time nodes to retrieve the data node at `10:45`.

### Example Query 2: Using Checkpoints for Rapid Access

Querying data for the same Bitcoin dataset but using checkpoint relationships. Suppose there’s a predefined checkpoint at `10:40 AM`.

1. Query navigates directly to the `10:40` checkpoint.
2. Adds 5 minutes to reach `10:45`.

```plaintext
get-node-type ts-path BTC/2024/11/04/10/40 + 5
```

This method significantly improves performance by jumping to the nearest checkpoint and then making a small synthetic traversal.

---

## Synthetic Relationships and Efficiency

The synthetic relationships within AGDB allow for inferred paths, meaning that time nodes can skip ahead to reach closer checkpoints rather than traversing through every individual minute or hour. This reduces the number of traversals, enhancing query performance.

For example:
- **10-minute interval checkpoint**: Instead of navigating each minute, the system jumps in 10-minute intervals, arriving at the desired node faster.

### Example of Synthetic Relationship Navigation

To retrieve data at `11:00 AM` starting from `8:00 AM`, AGDB uses synthetic relationships:

1. Navigate from `8:00 AM` to `10:00 AM` (2-hour interval).
2. Increment by `1 hour` to `11:00 AM`.

```plaintext
get-node-type ts-path BTC/2024/11/04/08/00 + 3 hours
```

This query quickly reaches `11:00 AM` by skipping unnecessary traversal steps.

---

## Practical Use Case: Rule-Based Trading Strategy

AGDB's time series structure can be applied in domains like finance to implement rule-based trading strategies efficiently. By using policies instead of traditional training, AGNs (Active Graph Networks) are ideal for rule-based decision-making without the need for large data processing.

### Example Trading Query

To simulate a trading decision at `11:45 AM` on `2024-11-04` using a rule-based approach, AGDB can query historical data points for pattern matching.

```plaintext
get-node-type ts-path TRADING/2024/11/04/11/45
```

- **Explanation**: The query retrieves the `11:45` node under the `TRADING` domain. Based on the data at this timestamp and predefined rules, AGDB can simulate a trading action (e.g., buy/sell decision).

---

## Additional Queries and Examples

### 1. View All Nodes Within an Hour

Retrieve all nodes for `10:00 AM` to `11:00 AM` on `2024-11-04`.

```plaintext
get-node-type ts-path BTC/2024/11/04/10/*
```

**Explanation**: The `*` wildcard allows for retrieving all minute nodes within `10:00 AM` to `11:00 AM`.

### 2. Pattern Matching for Events

Identify patterns in `temperature` data where values exceed a threshold within a day.

```plaintext
get-node-type ts-path WEATHER/2024/11/04/* threshold(temperature > 30)
```

**Explanation**: This query retrieves all time nodes on `2024-11-04` and applies a threshold to filter events where temperature exceeds `30`.

---

## Benefits of AGDB for Time Series Data

1. **Scalability**: By structuring time-series data with predefined relationships, AGDBs scale efficiently with data size.
2. **Query Optimization**: Checkpoints and synthetic relationships reduce query traversal time, making AGDBs suitable for real-time insights.
3. **Cross-Domain Integration**: AGNs in AGDBs support multiple domains (e.g., finance, healthcare) by allowing data from different contexts to interact seamlessly.

---

## Conclusion

AGDBs provide a robust framework for handling time series data by combining hierarchical node structures with efficient synthetic relationships. Queries are optimized for rapid traversal, supporting complex time-series analysis without GPU-intensive training. AGDB’s structured approach to data allows users to efficiently execute rule-based strategies, pattern matching, and context-driven decision-making across multiple domains.

