"""
ishkarim_devops — moduł z obszaru devops.

Self-healing DevOps: rollback, OIDC, policy-as-code, rekonfiguracja, CI/CD.

Źródła: 68 katalogów z repozytorium Ishkarim.
"""
from __future__ import annotations

__version__ = "0.1.0"
__area__ = "devops"



MODULES: list[str] = [
    'AST‑oparte lintowanie i testy kompletności',
    'Aktualizacja: rekonfiguracja i automatyzacja DevOps',
    'Architektura & przepływ - dwa front-endy nad wspólnym REST + warstwy pomocnicze',
    'Asercje oparte na schemacie i bramki CI',
    'Audit Layer for workflowctl Validation',
    'Audyt spójności JSONL przed uruchomieniem pipeline’u',
    'Automatyczne poprawki w DOCX i Markdown z Pandoc-Panflute',
    'Autonomiczne DevOps z rollbackiem i self‑regulacją',
    'Bezpieczny broker aktualizacji dla bibliotek i ChatGPT CLI',
    'Bramki jakości według kosztu błędu',
    'CLI do weryfikacji kompletności pliku_04',
    'Canary guardrail, który oszczędza bólu',
    'DeepMind’s Project Genie and Game Market Reactions_04',
    'DevOps reconfiguration — key findings',
    'DevOps: Self‑Healing & IaC Highlights',
    'DevOps: self‑healing & IaC findings',
    'Docker Hardened Images pinuj po digescie, nie tagu',
    'Docker vs Podman',
    'FFVII Remake 3 pozostaje przy Unreal Engine 4',
    'GitHub Actions z nowym edytorem i funkcją `case()`',
    'Guardraile dla iteracji typu diff-only',
    'Hermetyczne buildy i prywatne registry npm',
    'Konwencja nazw runbooków: prosty wzorzec bez kolizji',
    'LLVM rozważa włączenie precompiled headers',
    'Linux jako proaktywny OS z intencją i politykami deception-aware',
    'Linux jako proaktywny OS: architektura i lokalny POC',
    'Migawkowy przegląd projektu',
    'Modularność i projektowanie fundamentów',
    'New preprints on local AI  and resilience',
    'Node-MDX - testowalne przykłady i kontrakty HTTP',
    'Nowe praktyki: rekonfiguracja DevOps',
    'Nowe preprinty i narzędzia dla lokalnego AI',
    'Nowe wzorce DevOps i self‑healing',
    'Nowe wzorce: self‑healing, IaC, rollback',
    'Odporne DevOps bez chmury',
    'OpenAI wprowadza Prism – naukowe środowisko pisarskie_04',
    'Overture Maps 2026: kierunki i jakość danych',
    'Podsumowania i metryki day_xx',
    'Podziały Runbooków',
    'Pokrycie testów API i gating w CI',
    'Porównywanie dokumentów przez Pandoc JSON',
    'Proactive Linux Architecture and Policy Hooks',
    'Propozycje gier strategicznych',
    'Prototyp harnessu do instrumentacji dokumentu',
    'Przepisy na buildy reprodukowalne i rozszerzenia',
    'SPDX i CITATION.cff dla audytowalnych repozytoriów_04',
    'Samo-naprawczy pipeline DevOps',
    'Samonaprawiające się Petle DevOps',
    'Samonaprawiające się pipeline’y i kontrola polityk',
    'Self-Healing Infrastructure',
    'Self-healing pipelines  and IaC brief',
    'Snapshoty i audyt kotwic w CI',
    'Sphinx z lokalnymi metrykami i progami jakości',
    'State Cell Guard and Audit Patterns',
    'Szablon atomicznego runbooka do repozytorium_04',
    'Szablony testów',
    'Telling a Story Through ADR Titles',
    'Testowanie przykładów i linków w mdBook-MDX',
    'Turning Accepted ADRs into Living Roadmaps',
    'Turning documentation gates into executable policy',
    'TypeScript 7 nowy kompilator w Go przyspiesza buildy',
    'Typst 0.14.2 — bezpieczeństwo pluginów i powtarzalne buildy',
    'Udostępnianie repo na GitHubie',
    'Wersjonowanie pakietów reguł YAML jak kodu',
    'Wnioski z forów - RAG  and DevOps',
    'Zsynchronizuj zegary strumieni i systemu',
    'Śledzenie snapshotów przez tagi ‘canary’',
    '„tempo" — terminalowy interfejs do Temporal',
]


_REPO_ROOT: str | None = None


def _find_repo_root() -> str:
    """Auto-discover the Ishkarim repo root by walking up from __file__."""
    from pathlib import Path
    p = Path(__file__).resolve().parent
    for _ in range(10):
        if (p / "CATALOG.md").exists() or (p / "CHANGELOG.md").exists():
            return str(p)
        p = p.parent
    return str(Path(__file__).resolve().parents[5])  # fallback


def load_knowledge_index(root: str | None = None) -> list[dict]:
    """
    Zwraca listę rekordów ze wszystkich katalogów-źródeł obszaru.

    Args:
        root: ścieżka do katalogu głównego repozytorium (opcjonalne)

    Returns:
        Lista słowników z kluczami: name, doc_id, maturity, area
    """
    import re
    from pathlib import Path

    if root is None:
        root = _find_repo_root()

    results = []
    for name in MODULES:
        tags_path = Path(root) / name / "TAGS.md"
        if not tags_path.exists():
            continue
        tags = tags_path.read_text(errors="replace")
        doc_id = ""
        maturity = "draft"
        m = re.search(r"^doc_id:\s*(\S+)", tags, re.M)
        if m:
            doc_id = m.group(1)
        m2 = re.search(r"^maturity:\s*(\S+)", tags, re.M)
        if m2:
            maturity = m2.group(1)
        results.append({"name": name, "doc_id": doc_id, "maturity": maturity, "area": "devops"})
    return results


__all__ = ["MODULES", "load_knowledge_index", "__version__", "__area__"]
