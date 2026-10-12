+++
kind = "proof"
of = "lem-weil-pbc-etale-pullback-internal-hom"
+++
Identify étale pullback with the localization restriction using Etale.upperStarIsoLocalizationRestriction. Compute the unit of the restriction/pushforward adjunction sectionwise and verify its tensor and unit identities; these prove that the identification is monoidal. This is the étale specialization of the pro-étale argument in WeilConjectures.SixFunctors.ProEtale.UpperLowerStar.InternalHom.

Composition with an étale morphism induces equivalences on every slice, by CategoryTheory.MorphismProperty.Over.isEquivalence_post_map_op. Thus the presheaf restriction comparison is invertible by CategoryTheory.isIso_ihomComparison_whiskeringLeft. The sheaf inclusion comparison is invertible by CategoryTheory.Monoidal.Reflective.isIso_ihomComparison. Apply the composition formula for comparison transformations, and reflect isomorphisms through sheafToPresheaf to obtain the comparison for localization restriction.

Transport invertibility through the monoidal pullback/restriction identification, using isIso_ihomComparison_of_iso. Evaluate the comparison transformation at G and use asIso to construct the requested isomorphism.
