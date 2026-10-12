+++
id = "sk-prop-a1-kummer"
kind = "proposition"
title = "The affine line and $\\mathbf G_m$ with $\\Lambda(1)$-coefficients"
order = 2238
uses = ["sk-def-av-pic", "sk-def-curve", "sk-def-purity-conv", "sk-prop-cd", "sk-prop-cd-affine", "sk-prop-kummer-exact", "sk-thm-smooth-base-change"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerStar_affineLine", "AlgebraicGeometry.Etale.nonempty_iso_homology_zero_multiplicativeGroup", "AlgebraicGeometry.Etale.nonempty_iso_homology_one_multiplicativeGroup", "AlgebraicGeometry.Etale.isZero_homology_multiplicativeGroup"]
tags = ["sketch"]
+++
In the conventions of [sk-def-purity-conv], write
$p:\Aaf^1_Y\to Y$ for the projection, $j:\mathbf G_{m,Y}\hookrightarrow \Aaf^1_Y$ for the open complement of the zero section, and $\pi=pj$.
For every separated finite-type $Y$:

- **(a)** *Acyclicity of the affine line.*
$Rp_*\Lambda\simeq\Lambda_Y$; equivalently $R^mp_*\Lambda=0$ for $m>0$.
- **(b)** *The Kummer generator.* $R^0\pi_*\Lambda(1)\simeq\Lambda_Y(1)$,
with $p^*$ an isomorphism onto it, and $R^1\pi_*\Lambda(1)\simeq\Lambda_Y$
is free of rank one on the Kummer class $\kappa(t)$.
- **(c)** *Vanishing above degree one.* $R^m\pi_*\Lambda(1)=0$ for $m\ge2$.

All three are compatible with base change on $Y$, as is $\kappa(t)$.
Equivalently, (a)–(c) are the corresponding statements for
$\Aaf^1$ and $\mathbf G_m$ over a geometric point.
