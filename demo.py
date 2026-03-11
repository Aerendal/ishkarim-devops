#!/usr/bin/env python3
"""
demo.py — demo ishkarim-devops

Self-healing DevOps bez chmury — automatyczny rollback, policy-as-code, OIDC

Uruchomienie:
    python projects/ishkarim-devops/demo.py
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parents[0] / "src"))
import ishkarim_devops as m
from ishkarim_devops.utils import extract_tags

docs = m.load_knowledge_index()
# Pokaż katalogi z tematyką self-healing
healing = [d for d in docs if any(kw in d["name"].lower()
           for kw in ["heal", "napraw", "rollback", "self-"])]
print(f"Self-healing wzorce: {len(healing)} katalogów\n")
for d in healing[:5]:
    print(f"  • {d['name'][:70]}")
print("\n...uruchom benchmarks/bench_devops.py --quick dla metryk")

