+++
id = "prop-trf-compact-support-perfectness"
kind = "theorem"
title = "Compact-support perfectness"
lean = ["AlgebraicGeometry.Etale.isPerfect_compactlySupportedGlobalSections", "AlgebraicGeometry.Etale.isPerfect_geometricStalk"]
order = 3181
tags = ["latex:proposition"]
uses = ["def-compact-support-direct-image-detailed", "def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-weil-finite-coefficient-point", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-full-cohomological-dimension", "def-weil-scheme-morphism-properties", "lem-trf-finite-tor-amplitude-perfect", "prop-finite-compact-support-constructibility", "prop-weil-pbc-inverse-image-exact", "lem-sf-projection-finite-constant", "lem-sf-proetale-constructible-origin", "lem-exc-comparison-tor-interval", "prop-weil-pbc-comparison-direct-image", "lem-sf-etale-direct-image-vanishing", "obl-fin-comparison"]
+++
Fix the global finite-field datum
and the coefficient
conventions, and let $K\in D^b_{ctf}(X,A)$ with structure morphism
$a_X:X\to\Spec k$ separated finite type. Then

$$
R\Gamma_c(X,K)\in D^b_{\mathrm{fin}}(A),
$$

and the derived geometric stalk $K_{\bar x}=L\bar x^*K$ lies in
$D^b_{\mathrm{fin}}(A)$ for every
geometric point
$\bar x$ of $X$.
