+++
id = "prop-nagata-affine-blowup-chart"
kind = "theorem"
title = "Affine chart identification"
order = 34
lean = ["AlgebraicGeometry.AffineBlowup.opensRange_chart", "AlgebraicGeometry.AffineBlowup.chart_toSpec"]
tags = ["latex:proposition"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-piece", "lemma-nagata-homogeneous-away-to-chart-injective", "lemma-nagata-homogeneous-away-to-chart-surjective", "prop-nagata-rees-graded"]
+++
Let $x\in\mathcal R_A(I)$ be homogeneous of degree one (for instance
$x=at$ with $a\in I$). The chart
$\chi_x\colon\operatorname{Spec}\bigl(\mathcal R_A(I)_{(x),0}\bigr)\to
\operatorname{Bl}_I(\operatorname{Spec}A)$ of
[def-nagata-affine-blowup-chart-map] is an open immersion with image the
standard open $D_+(x)$, and its composite with the structure morphism
$\operatorname{Bl}_I(\operatorname{Spec}A)\to\operatorname{Spec}A$ is
$\operatorname{Spec}$ of the canonical ring homomorphism
$A\cong\mathcal R_A(I)_0\to\mathcal R_A(I)_{(x),0}$, $r\mapsto r/1$.
