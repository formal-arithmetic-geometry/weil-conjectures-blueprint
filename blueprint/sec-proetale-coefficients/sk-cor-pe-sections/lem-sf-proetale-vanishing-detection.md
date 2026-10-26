+++
id = "lem-sf-proetale-vanishing-detection"
kind = "lemma"
title = "Detection of vanishing on affine weakly contractible objects"
lean = ["AlgebraicGeometry.ProEtale.isZero_iff_forall_isWeaklyContractible", "AlgebraicGeometry.ProEtale.acyclic_iff_forall_isWeaklyContractible"]
order = 935
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "lem-cbc-proetale-stalk-conservative"]
+++
Let $\Lambda$ be a commutative ring, let $T$ be a scheme and let
$F$ be a sheaf of $\Lambda$-modules on the
small pro-étale site
$T_{\Proet}$.

1. **(i)** $F=0$ if and only if $F(W)=0$ for every affine weakly
contractible object $W\to T$ of $T_{\Proet}$.
1. **(ii)** More generally, a complex of $\Lambda$-module sheaves on
$T_{\Proet}$ is acyclic if and only if its evaluation at every affine
weakly contractible object of $T_{\Proet}$ is an acyclic complex.

Consequently the family of evaluation functors $F\mapsto F(W)$, indexed
by the affine weakly contractible objects, is a detection device on the
whole pro-étale topos, although the geometric-point stalks are not
conservative there by clause (4) of
[lem-cbc-proetale-stalk-conservative].
