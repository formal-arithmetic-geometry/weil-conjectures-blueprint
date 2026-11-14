+++
kind = "proof"
of = "dag-lem-pur-identified-ring-pullback-finite-limits"
tags = ["sheaf-dag"]
uses = ["dag-lem-pur-signed-line-sheaf-pullback-forget", "dag-lem-pur-signed-line-module-inverse-image-adjunction"]
+++
1. Obtain ring and abelian sheafification in the coefficient universe by equivalence with the small model. The site functor is representably flat because it preserves finite limits; hence the constructed ring, set and abelian inverse images preserve finite limits. Uniqueness of ring left adjoints identifies the ring inverse image with rInv. Its invertible adjunct of a gives the ring unit presentation. (uses [dag-lem-pur-signed-line-sheaf-pullback-forget])
2. Apply inverseImage_underlying_of_ring_presentation, then forget to sets and use the comparison with set inverse image. The underlying abelian inverse image preserves finite limits, and module forgetting reflects them, so the specified module pullback preserves finite limits. (uses [dag-lem-pur-signed-line-module-inverse-image-adjunction])
