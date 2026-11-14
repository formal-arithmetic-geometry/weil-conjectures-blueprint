+++
kind = "proof"
of = "dag-lem-pe-coefficient-comparison-fixed-pullback"
tags = ["sheaf-dag"]
uses = ["dag-def-pe-etale-constructible-module", "dag-lem-pe-coefficient-comparison-data"]
+++
1. The constant-ring unit is locally bijective. Scalar restriction is fully faithful by the Mathlib locally-surjective scalar-restriction Hom equivalence. To construct an antecedent of a fixed-scalar sheaf, apply module sheafification to the identity of its underlying abelian sheaf. The sheafification unit extends the scalar action; identity maps give its inverse isomorphism. Thus the literal coefficientModelFixedScalars functor is an equivalence. (uses [dag-def-pe-etale-constructible-module])
2. The ring-map adjunction equation states that constructibleComparisonRingMap sends each constant scalar to the same constant scalar. This identifies module direct image followed by scalar restriction with scalar restriction followed by fixed-scalar comparison direct image, by identity linear maps on sections. Conjugate through the two scalar equivalences and use uniqueness of left adjoints to identify the two comparison inverse images. (uses [dag-lem-pe-coefficient-comparison-data])
3. On site objects comparison and scheme base change commute: both are the same fibre product. Whisker the original site natural isomorphism by AsSmall.down and AsSmall.up. Its isomorphism on continuous direct images identifies the right adjoints of the two inverse-image composites. Uniqueness of left adjoints gives their inverse-image isomorphism. Whisker and compose it with the scalar comparison of the preceding step. (uses [dag-def-pe-etale-constructible-module], `def-weil-pbc-site-comparison-morphism`, `def-sfb-affine-locally-constructible-proetale-modules`)

Proof dependencies not drawn: `def-weil-pbc-site-comparison-morphism`, `def-sfb-affine-locally-constructible-proetale-modules`.
