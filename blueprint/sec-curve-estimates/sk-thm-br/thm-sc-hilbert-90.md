+++
id = "thm-sc-hilbert-90"
kind = "theorem"
title = "Hilbert 90 for a scheme"
lean = ["AlgebraicGeometry.Scheme.Pic.instCommGroup", "AlgebraicGeometry.Scheme.Pic.toH1Units", "AlgebraicGeometry.Scheme.Pic.toH1Units_mul", "AlgebraicGeometry.Scheme.Pic.toH1UnitsAddEquiv", "AlgebraicGeometry.Scheme.Pic.toCohomologicalPicardGroup", "AlgebraicGeometry.Scheme.Pic.toCohomologicalPicardGroup_mul", "AlgebraicGeometry.Scheme.Pic.toCohomologicalPicardGroupAddEquiv", "AlgebraicGeometry.Scheme.nonempty_equiv_H_one_unitsSheaf", "CategoryTheory.Sheaf.Torsor.classH1_eq_add_of_equivariant"]
order = 1326
uses = ["def-sc-curves", "def-sc-gm-torsor", "def-sc-invertible-module", "def-sc-picard-group", "lem-sc-line-bundle-torsor", "lem-sc-torsor-h1"]
+++
Let $X$ be a scheme (for instance a curve $C$ as in
[def-sc-curves]). The set of isomorphism classes of invertible
$\mathcal O_X$-modules ([def-sc-invertible-module]) is an
abelian group under $\otimes$, and there are isomorphisms
of abelian groups

$$
\{\text{invertible }\mathcal O_X\text{-modules}\}/{\cong}
\;\xrightarrow{\ \sim\ }\;
H^1(X_{\mathrm{Zar}},\mathcal O_X^\times)\;\xrightarrow{\ \sim\ }\;
H^1(X_{\Et},\mathbf G_m),
$$

the first sending $\mathcal L$ to the class of the Zariski
$\mathcal O_X^{\times}$-torsor
$\underline{\operatorname{Isom}}(\mathcal O_X,\mathcal L)$, and the
composite sending $\mathcal L$ to the class of the
$\mathbf G_m$-torsor
$\underline{\operatorname{Isom}}(\mathcal O_{X_{\Et}},\mathcal L_{\Et})$
([def-sc-gm-torsor]); the second map is the composite of the inverse of
the first with this map.
