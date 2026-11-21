+++
kind = "proof"
of = "dag-lem-pe-coefficient-comparison-representables"
tags = ["sheaf-dag"]
uses = ["dag-det-pe-classical-sheaves-image"]
+++
1. Use the sheaf-valued Yoneda equivalences and the comparison adjunction to construct an isomorphism from the inverse image of the lifted etale representable at V to the lifted pro-etale representable at its inclusion. The hom equivalences are natural in the target sheaf, so Coyoneda.ext constructs this isomorphism with no new mathematical assumption. (uses `def-weil-pbc-site-comparison-morphism`)
2. Apply the essential-image characterization det-pe-classical-sheaves-image to this isomorphism. Its IsClassical conclusion applies directly to the given affine presentation indexed in universe u+1, and makes the continuityMap of the lifted pro-etale representable bijective. Therefore the specified restriction cocone is colimiting, by IsColimit.ofPointIso applied to the chosen colimit. (uses [dag-det-pe-classical-sheaves-image])
3. A colimit cocone of sets is jointly surjective; its equality relation for a filtered diagram is eventual equality at one later stage. Transfer these two properties from the lifted pro-etale representable to the coefficient-sized opposite hom sets by ULift.up and ULift.down and the opposite-hom equivalence. Types.FilteredColimit.isColimitOf' then proves that coyoneda sends the opposite presentation cone to a colimit. Reflect the given limit along Scheme.ProEt.forget and preserve it along AsSmall.up; apply preservesColimit_of_preserves_colimit_cocone to that opposite cone. This uses the original larger index and keeps the coefficient universe independent.

Proof dependencies not drawn: `def-weil-pbc-site-comparison-morphism`.
