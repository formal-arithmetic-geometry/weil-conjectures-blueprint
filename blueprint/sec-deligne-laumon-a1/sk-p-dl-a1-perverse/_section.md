+++
id = "sk-p-dl-a1-perverse"
kind = "proposition"
title = "Fourier exactness on a curve"
order = 3081
uses = ["sk-d-dl-a1-setup", "sk-l-dl-a1-endpoints", "sk-prop-kernel-lisse", "sk-prop-stalk", "sk-thm-inversion"]
lean = ["AlgebraicGeometry.LAdicWeilComplex.IsCurvePerverseUpper", "AlgebraicGeometry.LAdicWeilComplex.IsCurvePerverseLower", "AlgebraicGeometry.LAdicWeilComplex.IsCurvePerverse", "AlgebraicGeometry.isCurvePerverse_fourierTransform_obj_iff"]
tags = ["sketch"]
+++
For nontrivial $\psi$, the transform $\DLAFT_\psi$ is an exact equivalence of the perverse
categories of the two affine lines. On a smooth curve these categories
are constructed from ordinary cohomology: the upper class has
$\mathcal H^aK=0$ for $a>0$ and $\mathcal H^0K$ of finite support;
the lower class has $\mathcal H^aK=0$ for $a<-1$ and
$\mathcal H^{-1}K$ with no nonzero finite-support subsheaf.
