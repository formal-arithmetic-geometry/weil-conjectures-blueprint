+++
id = "lem-weil-pbc-derived-cohomology-continuity"
kind = "lemma"
title = "Continuity for bounded-below etale complexes"
order = 1238
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-etale-cohomology-continuity", "prop-weil-pbc-inverse-image-exact", "thm-weil-pbc-hypercover-cohomology"]
+++
Let $X=\varprojlim_jX_j$ be a cofiltered system of quasi-compact
quasi-separated schemes [def-weil-pbc-scheme-conventions] with affine
transition maps. For a finite ring $\Lambda$, let $K_i\in\Dplus(X_{i,\Et},
\Lambda)$ and let $K_j,K$ be its inverse images
[def-weil-pbc-inverse-image]. Then the canonical restriction map is an
isomorphism

$$
 \varinjlim_{j\geq i}H^nR\Gamma(X_{j,\Et},K_j)
 \xrightarrow{\sim}H^nR\Gamma(X_{\Et},K)
 \qquad(n\in\mathbb Z).
$$
