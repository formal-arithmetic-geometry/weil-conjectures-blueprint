+++
id = "cor-weil-pbc-geometric-fiber-finite"
kind = "theorem"
title = "Finite-coefficient geometric-fiber formula"
order = 2136
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_isAddTorsion_ring", "AlgebraicGeometry.Etale.nonempty_addEquiv_sheafFiber_homology_rightDerivedLowerStar_of_isProper"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-scheme-conventions", "prop-weil-proet-finite-proper-base-change"]
tags = ["latex:corollary"]
+++
Let $f:X\to Y$ be proper, let $\bar y:\operatorname{Spec}\Omega\to Y$ be a geometric
point ($\Omega$ separably closed), and let $i_{\bar y}:X_{\bar y}\to X$ and
$a_{\bar y}:X_{\bar y}\to\operatorname{Spec}\Omega$ be the projections of the
geometric fibre $X_{\bar y}=X\times_Y\operatorname{Spec}\Omega$. Let $\Lambda$ be a
finite commutative ring and let $K\in\Dplus(X_{\Et},\Lambda)$. The étale
base-change morphism is an isomorphism

$$
 \bar y^{-1}Rf_*K\xrightarrow{\sim}
 Ra_{\bar y,*}i_{\bar y}^{-1}K.
$$

For every sheaf $F$ of $\Lambda$-modules on $X_{\Et}$ this gives, for every
$q\geq0$, an isomorphism of abelian groups

$$
 (R^qf_*F)_{\bar y}\cong H^q(X_{\bar y},F|_{X_{\bar y}}).
$$
