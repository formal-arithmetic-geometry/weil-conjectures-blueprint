+++
id = "proposition-smooth-purity-finite-coefficients"
kind = "proposition"
title = "Smooth purity with finite coefficients"
order = 759
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_twistShift", "AlgebraicGeometry.Etale.smoothPurityIso"]
uses = ["proposition-composition-open-restriction-compactifications-f", "definition-relative-dualizing-complex"]
+++
Let $A$ be any finite admissible coefficient ring, and let
$f:X\to Y$ be smooth of pure relative dimension $d$.
For $K\in D^b_{\mathrm{ctf}}(Y_{\mathrm{pro}\acute{e}t},A)$ there is a canonical
isomorphism, natural in $K$,

$$
f_A^{*}K(d)[2d]
\xrightarrow{\ \gamma_{f,A}(K)\ }f_A^{!}K.
\tag{9.15}
$$
