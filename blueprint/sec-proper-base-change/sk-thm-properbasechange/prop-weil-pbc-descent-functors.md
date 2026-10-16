+++
id = "prop-weil-pbc-descent-functors"
kind = "theorem"
title = "Descent of coefficient-compatible functors"
lean = ["CategoryTheory.StageSystem.Morphism", "CategoryTheory.StageSystem.Morphism.functor", "CategoryTheory.StageSystem.Morphism.Hom"]
order = 1372
uses = ["def-weil-pbc-finite-stage-pair-category", "def-weil-pbc-qbar-category", "prop-weil-pbc-scalar-extension"]
tags = ["latex:proposition"]
+++
Let $\Phi_E:\mathcal C_E(T)\to\mathcal C_E(S)$ be exact functors and let
$$
 \beta_{F/E}:T^S_{F/E}\Phi_E
 \xrightarrow{\sim}\Phi_FT^T_{F/E}
$$
be exact natural isomorphisms satisfying the unit, associator, and shift
equations of [prop-weil-pbc-scalar-extension]. Then they induce an exact
functor $\Phi:\mathcal P_T\to\mathcal P_S$. On a representative
$u:T^T_{M/E}K\to T^T_{M/F}L$, its value is represented by
$$
 T^S_{M/E}\Phi_EK\xrightarrow{\beta_{M/E}}
 \Phi_MT^T_{M/E}K\xrightarrow{\Phi_M(u)}
 \Phi_MT^T_{M/F}L\xrightarrow{\beta_{M/F}^{-1}}
 T^S_{M/F}\Phi_FL.
$$
This functor is, by [def-weil-pbc-qbar-category], already a functor on the
$\Qlb$ coefficient categories $\Dbc(T,\Qlb)=\mathcal P_T$ and
$\Dbc(S,\Qlb)=\mathcal P_S$. Compatible natural transformations and their
equations descend by the same formula.

In particular, the scalar-compatible families $(Rf_{*,E})_E$ and
$(Lg_E^*)_E$ descend to exact functors on $\Qlb$ coefficient categories, and
the finite-stage exchange maps descend to a natural transformation.
