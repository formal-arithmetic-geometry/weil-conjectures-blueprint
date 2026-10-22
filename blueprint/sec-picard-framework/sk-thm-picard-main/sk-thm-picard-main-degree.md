+++
id = "det-picard-main-degree"
kind = "lemma"
title = "Degree decomposition of the Picard scheme of a geometric curve"
lean = ["AlgebraicGeometry.exists_decomposition_picardFunctor", "AlgebraicGeometry.isLocallyConstant_picardDegree", "AlgebraicGeometry.exists_picardDegree_equiv_picardFunctorDegree", "AlgebraicGeometry.exists_decomposition_picardFunctor_isMonHom", "AlgebraicGeometry.exists_iso_representableBy_picardFunctorDegree_zero"]
uses = ["thm-pc-picard-representable", "rem-pc-group-structure", "det-thm-picard-coherence", "lem-sc-riemann-roch", "lem-pc-degree-base-change"]
+++
Let $k$ be algebraically closed, $C/k$ a smooth proper connected curve of
genus $g$, $P\in C(k)$, and let $\underline{\operatorname{Pic}}_{C/k}$ be
the group scheme representing $\operatorname{Pic}_{C/k}$
([thm-pc-picard-representable]), with universal $P$-rigidified invertible
sheaf $\cL$ on $C\times\underline{\operatorname{Pic}}_{C/k}$. For a point
$t$ with residue field $\kappa(t)$ put
$\delta(t)=\deg\cL_t:=\chi(C_{\kappa(t)},\cL_t)-(1-g)$. Then:

1. $\delta$ is locally constant on $\underline{\operatorname{Pic}}_{C/k}$;
hence
$\underline{\operatorname{Pic}}_{C/k}=\coprod_{d\in\Z}\underline{\operatorname{Pic}}^d_{C/k}$
with $\underline{\operatorname{Pic}}^d_{C/k}=\delta^{-1}(d)$ open and closed;
1. $\underline{\operatorname{Pic}}^d_{C/k}$ represents the subfunctor
$\operatorname{Pic}^d_{C/k}$ of classes all of whose fibres have degree
$d$, and its $k$-points are the invertible sheaves of degree $d$ on $C$;
1. $\underline{\operatorname{Pic}}^0_{C/k}$ is an open and closed subgroup
scheme, and tensoring with $\cO_C(dP)$ is an isomorphism of schemes
$\underline{\operatorname{Pic}}^0_{C/k}\xrightarrow{\sim}\underline{\operatorname{Pic}}^d_{C/k}$
with inverse given by tensoring with $\cO_C(-dP)$.
