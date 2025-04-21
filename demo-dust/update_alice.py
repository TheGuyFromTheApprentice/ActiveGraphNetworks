# Add some invalid values to the tensor
import json
import numpy as np

with open("dust.json", "r") as f:
    graph = json.load(f)

# Modify alice_tensor's values
tensor = np.array(graph["nodes"]["alice_tensor"]["tensor"])
tensor[0][0] = -15     # Invalid (below range)
tensor[2][2] = 999     # Invalid (above range)
tensor[1][1] = 180     # Valid

graph["nodes"]["alice_tensor"]["tensor"] = tensor.tolist()

# Save back to file
with open("dust.json", "w") as f:
    json.dump(graph, f, indent=2)

print("📉 Injected test violations into alice_tensor.")
