+++
kind = "proof"
of = "dag-def-sfb-pullback-from-point-comp-iso"
tags = ["sheaf-dag"]
+++
1. By `def-sfb-upper-star-from-point`, the point pullback is the composite of the point inverse-image functor with pullback along the structure morphism: p_Y^* = pointUpperStar followed by (toSpecZ Y)^* and p_X^* = pointUpperStar followed by (toSpecZ X)^*. Here the point inverse-image functor is the one induced by the profinite-to-pro-etale construction of `def-sfb-profinite-to-proetale`. Thus the source is, up to the canonical reassociation Functor.associator, pointUpperStar followed by (toSpecZ Y)^* followed by f^*, while the target is pointUpperStar followed by (toSpecZ X)^*. (uses `def-sfb-profinite-to-proetale`)
2. Apply `def-sfb-finite-upper-star-comp` with h₁ = f and h₂ = toSpecZ Y, with coefficients Ab. Its Lean comparison upperStarComp Ab f (toSpecZ Y) is the natural isomorphism (f ≫ toSpecZ Y)^* ≅ (toSpecZ Y)^* ⋙ f^*, so its inverse is (toSpecZ Y)^* ⋙ f^* ≅ (f ≫ toSpecZ Y)^*. Whiskering this inverse on the left by pointUpperStar using the Mathlib construction Functor.isoWhiskerLeft gives the corresponding natural isomorphism after the point pullback, and Functor.associator puts it in the source's displayed parenthesization. (uses `def-sfb-finite-upper-star-comp`)
3. The terminality of Spec Z is expressed in Lean by comp_toSpecZ f : f ≫ toSpecZ Y = toSpecZ X. Applying congrArg (upperStar Ab) to this equality and then eqToIso identifies (f ≫ toSpecZ Y)^* with (toSpecZ X)^*. Composing this identification with the isomorphism of the preceding step yields the natural isomorphism f^* ⋙ p_Y^* ≅ p_X^*; this is exactly the composite defining upperStarFromPointComp.

Proof dependencies not drawn: `def-sfb-profinite-to-proetale`, `def-sfb-finite-upper-star-comp`.
