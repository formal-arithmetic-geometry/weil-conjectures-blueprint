+++
id = "prop-weil-pbc-strict-henselization-stalk-formula"
kind = "theorem"
title = "Strict-henselization stalk formula"
order = 964
tags = ["latex:proposition"]
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-pointed-etale-neighbourhoods", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit", "lemma-weil-pbc-affine-neighbourhood-cofinal", "lemma-weil-pbc-etale-cohomology-continuity", "lemma-weil-pbc-fibre-product-limit"]
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
[def-weil-pbc-strict-henselization-limit] at $\bar s$. For
$K\in\Dplus(X_{\Et})$ with torsion cohomology, this assembles to

$$
 (Rf_*K)_{\bar s}\xrightarrow{\sim}
 \RGamma(X\times_SS_{(\bar s)},K|)
 \quad\text{in }\Dplus(\Ab).
$$
