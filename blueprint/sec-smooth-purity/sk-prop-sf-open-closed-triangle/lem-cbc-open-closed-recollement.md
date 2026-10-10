+++
id = "lem-cbc-open-closed-recollement"
kind = "lemma"
title = "Open-closed recollement"
order = 1850
uses = ["def-weil-open-closed-recollement", "def-weil-pbc-derived-categories", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-finite-direct-image-exact", "prop-weil-open-closed-recollement-adjunctions"]
+++
Let $i:Z\hookrightarrow X$ be a
closed immersion with
complementary
open immersion
$j:U\hookrightarrow X$, and let $\Lambda$ be a finite commutative
ring. For every $K\in D^+(X_{\Et},\Lambda)$ there is a functorial
distinguished triangle

$$
j_!j^{-1}K\longrightarrow K\longrightarrow i_*i^{-1}K
\longrightarrow j_!j^{-1}K[1],
$$

where $i_*$ is the (exact) direct image of the closed immersion, and
the triangle is compatible with the adjunctions
$j_!\dashv j^{-1}$, $i^{-1}\dashv i_*$ of
[prop-weil-open-closed-recollement-adjunctions].
