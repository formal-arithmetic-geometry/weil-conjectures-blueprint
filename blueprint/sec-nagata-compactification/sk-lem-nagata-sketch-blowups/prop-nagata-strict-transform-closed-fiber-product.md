+++
id = "prop-nagata-strict-transform-closed-fiber-product"
kind = "theorem"
title = "Global strict transform is a closed subscheme"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.StrictTransformChart.comap_ker_strictTransformι", "AlgebraicGeometry.Scheme.IdealSheafData.strictTransformChartModel_eq", "AlgebraicGeometry.Scheme.IdealSheafData.comap_strictTransformChartModel"]
order = 165
tags = ["latex:proposition"]
uses = ["def-nagata-strict-transform", "def-nagata-strict-transform-closed-chart-model"]
+++
Under the data of
[def-nagata-strict-transform-closed-chart-model], let
$Y^{\mathrm{st}}\subseteq Y\times_XX'$ be the strict transform of $Y$
relative to $X\setminus V(\mathcal I)$ ([def-nagata-strict-transform]).
For every chart datum $c=(U,V,a)$, the restriction of the ideal of
$Y^{\mathrm{st}}$ along $\iota_c$ is $\Gamma_{(a)}(C_a(A,B,I))$; that is,
$Y^{\mathrm{st}}$ meets the chart $\operatorname{Spec}(C_a(A,B,I))$ in
$\operatorname{Spec}(C_a^{\mathrm{st}}(A,B,I))$. Consequently the chart
model $\mathcal J^{\mathrm{st}}_{\mathrm{chart}}$ is the ideal of
$Y^{\mathrm{st}}$, so $Y^{\mathrm{st}}_{\mathrm{chart}}=Y^{\mathrm{st}}$
as closed subschemes of $Y\times_XX'$, and the restriction of
$\mathcal J^{\mathrm{st}}_{\mathrm{chart}}$ along every chart $\iota_c$ is
$\Gamma_{(a)}(C_a(A,B,I))$.
