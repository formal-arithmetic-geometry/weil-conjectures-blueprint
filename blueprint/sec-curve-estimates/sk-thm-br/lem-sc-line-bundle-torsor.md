+++
id = "lem-sc-line-bundle-torsor"
kind = "lemma"
title = "Line bundles and $\\mathbf G_m$-torsors"
lean = ["AlgebraicGeometry.Scheme.picEquivQuotientTorsorGmSheaf", "AlgebraicGeometry.Scheme.Pic.etaleTorsorClass", "AlgebraicGeometry.Scheme.Pic.injective_etaleTorsorClass", "AlgebraicGeometry.Scheme.Pic.surjective_etaleTorsorClass", "AlgebraicGeometry.Scheme.Pic.bijective_torsorClass", "AlgebraicGeometry.Scheme.picEquivQuotientTorsorUnitsSheaf_symm_mk", "AlgebraicGeometry.Scheme.nonempty_equiv_quotient_torsor"]
order = 1350
uses = ["def-sc-gm-torsor", "def-sc-invertible-module", "def-sc-picard-group", "lem-pc-fpqc-descent"]
+++
Let $X$ be a scheme (the left-hand side below is the Picard group of
[def-sc-picard-group]). For an invertible $\mathcal O_X$-module
$\mathcal L$ ([def-sc-invertible-module]) write $\mathcal L_{\Et}$ for
the etale sheaf $(\varphi:U\to X)\mapsto\Gamma(U,\varphi^*\mathcal L)$,
a module over $\mathcal O_{X_{\Et}}:=(\mathcal O_X)_{\Et}$. The
construction

$$
\mathcal L\longmapsto\underline{\operatorname{Isom}}(\mathcal O_{X_{\Et}},\mathcal L_{\Et})
$$

(with the action $u\cdot\varphi=u\circ\varphi$ of $\mathbf G_m$) is
a bijection

$$
\{\text{invertible }\mathcal O_X\text{-modules}\}/{\cong}
\;\longleftrightarrow\;
\{\text{isomorphism classes of }\mathbf G_m\text{-torsors on }X_{\Et}\}
$$

(torsors as in [def-sc-gm-torsor]). Likewise, on the Zariski site,
$\mathcal L\mapsto\underline{\operatorname{Isom}}(\mathcal O_X,\mathcal L)$,
the sheaf of local generators of $\mathcal L$, is a bijection from the
isomorphism classes of invertible $\mathcal O_X$-modules onto the
isomorphism classes of $\mathcal O_X^{\times}$-torsors on
$X_{\mathrm{Zar}}$, with inverse
$T\mapsto(T\times\mathcal O_X)/\mathcal O_X^{\times}$ (diagonal action
$g\cdot(t,a)=(g\cdot t,g^{-1}a)$).
