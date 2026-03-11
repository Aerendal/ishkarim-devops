"""
ci.py — kod wyekstrahowany z WORK.md dla obszaru devops.

Zawiera 3 fragmentów kodu. Każdy fragment poprzedzony komentarzem
z nazwą katalogu-źródła.
"""
from __future__ import annotations



# ────────────────────────────────────────────────────────────# Source: CLI do weryfikacji kompletności pliku_04
def stable_sha256_12(fm: dict, body: str) -> str:
    fm_json = json.dumps(fm, sort_keys=True, ensure_ascii=False, separators=(",",":"))
    return hashlib.sha256((fm_json + "\n" + body).encode("utf-8")).hexdigest()[:12]

# Source: Nowe praktyki: rekonfiguracja DevOps
# reconductor.py: event → plan → SQLite ledger
def classify_event(event: dict) -> tuple[str, list[Action], list[str]]:
    sig = event.get("signal_type", "")
    name = event.get("signal_name", "")
    # S1: CrashLoopBackOff → ROLLBACK + GATE
    if sig == "runtime" and name == "CrashLoopBackOff":
        actions = [
            Action(type="ROLLBACK", target="k8s/deploy/myapp",
                   params={"rollback_to": "previous_stable"}),
            Action(type="GATE", target="cicd/deploy",
                   params={"mode": "require_manual_approval"}),
        ]
        return ("rollback_then_gate", actions, ["CrashLoopBackOff detected"])
    # IaC drift → PATCH
    if sig == "iac" and name == "drift_detected":
        return ("patch_iac", [Action(type="PATCH", target="iac/env/prod",
                params={"apply_source_of_truth": True})], ["IaC drift"])

# Source: Samonaprawiające się Petle DevOps
e = target - metric          # błąd bieżący
I = clamp(I + e, -imax, imax)  # pamięć błędu
D = e - e_prev               # zmiana błędu
score = kP*e + kI*I + kD*D   # łączny ciężar
# score > throttle_threshold → throttle
# score > rollback_threshold → rollback
