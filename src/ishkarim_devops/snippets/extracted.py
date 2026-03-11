"""
extracted.py — fragmenty kodu z WORK.md dla obszaru devops.

UWAGA: To są fragmenty referencyjne wyekstrahowane z notatek badawczych.
Mogą wymagać dostosowania przed użyciem w produkcji.

Zawiera 8 fragmentów. Każdy poprzedzony komentarzem ze źródłem.
"""
# ruff: noqa
# type: ignore
from __future__ import annotations

# Source: CLI do weryfikacji kompletności pliku_04
@dataclass(frozen=True)
class Finding:
    layer: str      # L0/L1/L2/L3/L4
    severity: str   # ERROR/WARN/INFO
    code: str       # stabilny kod API (np. FM_PARSE_ERROR, SEC_MISSING, REF_UNRESOLVABLE)
    message: str
    path: Optional[str] = None  # np. "frontmatter.id", "body.heading[3]"
    hint: Optional[str] = None

@dataclass(frozen=True)
class Report:
    version: str
    target: str
    sha256_12: str
    ok: bool
    findings: List[Finding]
    summary: Dict[str, Any]

# ────────────────────────────────────────────────────────────

# Source: CLI do weryfikacji kompletności pliku_04
from markdown_it import MarkdownIt
md = MarkdownIt("commonmark")
tokens = md.parse(body)
# Nagłówki ATX i Setext są w tokenach heading_open; token.map[0]+1 = linia

# ────────────────────────────────────────────────────────────

# Source: Modularność i projektowanie fundamentów
class MyModule:
    def discover(self) -> dict:
        return {"name": "my-module", "version": "1.0.0", "compat": "kernel>=2.0.0"}
    def init(self, config: dict, services: dict) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def health(self) -> dict: return {"status": "ok"}

# ────────────────────────────────────────────────────────────

# Source: Nowe wzorce: self‑healing, IaC, rollback
plan = json.load(open("tfplan.json"))
destructive = [r for r in plan["resource_changes"]
               if "delete" in r.get("change", {}).get("actions", [])]
if destructive:
    raise SystemExit(f"BLOCKED: destructive changes require manual gate: {destructive}")

# ────────────────────────────────────────────────────────────

# Source: Prototyp harnessu do instrumentacji dokumentu
conn.execute("""CREATE VIRTUAL TABLE chunks USING fts5(
  doc_id, sec_id, text, tokenize='porter')""")
random.seed(1337)  # stały seed do deterministycznych tie-breaków

# ────────────────────────────────────────────────────────────

# Source: Zsynchronizuj zegary strumieni i systemu
# core/timebase.py
@dataclass(frozen=True)
class OffsetInfo:
    version: str; mean_seconds: float; stdev_ms: float
    measured_at_utc: float; samples: int

class Timebase:
    def to_utc_ns(self, ts_lsl_seconds: float) -> int:
        return int((ts_lsl_seconds + self._offset.mean_seconds) * 1_000_000_000)

# ────────────────────────────────────────────────────────────

# Source: Zsynchronizuj zegary strumieni i systemu
@dataclass
class Point:
    ts_utc_ns: int; session_id: str; offset_version: str
    stream: str; fields: dict

# ────────────────────────────────────────────────────────────

# Source: Śledzenie snapshotów przez tagi ‘canary’
def canary_from_sha256_hex(sha_hex: str, n: int = 5) -> str:
    raw = bytes.fromhex(sha_hex)
    return _crockford_b32(raw)[:n]
