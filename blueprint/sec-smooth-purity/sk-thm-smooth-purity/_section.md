+++
id = "sk-thm-smooth-purity"
kind = "proposition"
title = "Finite-coefficient smooth purity"
order = 1821
uses = ["sk-def-purity-conv", "sk-lem-diag-reg", "sk-prop-an", "sk-prop-cohsm", "sk-thm-dnc", "sk-prop-sp-orientation", "sk-prop-sp-tensor", "sk-lem-sp-finite-existence", "sk-lem-sp-reduction"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_dualizingComplex_twistShift", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_twistShift"]
tags = ["sketch"]
+++
Let $A$ be any finite admissible coefficient ring (a finite commutative ring
killed by a power of $\ell$), and let $f:X\to Y$ be smooth of pure relative
dimension $d$. For $K\in\Dctf(Y_{\mathrm{proét}},A)$ there is a canonical
isomorphism in $\Dctf(X_{\mathrm{proét}},A)$, natural in $K$,

$$
f_A^{*}K(d)[2d]\xrightarrow{\ \gamma_{f,A}(K)\ }f_A^{!}K .
$$
