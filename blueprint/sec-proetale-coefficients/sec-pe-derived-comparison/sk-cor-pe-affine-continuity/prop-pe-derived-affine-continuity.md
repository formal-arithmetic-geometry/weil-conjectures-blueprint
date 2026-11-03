+++
id = "prop-pe-derived-affine-continuity"
kind = "proposition"
title = "Pro-étale cohomology of a pro-étale affine"
order = 1051
tags = ["not-formalized"]
uses = ["thm-weil-pbc-site-comparison", "lem-weil-pbc-comparison-global-cohomology", "lem-weil-pbc-derived-cohomology-continuity"]
+++
Let $X$ be a scheme, $K\in D^+(X_{\mathrm{ét}})$ a bounded-below complex of
abelian sheaves, and let
$U=\varprojlim_{i\in I}U_i$ be a pro-étale affine over $X$, the limit being
cofiltered with affine transition maps and each $U_i$ affine and étale over
$X$. Write $K_i=K|_{U_i}\in D^+((U_i)_{\mathrm{ét}})$ and $K_U$ for the
inverse image of $K$ on $U_{\mathrm{ét}}$. Then for every $n\in\mathbf Z$ the
canonical maps

$$
\varinjlim_iH^n((U_i)_{\mathrm{ét}},K_i)\xrightarrow{\ \sim\ }
H^n(U_{\mathrm{ét}},K_U)\xrightarrow{\ \sim\ }
H^n(U_{\mathrm{proét}},(\nu_X^*K)|_U)
$$

are isomorphisms; equivalently
$R\Gamma(U_{\mathrm{proét}},(\nu_X^*K)|_U)\simeq\varinjlim_iR\Gamma((U_i)_{\mathrm{ét}},K_i)$
as a filtered derived colimit.

*Not formalized in Lean.* This is the tex corollary "Cohomology of a pro-étale affine"
(pe:affine-continuity), which nothing else uses; it is recorded here and will not be
formalized.
