+++
id = "prop-weil-pbc-strict-henselization-stalk-formula-detailed"
kind = "theorem"
title = "Strict-henselization stalk formula"
order = 1349
tags = ["latex:proposition"]
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit-detailed", "lem-weil-pbc-fibre-product-limit", "thm-weil-pbc-etale-cohomology-continuity"]
+++
Let $f:X\to S$ be quasi-compact and quasi-separated
[def-weil-pbc-scheme-conventions], let $F$ be a torsion etale sheaf
[def-weil-pbc-etale-sheaves], and let $\bar s\to S$ be geometric. Then

$$
 (R^qf_*F)_{\bar s}\xrightarrow{\sim}
 H^q(X\times_SS_{(\bar s)},F|)
 \qquad(q\geq0),
$$

where $S_{(\bar s)}$ is the strict henselization limit
[def-weil-pbc-strict-henselization-limit-detailed] at $\bar s$. For
$K\in\Dplus(X_{\Et})$ with torsion cohomology, this assembles to

$$
 (Rf_*K)_{\bar s}\xrightarrow{\sim}
 \RGamma(X\times_SS_{(\bar s)},K|)
 \quad\text{in }\Dplus(\Ab).
$$

## Proof

The stalk is the colimit over pointed etale neighbourhoods, whose inverse
limit is the strict henselization by
[def-weil-pbc-strict-henselization-limit-detailed]; the fibre product
commutation of [lem-weil-pbc-fibre-product-limit] replaces $X\times_SS_{(\bar
s)}$ by the limit of the $X\times_SV$, and
[thm-weil-pbc-etale-cohomology-continuity] identifies the colimit of
cohomologies with the cohomology of the limit. On a bounded-below K-injective
[def-weil-pbc-kinjective-resolutions] representative the same argument gives
the derived statement.
