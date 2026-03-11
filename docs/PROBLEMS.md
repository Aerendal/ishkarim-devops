# PROBLEMS — ishkarim-devops

> Self-healing DevOps bez chmury — automatyczny rollback, policy-as-code, OIDC

## ✅ Co ten projekt rozwiązuje

- ✅ Automatyczny rollback przy wykryciu regresji (bez ręcznej interwencji)
- ✅ OIDC w CI/CD **bez długożyciowych sekretów** (tokeny rotowane per-run)
- ✅ Policy-as-code — reguły infrastruktury jako pliki YAML wersjonowane w git
- ✅ Offline-first deployment — działa bez dostępu do internetu
- ✅ Self-healing pętle: detect → diagnose → fix → verify

---

## ❌ Czego ten projekt NIE rozwiązuje

- ❌ Kubernetes native — wzorce są agnostyczne, brak gotowych Helm chartów
- ❌ Multi-cloud orchestration — skupione na lokalnym/edge deployment
- ❌ Cost optimization chmurowy — brak integracji z billing APIs
- ❌ GUI do zarządzania pipeline'ami

---

## ⚠️ Znane problemy i ograniczenia

- ⚠️ **OIDC konfiguracja** wymaga ręcznego setup w GitHub Actions / GitLab CI
- ⚠️ **Rollback strategia** zakłada idempotentne deploymenty — nie zawsze prawdziwe dla baz danych
- ⚠️ **Policy enforcement** działa w cyklu CI, nie continuous — okno między commit a enforcement
- ⚠️ **Brak integracji** z istniejącymi CMDB systemami (ServiceNow, Jira)

---

## 🎯 Przypadki użycia

- 🎯 Startup bez DevOps inżyniera — automatyczny rollback chroni produkcję
- 🎯 Edge computing deployment gdzie sieć jest zawodna (przemysł, IoT)
- 🎯 Compliance-heavy środowiska (fintech, medtech) wymagające audit trail każdej zmiany
- 🎯 ML pipeline z automatycznym rollbackiem modelu przy regresji metryk

---

## 📊 Matryca decyzyjna

| Pytanie | Odpowiedź |
|---------|-----------|
| Czy potrzebujesz GPU? | **NIE** — zaprojektowany dla CPU-only |
| Czy działa offline? | **TAK** — zero zewnętrznych zależności sieciowych |
| Czy jest produkcyjny? | **WZORCE** — referencja do implementacji, nie plug-and-play |
| Czy obsługuje skalowanie? | **LOKALNIE** — single-node, do ~kilku tysięcy dokumentów |
| Licencja? | **MIT** — możesz używać w projektach komercyjnych |

---

## 🔗 Powiązane projekty

Inne moduły Ishkarim które uzupełniają ten projekt:

| Projekt | Relacja |
|---------|---------|
| `ishkarim-rag` | Wyszukiwanie semantyczne nad bazą wiedzy |
| `ishkarim-sqlite` | Trwała pamięć i event-sourcing |
| `ishkarim-agent` | Architektura agentów AI |
| `ishkarim-security` | Bezpieczeństwo systemów AI |
| `ishkarim-bench` | Benchmarki wydajnościowe |

---

*Ostatnia aktualizacja: 2026-03-11 | Generator: `scripts/enrich_projects.py`*
