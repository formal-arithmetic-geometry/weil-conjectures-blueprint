+++
kind = "proof"
of = "lem-weil-pbc-filtered-colimit-normal-ring-integrally-closed"
uses = ["lem-weil-pbc-filtered-colimit-localization-at-prime", "lem-weil-pbc-filtered-colimit-normal-ring-integrally-closed-common-stage"]
+++
Let $\mathfrak p\subset R$ be prime and $\mathfrak p_i\subset R_i$ its preimage. By [lem-weil-pbc-filtered-colimit-localization-at-prime], $R_{\mathfrak p}$ is the vertex of a colimit cocone over the filtered diagram $i\mapsto(R_i)_{\mathfrak p_i}$, whose objects are integrally closed domains by hypothesis. Hence $R_{\mathfrak p}$ is integrally closed by [lem-weil-pbc-filtered-colimit-normal-ring-integrally-closed-common-stage].
