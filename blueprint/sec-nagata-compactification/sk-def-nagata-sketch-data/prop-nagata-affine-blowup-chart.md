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

## Proof

Since $x$ is homogeneous of positive degree, the standard open
$D_+(x)\subseteq\operatorname{Proj}(\mathcal R_A(I))$ is canonically
isomorphic to $\operatorname{Spec}(\mathcal R_A(I)_{(x),0})$, and $\chi_x$
is the inverse of this isomorphism followed by the inclusion of $D_+(x)$;
so $\chi_x$ is an open immersion with image $D_+(x)$. The structure
morphism of $\operatorname{Proj}$ to $\operatorname{Spec}$ of the degree-zero
part restricts on $D_+(x)$ to $\operatorname{Spec}$ of the inclusion
$\mathcal R_A(I)_0\to\mathcal R_A(I)_{(x),0}$, $y\mapsto y/1$; composing
with the identification $A\cong\mathcal R_A(I)_0$ gives the second claim.
This is checked on the image of every $r\in A$.

For $x=at$ the chart ring is moreover identified with the blow-up algebra:
the map $\theta_a\colon\mathcal R_A(I)_{(at),0}\to A[I/a]$ is bijective by
[lemma-nagata-homogeneous-away-to-chart-injective] and
[lemma-nagata-homogeneous-away-to-chart-surjective], and it is
$A$-linear, so $D_+(at)\cong\operatorname{Spec}(A[I/a])$ over
$\operatorname{Spec}(A)$.
