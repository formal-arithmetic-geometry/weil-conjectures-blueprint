+++
id = "lemma-cohomology-multiplicative-group--4"
kind = "lemma"
title = "Naturality under field extension"
order = 1574008
aliases = ["bp-r490-4"]
lean = ["AlgebraicGeometry.Scheme.gmCohomologyMap_toCohomologicalPicardGroup"]
+++
Let $g:X\to Y$ be any morphism of schemes. Under the identifications
$H^1(X_{\acute{e}t},\mathbf G_m)=\operatorname{Pic}(X)$ and
$H^1(Y_{\acute{e}t},\mathbf G_m)=\operatorname{Pic}(Y)$ of
[lemma-cohomology-multiplicative-group--3], the pullback map on étale
$\mathbf G_m$-cohomology agrees with pullback of line bundles:

$$
g^*[\operatorname{Isom}(\mathcal O_Y,\mathcal L)]
=[\operatorname{Isom}(\mathcal O_X,g^*\mathcal L)]
\quad\text{in }H^1(X_{\acute{e}t},\mathbf G_m).
$$

Taking $g:C_{k'}\to C$ for an extension $k'/k$ of algebraically closed
ground fields, together with the comparison of
[theorem-bounded-below-cohomology-comparison] on $C$ and on $C_{k'}$, this shows that
the identification of [lemma-cohomology-multiplicative-group--1] is natural under
extension of the ground field.
