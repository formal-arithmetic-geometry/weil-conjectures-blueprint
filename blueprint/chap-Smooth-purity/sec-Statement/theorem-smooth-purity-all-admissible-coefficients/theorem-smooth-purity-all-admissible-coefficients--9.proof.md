+++
kind = "proof"
of = "theorem-smooth-purity-all-admissible-coefficients--9"
order = 730021
uses = ["theorem-smooth-purity-all-admissible-coefficients--2", "proposition-six-operations-change-coefficients", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "theorem-proper-base-change-classical-pro", "lemma-sp-reduction"]
+++
The orientations of $f$ and $f'$ are isomorphisms by their construction: extend an integral isomorphism from [theorem-smooth-purity-all-admissible-coefficients--2], choose an invertible orientation, and transport through the open image. Exceptional base change at the unit is an isomorphism by reduction to finite coefficients; the reduction comparisons commute with proper base change. The unit comparison is also an isomorphism.

Let $c=f'^!(\eta_g)\circ\beta\circ g'^*\gamma_f$. Then $c$ is an isomorphism. Take $\tau=\gamma_{f'}^{-1}\circ c$; cancellation proves the displayed equality. This is `AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation_baseChange_of_isIso`. It establishes existence of a comparison, without identifying it with the canonical Tate comparison.
