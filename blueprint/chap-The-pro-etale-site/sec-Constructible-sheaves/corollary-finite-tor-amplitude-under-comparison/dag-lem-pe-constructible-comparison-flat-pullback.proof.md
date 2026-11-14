+++
kind = "proof"
of = "dag-lem-pe-constructible-comparison-flat-pullback"
tags = ["sheaf-dag"]
uses = ["dag-sk-thm-pe-constructible-comparison"]
+++
1. The transported continuous comparison inclusion and canonical constant-section ring map give a ringed-topos morphism with exactly the specified module pushforward. Apply the existing general K-flat pullback theorem and use uniqueness of left adjoints to identify its pullback with constructibleComparisonPullback. (uses [dag-sk-thm-pe-constructible-comparison], `def-weil-pbc-site-comparison-morphism`, `lem-weil-pbc-continuous-ringed-topos-module-direct-image`, `lem-weil-pbc-supplied-ringed-topos-kflat-pullback`)
2. Place the given flat module M in degree zero. All other terms are zero, hence flat. It is bounded above, so it is K-flat. The general pullback theorem gives flat terms for its image. Evaluate in degree zero and transport flatness along the single-complex term isomorphism and the left-adjoint isomorphism. (uses `lem-pc-bounded-above-flat-kflat-site`)
3. For any K-flat complex with flat terms, the same supplied ringed-topos theorem gives K-flatness of its termwise pullback. The natural isomorphism of left adjoints induces a complex isomorphism. Tensor it with each acyclic test and transport vanishing homology to the canonical comparison complex. (uses `lem-weil-pbc-supplied-ringed-topos-kflat-pullback`)

Proof dependencies not drawn: `def-weil-pbc-site-comparison-morphism`, `lem-weil-pbc-continuous-ringed-topos-module-direct-image`, `lem-weil-pbc-supplied-ringed-topos-kflat-pullback`, `lem-pc-bounded-above-flat-kflat-site`.
