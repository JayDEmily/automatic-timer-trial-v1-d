# G3-D-OVERLAP - fresh evidence observation

Worker evidence only; not an independent verdict or a claim of four-way overlap. Original Step 8 RETURN remains in effect.

## Authority and preserved identities

- Native Start saved at 2026-11-27T10:01:24.9708564Z (manager-observed exact native menu and choice 1).
- Direct bootstrap `8293ba3b8790cbf099f35601a0e81bc05b933878`, sole parent paused setup `f535b19742303336e9005dcbce430643039cb4af`. Bootstrap changed only the ledger. Fresh ref was verified; clean private checkout and assignment unchanged across external binding attachment.
- Pinned M `8c4a11205c3a3b6df13979a274841e7d8f3391c1`, E `5af8187767977e16dbe1fc77d873f963ede82278`, CAC 1.1.4 retained. Protected stage verified against exact local M (13 files); fresh binding identity/digest verified privately. No target attachment commit.
- Original C `7514d2c185c7089ce9bafe1e2540bdbf4616f39f`, tree `9e8e7c6bf77294d9d3b7a102b3a2b306165d50a4`, sole parent `d73fc42ad51c21d8c4d1eba13c1f71f2c79d2818`.
- Original H `2e4a0f13e5bfe4a3c26e26a7894408d18c52f0a0` is C's direct child (ledger only, saved-turn-only independent reviewer); original independent V `45dd0e6dd60f3590f048d17cc7eddcded7072254` is H's direct child (review and ledger only). V is terminal PASS; original remote ref still points to V. Setup is V's direct child.

## Actual inherited evidence

Inspected the original candidate patch, prior plan, implementation evidence and independent review. The original list-of-strings contract trims edges, removes empty results, preserves order, duplicates, case and internal whitespace. Actual code performs one strip per entry and appends only nonempty results; the three new regression methods cover these requirements. The original candidate diff is limited to normalizer.py, tests/test_normalizer.py and evidence/G3-D1.md (43 insertions, 1 deletion). Source/test/workflow/implementation-evidence blobs match across C/H/V; all five retained source/test/workflow/evidence/review blobs match V/setup/bootstrap:

- `.github/workflows/ci.yml`: `f11bd46b4d4066988603c324c15c92a007ecdf0d`
- `evidence/G3-D1.md`: `d241dca121076a2f3b2a90e697e1275739cd09b6`
- `normalizer.py`: `12ae806356a5fa6706575c9ac5ee0631e2d886f1`
- `reviews/G3-D1.md`: `deefe93397d1f0f3dea8d546167cd10b6b4a947a`
- `tests/test_normalizer.py`: `5bcd684de674df38a90780bc6ac0a63438dc98f5`

Original C-specific CI: Fixture CI, push on the original hosted-editor-retry ref; run 45962137612, attempt 1, job 140382219927 (Test normalizer), success; tested C/tree exact; six tests passed. The complete retained CI object equals both H and V; the already-local original log's length and SHA-256 match the retained record. No new log retrieval, test run, candidate, CI result or review verdict. The independent PASS remains scoped only to original C/tree/H.

## Actual substantive Git process intervals (UTC)

Each row is an actual subprocess, not a continuous work interval or chat lifetime. All returned 0; raw commands, exit codes and full outputs are retained privately for the programme manager. Setup, binding, thinking and waiting are excluded. Publication intervals and first pause are preserved in the same private raw record after this report is committed.

