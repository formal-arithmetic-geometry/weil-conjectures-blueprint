+++
id = "sk-prop-sf-dualizable-biduality"
kind = "proposition"
title = "Biduality of a perfect complex"
order = 2504
uses = ["sk-def-sf-operations"]
lean = ["AlgebraicGeometry.Etale.DerivedCategory.isDualizable_coefficientDual", "AlgebraicGeometry.Etale.DerivedCategory.nonempty_iso_coefficientDual_coefficientDual", "AlgebraicGeometry.Etale.DerivedCategory.nonempty_iso_coefficientDual_tensor"]
tags = ["sketch"]
+++
Let $K\in D(X,\Lambda)$ be perfect, that is, dualizable for
$\otimes^L_{\Lambda_X}$ (locally on the site of $X$ quasi-isomorphic to a bounded
complex of finite projective $\Lambda_X$-modules). Then
$K^\vee=\RHom_X(K,\Lambda_X)$ is again perfect, with evaluation
$K\otimes^L_{\Lambda_X}K^\vee\to\Lambda_X$ the counit of the
tensor–internal-Hom adjunction, and the biduality map $K\to K^{\vee\vee}$
is an isomorphism. For every $M\in D(X,\Lambda)$ the
canonical map $K^\vee\otimes^L_{\Lambda_X}M\to\RHom_X(K,M)$ is an isomorphism.
