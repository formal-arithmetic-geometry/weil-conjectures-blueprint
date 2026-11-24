+++
id = "proposition-smooth-purity-finite-coefficients"
kind = "proposition"
title = "Smooth purity with finite coefficients"
order = 759
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_twistShift", "AlgebraicGeometry.Etale.smoothPurityIso"]
uses = ["definition-constructible-sheaves", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "definition-compactification-refinement"]
+++
Let $A$ be any finite admissible coefficient ring, and let
$f:X\to Y$ be smooth of pure relative dimension $d$.
For $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{Y_{\mathrm{pro}\acute{e}t}},A)$ there is a canonical
isomorphism, natural in $K$,

$$
f_A^{*}\href{@definition-tate-twists}{K(d)}[2d]
\xrightarrow{\ \gamma_{f,A}(K)\ }\href{@theorem-existence-exceptional-inverse-image}{f_A^{!}K}.
\tag{9.15}
$$
