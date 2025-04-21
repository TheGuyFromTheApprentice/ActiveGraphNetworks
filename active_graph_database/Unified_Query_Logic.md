### Document 2: Unified Command Logic for AGDB

# Unified Command Logic for AGDB

This document details the command structure for interacting with AGDB, covering CRUD operations, querying, managing synthetic relationships, setting policies, and more. Each command is structured in a noun-verb format, following PowerShell-style syntax.

## Command Categories

1. **Graph Management Commands**
2. **Node and Relationship Management**
3. **Attribute and Domain Commands**
4. **Query and Retrieval Commands**
5. **Policy Management**

---

### 1. Graph Management Commands

#### `create-graph`
- **Description**: Initializes a new graph, specifying the type and metadata.
- **Usage**: `create-graph -name "financial_time_series" -type "AGDB"`
- **Example**:
  ```plaintext
  create-graph -name "financial_time_series" -type "AGDB" -attributes ["Open", "Close", "Volume"]
  ```

#### `load-graph`
- **Description**: Loads an existing graph from JSON or CSV.
- **Usage**: `load-graph -file "path/to/graph.json"`
- **Example**:
  ```plaintext
  load-graph -file "graphs/trading_data.json"
  ```

---

### 2. Node and Relationship Management

#### `create-node`
- **Description**: Adds a node to the graph, defining its type, domain, and attributes.
- **Usage**: `create-node -id "node_001" -type "TimeSeriesNode" -domain "TradingData"`
- **Example**:
  ```plaintext
  create-node -id "node_001" -attributes {"open": 50, "close": 55, "volume": 5000}
  ```

#### `create-relationship`
- **Description**: Establishes a relationship between two nodes.
- **Usage**: `create-relationship -from "node_001" -to "node_002" -type "temporal_sequence"`
- **Example**:
  ```plaintext
  create-relationship -from "node_001" -to "node_002" -type "next"
  ```

---

### 3.

 Attribute and Domain Commands

#### `set-attribute`
- **Description**: Modifies or sets attributes for a node.
- **Usage**: `set-attribute -node "node_001" -attributes {"volume": 6000}`
- **Example**:
  ```plaintext
  set-attribute -node "node_001" -attributes {"open": 52, "high": 60}
  ```

#### `set-domain`
- **Description**: Assigns a domain to a node or graph.
- **Usage**: `set-domain -graph "financial_time_series" -name "Trading"`
- **Example**:
  ```plaintext
  set-domain -node "node_001" -name "Finance"
  ```

---

### 4. Query and Retrieval Commands

#### `get-node`
- **Description**: Retrieves data for a specific node.
- **Usage**: `get-node -id "node_001"`
- **Example**:
  ```plaintext
  get-node -id "node_001" -attributes ["open", "close"]
  ```

#### `get-relationship`
- **Description**: Retrieves relationships for a node.
- **Usage**: `get-relationship -node "node_001" -type "temporal_sequence"`
- **Example**:
  ```plaintext
  get-relationship -node "node_001" -direction "outgoing"
  ```

---

### 5. Policy Management

#### `set-policy`
- **Description**: Defines or updates a policy for relationship inferences.
- **Usage**: `set-policy -name "trading_inference" -rules {"time_series_trend": {...}}`
- **Example**:
  ```plaintext
  set-policy -name "trading_inference" -rules {"volatility_correlation": {"weight_threshold": 0.5}}
  ```

#### `apply-policy`
- **Description**: Executes a policy-based query.
- **Usage**: `apply-policy -name "trading_inference" -target "node_001"`
- **Example**:
  ```plaintext
  apply-policy -name "similar_patterns" -target "node_001"
  ```

---

### Summary

This unified command structure allows for robust interaction with AGDB, enabling users to perform a wide range of operations from graph creation and management to complex query and retrieval operations. By using a straightforward noun-verb syntax, the command logic is accessible and scalable across various data structures, making AGDB a powerful tool for data-driven insights across multiple domains. 
