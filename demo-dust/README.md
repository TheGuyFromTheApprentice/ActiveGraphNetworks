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
```

### 🔄  Test a rule violation

```bash
python update_alice.py         # injects out‑of‑range values into Alice
python validate_dust.py        # now shows ❤️‍🔥 violations for those cells
```

### 📁  What each script does

| Script               | Purpose                                                  |
|----------------------|----------------------------------------------------------|
| `dust.py`            | Rebuilds **dust.json** (Spec + Instance + Rules)        |
| `view_dust.py`       | CLI overview of **all** nodes and typed edges            |
| `view_alice.py`      | Deep‑inspection of one instance and everything it inherits |
| `update_alice.py`    | Demo helper – mutates Alice’s tensor for testing         |
| `validate_dust.py`   | Evaluates every InstanceNode against its RuleNodes       |

### 🛠  Next steps you can try

1. **Add a new SpecNode**  
   ```python
   # inside dust.py
   add_node("spec_blood_panel", "SpecNode",
            tensor_shape=[4,4], allowed_range=[0,400])
   ```
2. **Spin up a fresh InstanceNode that *conforms_to* it**  
3. **Write a RuleNode** (e.g., `"value >= 0 and value <= 400"`)  
4. Re‑run `validate_dust.py` to see the new schema enforced in real time.

*That’s the whole end‑to‑end loop: build → inspect → mutate → validate*
