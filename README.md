# ishkarim-devops

> **Self-healing DevOps bez chmury — automatyczny rollback, policy-as-code, OIDC**

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![CPU-only](https://img.shields.io/badge/CPU-only-orange)]()

## Problem, który rozwiązujemy

- Automatyczny rollback przy wykryciu regresji (bez ręcznej interwencji)
- OIDC w CI/CD
- Policy-as-code — reguły infrastruktury jako pliki YAML wersjonowane w git

Pełna lista → [docs/PROBLEMS.md](docs/PROBLEMS.md)

## Szybki start

```bash
# Instalacja
pip install -e projects/ishkarim-devops

# Demo (10 sekund)
python projects/ishkarim-devops/demo.py
```

## Użycie w kodzie

```python
import ishkarim_devops as m

# Wszystkie 68 katalogi wiedzy obszaru 'devops'
docs = m.load_knowledge_index()
print(f"{len(docs)} katalogów | obszar: {m.__area__}")

# Narzędzia pomocnicze
from ishkarim_devops.utils import read_work_md, extract_tags, extract_python_blocks
```

## Dla kogo

- Startup bez DevOps inżyniera — automatyczny rollback chroni produkcję
- Edge computing deployment gdzie sieć jest zawodna (przemysł, IoT)
- Compliance-heavy środowiska (fintech, medtech) wymagające audit trail każdej zmiany

## Dokumentacja

| Plik | Zawartość |
|------|-----------|
| [docs/PROBLEMS.md](docs/PROBLEMS.md) | Co rozwiązuje / czego nie / znane problemy |
| [docs/api.md](docs/api.md) | Dokumentacja API |
| [docs/overview.md](docs/overview.md) | Przegląd obszaru |
| [docs/sources.md](docs/sources.md) | Źródłowe katalogi wiedzy |
| [MODULES.md](MODULES.md) | Pełny indeks 68 katalogów |

## Testy i benchmarki

```bash
# Testy jednostkowe
pytest tests/test_devops.py -v

# Testy domenowe (z prawdziwymi danymi)
pytest tests/test_devops_domain.py -v

# Benchmarki wydajnościowe
python benchmarks/bench_devops.py --quick
```

## Struktura projektu

```
ishkarim-devops/
├── demo.py                    ← uruchom mnie
├── pyproject.toml
├── README.md
├── MODULES.md                 ← 68 katalogów-źródeł
├── docs/
│   ├── PROBLEMS.md            ← co rozwiązuje / czego nie
│   ├── api.md                 ← dokumentacja API
│   ├── overview.md
│   └── sources.md
├── src/ishkarim_devops/
│   ├── __init__.py            ← MODULES list + load_knowledge_index()
│   ├── utils.py               ← read_work_md, extract_tags, extract_python_blocks
│   └── snippets/              ← kod z WORK.md (referencyjny)
├── tests/
│   ├── test_devops.py         ← testy jednostkowe
│   └── test_devops_domain.py  ← testy domenowe
└── benchmarks/
    └── bench_devops.py        ← benchmarki wydajnościowe
```

## Ograniczenia

> ⚠️ To projekt **referencyjny** — wzorce i wiedza, nie gotowa biblioteka produkcyjna.
> Przed wdrożeniem produkcyjnym przeczytaj [docs/PROBLEMS.md](docs/PROBLEMS.md).

---

*Część ekosystemu [Ishkarim](../../README.md) — 68 katalogów wiedzy obszaru `devops`*
*Wygenerowano: 2026-03-11 | `scripts/build_projects.py` + `scripts/enrich_projects.py`*
