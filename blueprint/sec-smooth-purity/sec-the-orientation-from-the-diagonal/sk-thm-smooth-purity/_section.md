+++
id = "sk-thm-smooth-purity"
kind = "proposition"
title = "Smooth purity with finite coefficients"
order = 457
lean = ["AlgebraicGeometry.Etale.nonempty_iso_dualizingComplex_twistShift", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_twistShift"]
uses = ["sk-prop-cohsm", "sk-lem-diag-reg", "sk-prop-an", "sk-thm-dnc", "sk-prop-sp-orientation", "sk-lem-sp-finite-existence", "sk-lem-sp-reduction", "sk-thm-existence"]
tags = ["sketch"]
+++
Let $A$ be any finite admissible coefficient ring, and let
$f:X\to Y$ be smooth of pure relative dimension $d$.
For $K\in D^b_{\mathrm{ctf}}(Y_{\mathrm{pro}\acute{e}t},A)$ there is a canonical
isomorphism, natural in $K$,

$$
f_A^{*}K(d)[2d]
\xrightarrow{\ \gamma_{f,A}(K)\ }f_A^{!}K.
\tag{10.14}
$$
