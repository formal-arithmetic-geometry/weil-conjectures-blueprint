+++
kind = "proof"
of = "dag-lem-pe-constructible-comparison-tensor-test-reflection"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-constructible-comparison-module-exact", "dag-sk-thm-pe-constructible-comparison"]
+++
1. Apply exactness and faithfulness of the intrinsic coefficient-sized comparison module pullback. Its left adjoint preserves finite colimits, so finite-limit preservation makes it homology preserving. (uses [dag-lem-pe-constructible-comparison-module-exact], [dag-sk-thm-pe-constructible-comparison])
2. Construct the supplied ringed-topos morphism from the canonical continuous site comparison and constant-section ring map. Its tensor pullback is left adjoint to the specified module pushforward, hence naturally isomorphic to constructibleComparisonPullback. Transport the canonical ordinary tensor-product comparison and its naturality through this left-adjoint isomorphism. (uses `lem-weil-pbc-continuous-ringed-topos-module-direct-image`, `lem-weil-pbc-supplied-ringed-topos-kflat-pullback`, `lem-weil-pbc-canonical-ringed-tensor-comparison-construction`)
3. The mapBifunctorSingle₂Iso identifies the ordinary total tensor with M in degree zero with the termwise tensor-right complex. The natural tensor comparison supplies an isomorphism between pullback of that complex and the tensor-right complex after pullback. Homology preservation identifies its homology with the pullback of etale homology. Use faithfulness to reflect id=0, then transport back through the single-tensor isomorphism. (uses [dag-lem-pe-constructible-comparison-module-exact], `def-pc-tensor-complex-sheaves`)

Proof dependencies not drawn: `lem-weil-pbc-continuous-ringed-topos-module-direct-image`, `lem-weil-pbc-supplied-ringed-topos-kflat-pullback`, `lem-weil-pbc-canonical-ringed-tensor-comparison-construction`, `def-pc-tensor-complex-sheaves`.
