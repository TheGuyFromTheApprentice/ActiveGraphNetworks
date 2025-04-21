import json

with open("dust.json", "r") as f:
    graph = json.load(f)

print("\n=== 🧠 NODES ===")
for node_id, node in graph["nodes"].items():
    print(f"[{node['type']}] {node_id}")
    for k, v in node.items():
        if k not in ["id", "type"]:
            print(f"  ├─ {k}: {v}")
    print()

print("=== 🔗 EDGES ===")
for edge in graph["edges"]:
    print(f"{edge['source']} --{edge['type']}--> {edge['target']}")
