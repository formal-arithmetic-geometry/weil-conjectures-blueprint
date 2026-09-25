+++
id = "lem-weil-biduality-locally-free"
kind = "lemma"
title = "Biduality for locally free objects on a smooth scheme"
order = 2218
uses = ["def-sf-orientation", "def-weil-site-perfect-complex", "lem-weil-coefficient-frobenius"]
+++
Let $X$ be a smooth separated finite-type $k$-scheme of pure dimension
$d$ whose orientation has been identified,
$\omega_X\cong\Lambda_X(d)[2d]$ ([def-sf-orientation]), and let
$K\in D^b_{ctf}(X,\Lambda)$ be quasi-isomorphic, locally on the site of
$X$, to a bounded complex of finite free $\Lambda_X$-modules
([def-weil-site-perfect-complex]). Then
$\delta_K:K\to D_XD_XK$ is an isomorphism.

## Proof

Use the orientation assumed in the statement, as defined in
[def-sf-orientation]. Locally take a bounded finite free model for
$K$, as in [def-weil-site-perfect-complex]. Its coefficient dual
computes $R\mathcal Hom_\Lambda(K,\Lambda_X)$; tensoring the target
with the invertible rank-one twist and shifting therefore gives
$D_XK\cong K^\vee(d)[2d]$. Apply this computation twice. The
invertible twists and opposite shifts cancel, and evaluation identifies
$\delta_K$ with the termwise finite-projective double-dual map.
It is an isomorphism by the perfect-complex clause of
[lem-weil-coefficient-frobenius]. Isomorphisms can be checked on
the covering on which these models were chosen, proving the assertion.
