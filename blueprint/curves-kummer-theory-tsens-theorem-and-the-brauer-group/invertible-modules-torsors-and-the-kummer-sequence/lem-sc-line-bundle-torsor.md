+++
id = "lem-sc-line-bundle-torsor"
kind = "lemma"
title = "Line bundles and G_m-torsors"
order = 3417
lean = ["AlgebraicGeometry.picardGroupEquivGmTorsor"]
uses = ["def-sc-curves", "def-sc-picard-group", "def-sc-gm-torsor", "def-sc-invertible-module"]
+++
Let $C$ be a curve [def-sc-curves]. The construction
$$
 \mathcal L\longmapsto\underline{\operatorname{Isom}}(\mathcal O_C,\mathcal L)
$$
(with the action $u\cdot\varphi=u\circ\varphi$ of $\mathbf G_m$) and the
construction
$$
 T\longmapsto(T\times\mathcal O_C)/\mathbf G_m
$$
(with the diagonal action $g\cdot(t,a)=(g\cdot t,g^{-1}a)$) are mutually
inverse bijections
$$
 \operatorname{Pic}(C)\longleftrightarrow
 \{\text{isomorphism classes of }\mathbf G_m\text{-torsors}\}.
$$

## Proof

For invertible $\mathcal L$, the sheaf
$T:=\underline{\operatorname{Isom}}(\mathcal O_C,\mathcal L)$ is a
$\mathbf G_m$-torsor [def-sc-gm-torsor]: the action is free and transitive,
and on a trivializing open $U$ with $\mathcal L|_U\cong\mathcal O_U$ one
has $T|_U\cong\mathbf G_m|_U$ via $\varphi\mapsto\varphi(1)$. Conversely,
for a torsor $T$ the quotient sheaf
$\mathcal L(T):=(T\times\mathcal O_C)/\mathbf G_m$ is locally isomorphic to
$(\mathbf G_m\times\mathcal O_C)/\mathbf G_m\cong\mathcal O_C$ (via
$(u,a)\mapsto ua$), hence is an invertible module. The map
$t\mapsto\varphi_t$, $\varphi_t(a)=[t,a]$, is an isomorphism
$T\to\underline{\operatorname{Isom}}(\mathcal O_C,\mathcal L(T))$
(sectionwise, since $[(g\cdot t,g^{-1}a)]=[(t,a)]$), and the map
$[(\varphi,a)]\mapsto\varphi(a)$ is an isomorphism
$$
 \mathcal L\bigl(\underline{\operatorname{Isom}}(\mathcal O_C,\mathcal L)\bigr)\to\mathcal L,
$$
well-defined because $g\varphi(g^{-1}a)=\varphi(a)$. The two constructions
are therefore mutually inverse.
