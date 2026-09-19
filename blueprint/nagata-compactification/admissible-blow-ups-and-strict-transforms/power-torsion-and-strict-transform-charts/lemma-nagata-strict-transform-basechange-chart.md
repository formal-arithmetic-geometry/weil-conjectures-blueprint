+++
id = "lemma-nagata-strict-transform-basechange-chart"
kind = "lemma"
title = "Ordinary base-change chart"
order = 319
uses = ["def-nagata-strict-transform-basechange-chart-ring", "prop-nagata-affine-blowup-chart"]
+++
**Status.** Bypassed by the formalized route: the strict transform is
supplied by the API of
`WeilConjectures/Compactification/StrictTransform.lean` —
`AlgebraicGeometry.strictTransform`, its closed immersion
`AlgebraicGeometry.Scheme.IdealSheafData.isClosedImmersion_pullbackLift_blowup_comap`,
and the pullback square
`AlgebraicGeometry.isPullback_strictTransformOpen` — so the
strict-transform chart rings and their cocycle are never assembled by hand.

Over the $a$-chart of
$\operatorname{Bl}_I(\operatorname{Spec}A)$, the ordinary base change

$$
\operatorname{Spec}(B)\times_{\operatorname{Spec}A}
\operatorname{Bl}_I(\operatorname{Spec}A)
$$

is canonically $\operatorname{Spec}(C_a(A,B,I))$.

## Proof

Apply the affine fibre-product formula to the constructed chart
identification of [prop-nagata-affine-blowup-chart]. The tensor
product appearing in that formula is precisely
[def-nagata-strict-transform-basechange-chart-ring].
