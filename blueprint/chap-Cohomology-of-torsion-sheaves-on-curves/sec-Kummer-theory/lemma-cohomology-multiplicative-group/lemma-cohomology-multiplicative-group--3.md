+++
id = "lemma-cohomology-multiplicative-group--3"
kind = "lemma"
title = "Naturality under restriction"
order = 1576006
aliases = ["bp-r490-3"]
lean = ["AlgebraicGeometry.Scheme.etaleRestrictionH_toCohomologicalPicardGroup"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1"]
+++
For a scheme $Y$, descent for invertible modules identifies
$H^1(Y_{\acute{e}t},\mathbf G_m)$ with $\operatorname{Pic}(Y)$, sending an invertible
sheaf $\mathcal L$ to the class of the $\mathbf G_m$-torsor
$\operatorname{Isom}(\mathcal O_Y,\mathcal L)$. Let $f:X\to Y$ be an étale
monomorphism of schemes. Under these identifications, restriction of
cohomology classes agrees with pullback of line bundles:

$$
f^*[\operatorname{Isom}(\mathcal O_Y,\mathcal L)]
=[\operatorname{Isom}(\mathcal O_X,f^*\mathcal L)]
\quad\text{in }H^1(X_{\acute{e}t},\mathbf G_m).
$$

For an open immersion $U\hookrightarrow C$, together with the comparison of
[theorem-bounded-below-cohomology-comparison] on $C$ and on $U$, this shows that
the identification of [lemma-cohomology-multiplicative-group--1] is natural under restriction.
