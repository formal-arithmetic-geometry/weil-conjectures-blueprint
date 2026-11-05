+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--6"
order = 425013
uses = ["proposition-proper-direct-image-constructible-complexes--2", "proposition-proper-direct-image-constructible-complexes--5", "lemma-integral-models", "lemma-reduction-derived-nakayama", "proposition-integral-constructibility-criterion", "lemma-change-coefficients"]
+++
It suffices to test each component at $K\in\Dbc(X,\mathcal O_E)$.
Both terms are bounded constructible, by
[proposition-proper-direct-image-constructible-complexes--2] and stability under
inverse image [lemma-integral-models]. The coefficient comparisons identify the
first derived reduction of the base change map with the finite-coefficient base
change map at $K\otimes^{\mathbf L}_{\mathcal O_E}\mathbf F_E$.
This reduction is bounded constructible of étale origin, so
[proposition-proper-direct-image-constructible-complexes--5] applies.
Derived Nakayama [lemma-reduction-derived-nakayama] then reflects invertibility.

The two intermediate results are
`AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_derivedReduction_boundedConstructibleBaseChange`
and
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_integral_app_of_reduction`.
Thus the proof tests the ordinary base change map directly after reduction.
