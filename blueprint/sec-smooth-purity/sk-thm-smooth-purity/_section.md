+++
id = "sk-thm-smooth-purity"
kind = "theorem"
title = "Finite-coefficient smooth purity"
order = 2352
uses = ["sk-def-purity-conv", "sk-lem-diag-reg", "sk-prop-an", "sk-prop-cohsm", "sk-thm-dnc"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_dualizingComplex_twistShift", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_twistShift"]
tags = ["sketch"]
+++
In the conventions of [sk-def-purity-conv], let $f:X\to Y$ be smooth
separated of pure relative dimension $d$. Then

$$
\omega_f=Rf^{!}\Lambda_Y\ \cong\ \Lambda_X(d)[2d],
$$

canonically; for every $K\in D^b_{ctf}(Y,\Lambda)$ the tensor formula
[sk-prop-cohsm] (b) gives the purity isomorphism

$$
Rf^{!}K\ \cong\ Lf^{*}K(d)[2d].
$$

These isomorphisms are compatible with base change and with composition
of smooth morphisms (twist additivity). *Agreement on the model:*
for the projection $\pi$ of a vector bundle of rank $d$ (in particular for
$p_d:\Aaf^d_Y\to Y$) the isomorphism $\omega_\pi\cong\Lambda(d)[2d]$
constructed below is the $R\pi^{!}$-form $\gamma_{\pi,\Lambda}$ of
[sk-prop-an] (ii).
