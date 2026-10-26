+++
id = "sk-p-dl-a1-perverse"
kind = "proposition"
title = "Fourier transform and the perverse heart"
order = 3991
uses = ["sk-l-dl-a1-endpoints", "sk-lem-wft-character-integral", "sk-lem-wft-curve-heart", "sk-thm-inversion"]
lean = ["AlgebraicGeometry.isCurvePerverse_fourierTransform_obj_iff"]
tags = ["sketch"]
+++
Let $\psi$ be a nontrivial additive character of $k_0$. On the Weil
complexes of $\mathbf A^1_{k_0}$ and of the dual line, take the classes
${}^pD^{\le0}$ and ${}^pD^{\ge0}$ of [sk-lem-wft-curve-heart], imposed
on the cohomology Weil sheaves and their supports. Then
$\operatorname{FT}_\psi$ is t-exact for these classes, and a Weil
complex is a perverse Weil sheaf if and only if its transform is. Hence
$\operatorname{FT}_\psi$ induces an exact equivalence of the perverse
Weil hearts, with inverse $\operatorname{FT}_{\psi^{-1}}(-)(1)$; in
particular it sends simple perverse Weil sheaves to simple ones.
