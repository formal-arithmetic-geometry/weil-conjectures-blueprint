+++
id = "thm-fin-projective-smooth-curve-finiteness"
kind = "theorem"
title = "Constant-coefficient finiteness for projective smooth curves"
order = 5186
lean = ["AlgebraicGeometry.Etale.isConstructible_higherDirectImage_constant_of_smoothProjective_curve"]
uses = ["def-sbc-smooth-morphisms", "lem-fin-projective-curve-betti-cardinalities", "fin4-lem-stalk-constructibility-criterion"]
+++
Let $S$ be Noetherian and let $f:X\to S$ be projective and smooth
[def-sbc-smooth-morphisms], with geometric fibres of pure dimension one. If
$\ell$ is a prime invertible on $S$, every higher direct image
$R^rf_*\mathbf F_\ell$ is constructible.

## Proof

The morphism is proper, since projective morphisms are proper. Proper base
change identifies its stalks with $H^r(X_{\bar s},\mathbf F_\ell)$. These
stalks are finite and have constructible cardinalities by
[lem-fin-projective-curve-betti-cardinalities]. The criterion
[fin4-lem-stalk-constructibility-criterion] now applies to the sheaf
$R^rf_*\mathbf F_\ell$.

Proper base change was used only as an isomorphism; finiteness of the fibre
groups came from the curve calculation.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:pc-projective-morphism, def:weil-pbc-direct-image, def:weil-pbc-constructible-complexes, cor:weil-pbc-geometric-fiber-finite, lem:pc-projective-proper
