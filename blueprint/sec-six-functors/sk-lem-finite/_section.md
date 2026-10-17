+++
id = "sk-lem-finite"
kind = "lemma"
title = "Perfect complexes at the geometric point"
lean = ["AlgebraicGeometry.WeilSheaf.subsingleton_cohomology_adicConstant", "DerivedCategory.IsPerfect.tensor_homology", "DerivedCategory.isPerfect_of_finiteTorAmplitude", "DerivedCategory.IsPerfect.ihom_unit", "AlgebraicGeometry.Etale.isPerfect_compactlySupportedGlobalSections", "AlgebraicGeometry.Etale.isPerfect_rightDerivedGlobalSections", "AlgebraicGeometry.Etale.isPerfect_ihom_compactlySupportedGlobalSections", "AlgebraicGeometry.Etale.isPerfect_ihom_rightDerivedGlobalSections", "AlgebraicGeometry.Etale.isPerfect_compactlySupportedGlobalSections_integral", "AlgebraicGeometry.Etale.isPerfect_rightDerivedGlobalSections_integral", "AlgebraicGeometry.Etale.isPerfect_ihom_compactlySupportedGlobalSections_integral", "AlgebraicGeometry.Etale.isPerfect_ihom_rightDerivedGlobalSections_integral", "AlgebraicGeometry.Etale.rationalHomology_globalSections", "AlgebraicGeometry.ProEtale.isPerfect_compactlySupportedGlobalSections_adic", "AlgebraicGeometry.ProEtale.isPerfect_rightDerivedGlobalSections_adic", "AlgebraicGeometry.ProEtale.isPerfect_ihom_compactlySupportedGlobalSections_adic", "AlgebraicGeometry.ProEtale.isPerfect_ihom_rightDerivedGlobalSections_adic"]
order = 2384
uses = ["sk-prop-sf-trace-perfectness", "sk-thm-sf-ctf-stability", "sk-thm-sf-direct-image-tor-amplitude"]
tags = ["sketch"]
+++
Let $\Lambda$ be an admissible coefficient ring, and for a scheme $X$ let
$a_X\colon X\to s=\operatorname{Spec}k$ be its structure morphism.

Suppose $k$ is algebraically closed. The category
$\Dctf(s,\Lambda)$ identifies with
$\operatorname{Perf}(\Lambda)$, the category of bounded complexes of
finite projective $\Lambda$-modules up to quasi-isomorphism. For
$K\in\Dctf(X,\Lambda)$, both

$$
 \RGammac(X,K)=Ra_{X!}K,\qquad \RGamma(X,K)=Ra_{X*}K
$$

are perfect complexes. Their duals $R\operatorname{Hom}_\Lambda(-,\Lambda)$ are perfect, and
the evaluation map $P\to R\operatorname{Hom}_\Lambda(R\operatorname{Hom}_\Lambda(P,\Lambda),
\Lambda)$ is an isomorphism for each of them.

*Complement.* If the cohomology sheaves of $K$ lie in degrees $[a,b]$, then
$\RGammac(X,K)$ and $\RGamma(X,K)$ have cohomology only in degrees
$[a,b+2\dim X]$. For $\Lambda=\Oe$ both lie in $D^b_{\mathrm{fg}}(\Oe)$, and
their reductions modulo $\varpi_E^n$ are perfect of one common Tor amplitude,
independent of $n$. At the field stages $E$ and $\Qlb$ they are bounded with
finite-dimensional cohomology.