| Git command (private checkout omitted) | Start UTC | End UTC | Result |
|---|---|---|---|
| `git rev-parse 7514d2c185c7089ce9bafe1e2540bdbf4616f39f^{tree}` | 2026-11-27T10:03:38.150414724Z | 2026-11-27T10:03:38.154025525Z | 9e8e7c6bf77294d9d3b7a102b3a2b306165d50a4 |
| `git rev-list --parents -n1 f535b19742303336e9005dcbce430643039cb4af` | 2026-11-27T10:03:38.162053125Z | 2026-11-27T10:03:38.165772025Z | f535b19742303336e9005dcbce430643039cb4af 45dd0e6dd60f3590f048d17cc7eddcded7072254 |
| `git rev-list --parents -n1 2e4a0f13e5bfe4a3c26e26a7894408d18c52f0a0` | 2026-11-27T10:03:38.173769526Z | 2026-11-27T10:03:38.177637426Z | 2e4a0f13e5bfe4a3c26e26a7894408d18c52f0a0 7514d2c185c7089ce9bafe1e2540bdbf4616f39f |
| `git rev-list --parents -n1 45dd0e6dd60f3590f048d17cc7eddcded7072254` | 2026-11-27T10:03:38.185546527Z | 2026-11-27T10:03:38.189159727Z | 45dd0e6dd60f3590f048d17cc7eddcded7072254 2e4a0f13e5bfe4a3c26e26a7894408d18c52f0a0 |
| `git diff --name-only 7514d2c185c7089ce9bafe1e2540bdbf4616f39f 2e4a0f13e5bfe4a3c26e26a7894408d18c52f0a0` | 2026-11-27T10:03:38.196849627Z | 2026-11-27T10:03:38.200526428Z | state/ledger.json |
| `git diff --name-only 2e4a0f13e5bfe4a3c26e26a7894408d18c52f0a0 45dd0e6dd60f3590f048d17cc7eddcded7072254` | 2026-11-27T10:03:38.208133128Z | 2026-11-27T10:03:38.211770828Z | reviews/G3-D1.md, state/ledger.json |
| `git rev-parse 7514d2c185c7089ce9bafe1e2540bdbf4616f39f^` | 2026-11-27T10:03:38.220001329Z | 2026-11-27T10:03:38.223518129Z | d73fc42ad51c21d8c4d1eba13c1f71f2c79d2818 |
| `git diff --stat d73fc42ad51c21d8c4d1eba13c1f71f2c79d2818 7514d2c185c7089ce9bafe1e2540bdbf4616f39f` | 2026-11-27T10:03:38.227852229Z | 2026-11-27T10:03:38.231721230Z | 3 files; 43 insertions, 1 deletion |
| `git diff d73fc42ad51c21d8c4d1eba13c1f71f2c79d2818 7514d2c185c7089ce9bafe1e2540bdbf4616f39f` | 2026-11-27T10:03:38.235972730Z | 2026-11-27T10:03:38.239559930Z | actual patch inspected; retained privately |
| `git show 7514d2c185c7089ce9bafe1e2540bdbf4616f39f:plans/active-execplan.md` | 2026-11-27T10:03:38.243653231Z | 2026-11-27T10:03:38.247139331Z | actual committed content inspected; retained privately |
| `git show 7514d2c185c7089ce9bafe1e2540bdbf4616f39f:evidence/G3-D1.md` | 2026-11-27T10:03:38.251400531Z | 2026-11-27T10:03:38.254698931Z | actual committed content inspected; retained privately |
| `git show 45dd0e6dd60f3590f048d17cc7eddcded7072254:reviews/G3-D1.md` | 2026-11-27T10:03:38.258657331Z | 2026-11-27T10:03:38.263020132Z | actual committed content inspected; retained privately |
| `git show 2e4a0f13e5bfe4a3c26e26a7894408d18c52f0a0:state/ledger.json` | 2026-11-27T10:03:38.270041532Z | 2026-11-27T10:03:38.274027833Z | actual committed content inspected; retained privately |
| `git show 45dd0e6dd60f3590f048d17cc7eddcded7072254:state/ledger.json` | 2026-11-27T10:03:38.278384733Z | 2026-11-27T10:03:38.282137833Z | actual committed content inspected; retained privately |
| `git ls-tree -r 7514d2c185c7089ce9bafe1e2540bdbf4616f39f` | 2026-11-27T10:03:38.364145438Z | 2026-11-27T10:03:38.370470439Z | 10 tree entries; checked blob identities |
| `git ls-tree -r 2e4a0f13e5bfe4a3c26e26a7894408d18c52f0a0` | 2026-11-27T10:03:38.378170539Z | 2026-11-27T10:03:38.382097340Z | 10 tree entries; checked blob identities |
| `git ls-tree -r 45dd0e6dd60f3590f048d17cc7eddcded7072254` | 2026-11-27T10:03:38.386216940Z | 2026-11-27T10:03:38.389676340Z | 11 tree entries; checked blob identities |
| `git ls-tree -r f535b19742303336e9005dcbce430643039cb4af` | 2026-11-27T10:03:38.393616640Z | 2026-11-27T10:03:38.397067641Z | 11 tree entries; checked blob identities |
| `git ls-tree -r 8293ba3b8790cbf099f35601a0e81bc05b933878` | 2026-11-27T10:03:38.401290941Z | 2026-11-27T10:03:38.404676941Z | 11 tree entries; checked blob identities |
| `git diff --name-only 45dd0e6dd60f3590f048d17cc7eddcded7072254 8293ba3b8790cbf099f35601a0e81bc05b933878` | 2026-11-27T10:03:38.417012642Z | 2026-11-27T10:03:38.421199042Z | AGENTS.md, plans/active-execplan.md, state/ledger.json |

No artificial delay or overlap barrier; no repetition of accepted source/CI tests. The single lane makes no determination of the common interval. Separate ledger-only pause follows report publication, pending distinct programme acceptance.
