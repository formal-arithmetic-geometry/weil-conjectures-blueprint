+++
id = "prop-weil-pbc-descent-functors"
kind = "theorem"
title = "Descent of coefficient-compatible functors"
order = 1312
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

## Proof

Define $\Phi(E,K)=(E,\Phi_EK)$ on objects and, on a representative $(M,u)$,
by the displayed composite in $\mathcal C_M(S)$. The value is independent of
$M$: for $M\subset N$ the $\beta$-isomorphisms transport the composite for
$u$ to the composite for $u_N$, using the unit and associator equations of
[prop-weil-pbc-scalar-extension] which the $\beta$'s satisfy; equivalent
representatives give equal composites at the witnessing stage by those
equations, so $\Phi$ is well defined on the morphisms of
[def-weil-pbc-finite-stage-pair-category]. It is additive, the composites
being exact functors and exact natural isomorphisms of exact natural
transformations, and exact (finite-stage exactness of the $\Phi_E$ and the
$T$'s makes the composite exact on distinguished triangles); natural
transformations and their equations descend by that formula by the
equivariance with the $\beta$'s. By [def-weil-pbc-qbar-category] this is
already the descent to the $\Qlb$ coefficient categories
($\Dbc(T,\Qlb)=\mathcal P_T$ and $\Dbc(S,\Qlb)=\mathcal P_S$); no extension
to an envelope is needed. The families $(Rf_{*,E})_E$ and $(Lg_E^*)_E$ carry
the scalar-extension isomorphisms of [prop-weil-pbc-scalar-extension] as the
data $\beta$, so they descend to exact functors on the $\Qlb$ coefficient
categories, and the finite-stage exchange maps, being compatible with scalar
extension, descend to a natural transformation.
