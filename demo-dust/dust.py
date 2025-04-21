# 🧠 DUST3 Graph Initialization Script (Enhanced)

import numpy as np
import json

# === Base Structure ===
dust3_graph = {
    "nodes": {},  # id -> node dict
    "edges": []   # list of {source, target, type}
}

# === Utility Functions ===
def add_node(node_id, node_type, **attrs):
    if node_id in dust3_graph["nodes"]:
        raise ValueError(f"Node '{node_id}' already exists.")
    node = {
        "id": node_id,
        "type": node_type,
        "metadata": attrs.get("metadata", {})
    }
    # Directly include known fields (if provided)
    for key in ["tensor", "tensor_shape", "allowed_range", "history", "label", "rule"]:
        if key in attrs:
            node[key] = attrs[key]
    dust3_graph["nodes"][node_id] = node

def add_edge(source, target, edge_type):
    if source not in dust3_graph["nodes"] or target not in dust3_graph["nodes"]:
        raise ValueError("Both source and target must be existing node ids.")
    dust3_graph["edges"].append({
        "source": source,
        "target": target,
        "type": edge_type
    })

# === Example Graph Construction ===

# Define a SpecNode (schema + constraints)
add_node(
    "spec_vital_signs",
    "SpecNode",
    tensor_shape=[3, 3],
    allowed_range=[0, 250],
    metadata={"version": "1.0", "description": "Vital sign readings (BP, HR, Temp)"}
)

# Classify the spec under a semantic type
add_node(
    "class_numeric",
    "ClassNode",
    label="NumericMeasurement",
    metadata={"domain": "Clinical"}
)
add_edge("spec_vital_signs", "class_numeric", "type_of")

# Create an InstanceNode with initial tensor
tensor = np.full((3, 3), np.nan)
add_node(
    "alice_tensor",
    "InstanceNode",
    tensor=tensor.tolist(),
    history=[],
    metadata={"created_by": "system", "origin": "demo"}
)
add_edge("alice_tensor", "spec_vital_signs", "conforms_to")

# Attach a RuleNode to enforce value range
add_node(
    "rule_check_range",
    "RuleNode",
    rule="value >= 0 and value <= 250",
    metadata={"description": "Ensures all values fall within vital range"}
)
add_edge("spec_vital_signs", "rule_check_range", "follows_rule")

# === Export Graph ===
output_path = "dust.json"
with open(output_path, "w") as f:
    json.dump(dust3_graph, f, indent=2)

print(f"DUST3 graph exported to: {output_path}")
