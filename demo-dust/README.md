## 🚀  Workflow – from clone to validation

```bash
# 1 Clone the demo repo
git clone https://github.com/ActiveGraphNetworks/demo-dust
cd demo-dust

# 2 (optional) Regenerate the graph from code
python dust.py                 # builds dust.json anew

# 3 Explore the whole graph
python view_dust.py            # prints all nodes & edges

# 4 Walk Alice’s inheritance chain
python view_alice.py           # shows tensor → spec → class → rules

# 5 Validate every tensor against its inherited rules
python validate_dust.py        # reports pass / violations
