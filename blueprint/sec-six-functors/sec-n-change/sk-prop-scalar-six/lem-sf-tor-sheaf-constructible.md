+++
id = "lem-sf-tor-sheaf-constructible"
kind = "lemma"
title = "Tor sheaves of constructible sheaves"
lean = ["AlgebraicGeometry.Etale.homologyDerivedTensorConstantSheafIso", "AlgebraicGeometry.Etale.isFiniteLocallyConstantSheaf_torSheaf_constantSheaf", "AlgebraicGeometry.Etale.isFiniteLocallyConstantSheaf_torSheaf", "AlgebraicGeometry.Etale.isConstructibleSheaf_torSheaf", "AlgebraicGeometry.Etale.isConstructibleSheaf_homology_tensor_singleFunctor"]
order = 2837
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-derived-tensor", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, $n\geq1$, and
put $A=A_{E,n}$. Let $T$ be a scheme on which $\ell$ is invertible and
let $F$ and $G$ be
constructible sheaves
of $A_T$-modules on $T_{\mathrm{proet}}$. Then for every
$r\in\mathbf Z$ the
cohomology sheaf
$\mathcal H^r(F\otimes_A^LG)$ is constructible, and its stalk at a
geometric point $\bar t\to T$ is the finite $A$-module
$\operatorname{Tor}^A_{-r}(F_{\bar t},G_{\bar t})$.
