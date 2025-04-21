# 🧪 DUST3 Validator — Validates all instance tensors using their linked rules

import json
import numpy as np

# === Load Graph ===
with open("dust.json", "r") as f:
    graph = json.load(f)

nodes = graph["nodes"]
edges = graph["edges"]

# === Helpers ===
def get_edges(source=None, target=None, edge_type=None):
    return [
        e for e in edges
        if (source is None or e["source"] == source)
        and (target is None or e["target"] == target)
        and (edge_type is None or e["type"] == edge_type)
    ]

def get_node(node_id):
    return nodes.get(node_id)

def evaluate_rule(rule, value):
    try:
        return eval(rule)
    except Exception:
        return False

# === Validation Process ===
def validate_instance(instance_id):
    instance = get_node(instance_id)
    tensor = np.array(instance.get("tensor"))
    results = []

    # Step 1: Get spec this instance conforms to
    spec_edge = get_edges(source=instance_id, edge_type="conforms_to")
    if not spec_edge:
        return [{"error": "No spec found"}]
    spec_id = spec_edge[0]["target"]
    spec = get_node(spec_id)

    # Step 2: Get rules applied to that spec
    rule_edges = get_edges(source=spec_id, edge_type="follows_rule")
    rules = [get_node(e["target"]) for e in rule_edges]

    for rule in rules:
        rule_expr = rule.get("rule")
        violations = []
        for i in range(tensor.shape[0]):
            for j in range(tensor.shape[1]):
                value = tensor[i][j]
                if np.isnan(value):
                    continue  # skip NaNs
                if not evaluate_rule(rule_expr, value):
                    violations.append((i, j, value))
        results.append({
            "rule": rule_expr,
            "violations": violations,
            "passed": len(violations) == 0
        })

    return results

# === Run Validator ===
print("\n🔍 DUST3 Tensor Validation Report:\n")
for node_id, node in nodes.items():
    if node["type"] == "InstanceNode":
        print(f"📦 Instance: {node_id}")
        result = validate_instance(node_id)
        for r in result:
            print(f"  ↪ Rule: {r['rule']}")
            if r["passed"]:
                print("     ✅ Passed")
            else:
                print(f"     ❌ {len(r['violations'])} violations: {r['violations']}")
        print()
