+++
id = "thm-cbc-finite-torsion"
kind = "theorem"
title = "Compact-support base change at finite coefficients"
order = 1529
uses = ["cor-cbc-derived-extension-zero-base-change", "def-cbc-compact-support-square", "def-cbc-exchange-map", "def-compact-support-direct-image-detailed", "def-weil-compactifications-refinements", "def-weil-pbc-derived-categories", "def-weil-pbc-etale-sheaves", "prop-compactification-coherence-detailed", "thm-nagata-compactification", "thm-weil-pbc-bounded-below"]
+++
Let $\square$ be a
compact-support
base-change square with $f:X\to Y$ separated of finite type, let
$\Lambda$ be a finite commutative ring and let $g:Y'\to Y$ be
arbitrary. For every derived category

$$
K\in D^+(X_{\Et},\Lambda)
$$

the exchange map

$$
\operatorname{Ex}_!(K):g^{-1}Rf_!K\xrightarrow{\ \sim\ }
Rf'_!g'^{-1}K
$$

of [def-cbc-exchange-map] is an isomorphism in
$D^+(Y'_{\Et},\Lambda)$; it is natural in $K$, is the identity for
identity base changes, and satisfies horizontal and vertical pasting
after inserting the canonical associativity isomorphisms. It is
independent of the chosen compactification.
