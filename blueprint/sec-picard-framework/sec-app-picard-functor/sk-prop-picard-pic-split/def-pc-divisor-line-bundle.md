+++
id = "def-pc-divisor-line-bundle"
kind = "definition"
title = "The module $\\mathcal{O}_X(D)$ of an effective Cartier divisor"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.toModules", "AlgebraicGeometry.Scheme.Modules.dual", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.isInvertible_toModules", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.isInvertible_dual_toModules"]
order = 645
uses = ["def-sc-divisor", "def-nagata-invertible-ideal", "def-sc-invertible-module"]
+++
Let $S$ be a scheme and let $D\subset S$ be an
effective Cartier divisor
with ideal sheaf $\mathcal{I}_D$. The *associated invertible module* is

$$
\mathcal{O}_S(D):=\mathcal{H}om_{\mathcal{O}_S}(\mathcal{I}_D,\mathcal{O}_S)=\mathcal{I}_D^\vee .
$$
