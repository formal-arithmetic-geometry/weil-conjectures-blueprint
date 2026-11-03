+++
id = "prop-pd-picard-degree-decomposition"
kind = "theorem"
title = "Degree decomposition of the Picard scheme"
order = 858
tags = ["latex:proposition"]
uses = ["cor-pc-sigma-pic-iso", "def-pc-degree-line-bundle", "def-pc-divisor-line-bundle", "def-pc-euler-characteristic", "def-pc-picard-functor", "def-pc-rational-point", "def-pc-separably-closed", "def-pc-smooth-projective-curve", "def-pc-subfunctor", "def-pd-degree-morphism", "def-pd-fibrewise-degree", "def-nagata-invertible-ideal", "lem-pc-degree-agrees-sc", "lem-pc-degree-base-change", "lem-pc-rational-points-dense", "lem-pc-vanishing-above-dim", "lem-pd-degree-locally-constant", "lem-sc-point-cartier", "prop-pc-xk-integral", "rem-pc-group-structure", "thm-pc-picard-representable"]
lean = ["AlgebraicGeometry.exists_decomposition_picardFunctor", "AlgebraicGeometry.picardDegree_mul", "AlgebraicGeometry.mul_mem_picardSubfunctorDegree", "AlgebraicGeometry.exists_decomposition_picardFunctor_representableBy", "AlgebraicGeometry.exists_decomposition_picardFunctor_isMonHom", "AlgebraicGeometry.exists_decomposition_picardTranslation"]
+++
Let $k$ be a separably closed field
and let $C$ be a $k$-scheme which is proper, smooth of relative
dimension $1$ and geometrically integral over $k$. Fix a $k$-rational point
$P\in C(k)$ (one exists by [lem-pc-rational-points-dense]), and for
$d\in\Z$ put $\mathcal{O}_C(dP):=\mathcal{O}_C(P)^{\otimes d}$ (a negative power
meaning a power of the dual), where $\mathcal{O}_C(P)$ is the module of
[def-pc-divisor-line-bundle] of the effective Cartier divisor $P$
([lem-sc-point-cartier]). Let $\underline{\operatorname{Pic}}_{C/k}$ be the group
scheme representing $\operatorname{Pic}_{C/k}$
([thm-pc-picard-representable], [rem-pc-group-structure]), and let
$\deg:\operatorname{Pic}_{C/k}\to\underline{\Z}$ be the degree morphism of
[def-pd-degree-morphism]. For $d\in\Z$ let
$\operatorname{Pic}^d_{C/k}\subseteq\operatorname{Pic}_{C/k}$ be the
subfunctor of classes whose
fibrewise degree function is identically $d$. Then:

1. $\deg$ is a homomorphism of sheaves of groups; in particular
$\operatorname{Pic}^0_{C/k}=\ker(\deg)$ is a subgroup functor and
$\operatorname{Pic}^{d}_{C/k}\cdot\operatorname{Pic}^{e}_{C/k}\subseteq\operatorname{Pic}^{d+e}_{C/k}$.
1. The function $\delta:\underline{\operatorname{Pic}}_{C/k}\to\Z$, $t\mapsto\deg\mathcal{L}_t$,
is locally constant, where $\mathcal{L}$ is an invertible module on
$C\times_k\underline{\operatorname{Pic}}_{C/k}$ representing the universal class
(one exists, normalized along $P$). Hence
$$
\underline{\operatorname{Pic}}_{C/k}=\coprod_{d\in\Z}\underline{\operatorname{Pic}}^d_{C/k},
\qquad
\underline{\operatorname{Pic}}^d_{C/k}:=\delta^{-1}(d),
$$
each $\underline{\operatorname{Pic}}^d_{C/k}$ is an open and closed subscheme,
and it represents the subfunctor $\operatorname{Pic}^d_{C/k}$.
1. $\underline{\operatorname{Pic}}^0_{C/k}$ is an open and closed subgroup scheme
of $\underline{\operatorname{Pic}}_{C/k}$.
1. For every $d\in\Z$, tensoring with $\mathcal{O}_C(dP)$, i.e. the translation
$x\mapsto x\cdot[\mathcal{O}_C(dP)]$ by the $k$-point
$[\mathcal{O}_C(dP)]\in\underline{\operatorname{Pic}}_{C/k}(k)$, which on a class
represented by an invertible module $\mathcal{M}$ on $C_T$ is
$\mathcal{M}\mapsto\mathcal{M}\otimes\operatorname{pr}_C^*\mathcal{O}_C(dP)$, restricts to an
isomorphism of schemes
$$
\underline{\operatorname{Pic}}^0_{C/k}\xrightarrow{\ \sim\ }\underline{\operatorname{Pic}}^d_{C/k},
$$
with inverse the translation by $[\mathcal{O}_C(-dP)]$.
