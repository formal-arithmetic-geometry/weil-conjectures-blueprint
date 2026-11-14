+++
kind = "proof"
of = "dag-lem-pur-ringed-site-pullback-localization-universes"
tags = ["sheaf-dag"]
+++
1. The functor Over.star V sends X to V × X → V and is right adjoint to forgetting the slice. Product comparison U(V × X) ≅ U(V) × U(X) identifies the two composite module right adjoints. Naturality of a along the second projection verifies the coefficient square.
2. Uniqueness of left adjoints gives an isomorphism between slice restriction followed by F_V and F followed by target restriction. Under the composite adjunction its adjunct is the restricted global unit: compute both units at X using restriction along prod.snd; the equation prodComparison_snd and naturality of the global unit identify the components. Consequently the canonical comparison is that isomorphism.
3. Precompose with this comparison and apply the slice adjunction to obtain the claimed Hom equivalence. The triangle identity gives its unit formula and injectivity gives the local extensionality criterion. For the final assertion, Over.post U preserves finite limits and coverings; Mathlib isContinuous_iff_coverPreserving supplies continuity.
