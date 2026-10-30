+++
id = "sk-lem-finite"
kind = "lemma"
title = "Perfect complexes at the geometric point"
order = 502
lean = ["AlgebraicGeometry.WeilSheaf.subsingleton_cohomology_adicConstant", "DerivedCategory.IsPerfect.tensor_homology", "DerivedCategory.isPerfect_of_finiteTorAmplitude", "DerivedCategory.IsPerfect.ihom_unit", "AlgebraicGeometry.ProEtale.isPerfect_compactlySupportedGlobalSections_adic", "AlgebraicGeometry.ProEtale.isPerfect_rightDerivedGlobalSections_adic", "AlgebraicGeometry.ProEtale.isPerfect_ihom_compactlySupportedGlobalSections_adic", "AlgebraicGeometry.ProEtale.isPerfect_ihom_rightDerivedGlobalSections_adic"]
uses = ["sk-prop-sf-trace-perfectness", "sk-thm-sf-ctf-stability", "sk-cor-sf-direct-image-ctf"]
tags = ["sketch"]
+++
Suppose $k$ is algebraically closed. The category
$D^b_{\mathrm{ctf}}(s,\Lambda)$ identifies with
$\operatorname{Perf}(\Lambda)$, the category of bounded complexes of
finite projective $\Lambda$-modules up to quasi-isomorphism. For
$K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, both

$$
R\Gamma_c(X,K)=Ra_{X!}K,\qquad R\Gamma(X,K)=Ra_{X*}K
$$

and every geometric stalk $K_{\bar x}$ are perfect complexes. Their duals $R\!\operatorname{Hom}_\Lambda(-,\Lambda)$ are perfect, and
the evaluation map $P\to R\!\operatorname{Hom}_\Lambda(R\!\operatorname{Hom}_\Lambda(P,\Lambda), \Lambda)$ is an isomorphism for each of them.

*Complement.* If the cohomology sheaves of $K$ lie in degrees $[a,b]$, then
$\RGammac(X,K)$ and $\RGamma(X,K)$ have cohomology only in degrees
$[a,b+2\dim X]$. For $\Lambda=\Oe$ both lie in $D^b_{\mathrm{fg}}(\Oe)$, and
their reductions modulo $\pi_E^n$ are perfect of one common Tor amplitude,
independent of $n$. For $\Lambda=E,\Qlb$ they are bounded with
finite-dimensional cohomology.
