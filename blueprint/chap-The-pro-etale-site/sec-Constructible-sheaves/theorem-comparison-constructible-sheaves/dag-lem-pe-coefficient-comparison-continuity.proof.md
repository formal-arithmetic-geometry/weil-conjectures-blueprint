+++
kind = "proof"
of = "dag-lem-pe-coefficient-comparison-continuity"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-comparison-representables", "dag-lem-pe-coefficient-comparison-presentation-sheafification"]
+++
1. Lift the presentation diagram to the coefficient-sized etale model. Its comparison image is naturally isomorphic to P.diagram followed by AsSmall.up. Reflect P.isLimit through the fully faithful site forgetful functor and preserve it with the AsSmall equivalence. Apply representable continuity and the full-faithful left-Kan-extension colimit criterion from WeilConjectures.CategoryTheory.Pro.PresheafColimit; transport preservation along the displayed diagram isomorphism. This constructs an actual IsColimit for the raw Kan-extension cocone. (uses [dag-lem-pe-coefficient-comparison-representables])
2. Apply affine-presentation sheafification invertibility at every stage and at the vertex. Naturality of toSheafify transports the raw Kan-extension colimit to the sheafified functor, using isColimitMapCoconeOfNatTrans. The definition of sheafPullback and sectionCocone identifies the result with the original theorem, with its projection maps unchanged. (uses [dag-lem-pe-coefficient-comparison-presentation-sheafification])
