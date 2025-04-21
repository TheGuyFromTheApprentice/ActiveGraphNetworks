import json

with open("dust.json", "r") as f:
    graph = json.load(f)

nodes = graph["nodes"]
edges = graph["edges"]

def find_target(source_id, edge_type):
    for e in edges:
        if e["source"] == source_id and e["type"] == edge_type:
            return e["target"]
    return None

def print_tensor(tensor):
    for row in tensor:
        print("  | " + " | ".join(str(v) if v is not None else " " for v in row) + " |")

# Get Alice
alice = nodes.get("alice_tensor")
if not alice:
    print("❌ Alice not found.")
    exit()

print("\n=== 🧬 Alice (InstanceNode) ===")
print(f"ID: {alice['id']}")
print("Tensor:")
print_tensor(alice["tensor"])

# Resolve Spec
spec_id = find_target("alice_tensor", "conforms_to")
spec = nodes.get(spec_id)
print(f"\n🔗 Conforms to Spec: {spec_id}")
print(f"  Shape: {spec['tensor_shape']}")
print(f"  Allowed Range: {spec['allowed_range']}")

# Resolve Class
class_id = find_target(spec_id, "type_of")
class_node = nodes.get(class_id)
print(f"\n🧠 Spec Type: {class_node['label']}")

# Resolve Rules
print("\n📏 Rules:")
for e in edges:
    if e["source"] == spec_id and e["type"] == "follows_rule":
        rule_node = nodes.get(e["target"])
        print(f"  - {rule_node['rule']}")
