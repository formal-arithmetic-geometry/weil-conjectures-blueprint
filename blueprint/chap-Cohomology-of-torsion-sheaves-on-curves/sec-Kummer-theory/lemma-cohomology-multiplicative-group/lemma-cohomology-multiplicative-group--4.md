+++
id = "lemma-cohomology-multiplicative-group--4"
kind = "lemma"
title = "Naturality under field extension"
order = 1571005
aliases = ["bp-r490-4"]
lean = ["AlgebraicGeometry.Scheme.gmCohomologyMap_toCohomologicalPicardGroup"]
uses = ["lemma-cohomology-multiplicative-group--1"]
+++
Let $g:X\to Y$ be any morphism of schemes. The pullback map on étale
$\mathbf G_m$-cohomology is compatible with
[lemma-cohomology-multiplicative-group--1]:
$$
g^*[\operatorname{Isom}(\mathcal O_Y,\mathcal L)]
=[\operatorname{Isom}(\mathcal O_X,g^*\mathcal L)]
\quad\text{in }H^1(X_{\acute{e}t},\mathbf G_m).
$$
Taking $g:C_{k'}\to C$ gives naturality under extension $k'/k$ of
algebraically closed ground fields.
