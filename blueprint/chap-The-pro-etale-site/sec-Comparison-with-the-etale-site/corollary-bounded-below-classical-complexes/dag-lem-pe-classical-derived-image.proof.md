+++
kind = "proof"
of = "dag-lem-pe-classical-derived-image"
tags = ["sheaf-dag"]
uses = ["dag-sk-thm-pe-classical-sheaves"]
+++
1. Apply the module-valued clause of proEtaleClassicalSheaves to the cohomology sheaf of the source. Exact inverse image commutes with bounded-below derived homology. Naturality of continuityMap transports classicality along this isomorphism. The definition uses standard-model cohomology; identify it with small-model cohomology by cancelling the localization functor in their common factorization through complex homology and the ShrinkHoms equivalence. (uses [dag-sk-thm-pe-classical-sheaves], `lem-weil-pbc-exact-functor-bounded-below`)

Proof dependencies not drawn: `lem-weil-pbc-exact-functor-bounded-below`, `def-sfb-exact-derived-cohomology-comparison`.
