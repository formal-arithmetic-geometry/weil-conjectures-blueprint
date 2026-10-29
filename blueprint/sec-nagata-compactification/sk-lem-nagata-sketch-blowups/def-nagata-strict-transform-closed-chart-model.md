+++
id = "def-nagata-strict-transform-closed-chart-model"
kind = "definition"
title = "Closed chart model of the global strict transform"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.StrictTransformChart", "AlgebraicGeometry.Scheme.IdealSheafData.StrictTransformChart.ι", "AlgebraicGeometry.Scheme.IdealSheafData.strictTransformChartModel"]
order = 180
uses = ["def-nagata-global-blowup", "def-nagata-strict-transform-chart-ring"]
+++
Let $f\colon Y\to X$ be a morphism, let $\mathcal I$ be a quasi-coherent
ideal on $X$, and put $X'=\operatorname{Bl}_{\mathcal I}(X)$. A *chart
datum* is a triple $c=(U,V,a)$ consisting of an affine open
$U=\operatorname{Spec}(A)$ of $X$, an affine open
$V=\operatorname{Spec}(B)\subseteq f^{-1}(U)$ of $Y$, and an element
$a\in\mathcal I(U)$; put $I=\mathcal I(U)$. Such a datum gives the open
immersion

$$
\iota_c\colon\operatorname{Spec}(C_a(A,B,I))
=V\times_U\operatorname{Spec}(A[I/a])
\longrightarrow Y\times_XX'
$$

of the base change of the $a$-chart of the blow-up, and the closed
subscheme $\operatorname{Spec}(C_a^{\mathrm{st}}(A,B,I))$ of
$\operatorname{Spec}(C_a(A,B,I))$, cut out by the ideal
$\Gamma_{(a)}(C_a(A,B,I))$.

The *chart model* of the strict transform is the quasi-coherent ideal
$\mathcal J^{\mathrm{st}}_{\mathrm{chart}}\subseteq\mathcal O_{Y\times_XX'}$
defined as the largest quasi-coherent ideal whose restriction along every
chart $\iota_c$ is contained in $\Gamma_{(a)}(C_a(A,B,I))$, and
$Y^{\mathrm{st}}_{\mathrm{chart}}\subseteq Y\times_XX'$ is the closed
subscheme it defines.
