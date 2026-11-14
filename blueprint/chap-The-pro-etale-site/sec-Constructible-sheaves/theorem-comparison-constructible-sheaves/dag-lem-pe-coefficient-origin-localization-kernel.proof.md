+++
kind = "proof"
of = "dag-lem-pe-coefficient-origin-localization-kernel"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-fixed-closed-unit-epi", "dag-lem-pe-coefficient-fixed-kernel-comparison"]
+++
1. Apply the canonical closed-unit epimorphy theorem and the independent kernel comparison theorem. For an arbitrary adjunction with the same left and right functors, Adjunction.leftAdjointUniq gives an isomorphism of left adjoints and its unit formula writes the new unit as the canonical unit followed by an invertible direct-image morphism. Postcomposition by an isomorphism preserves epimorphy. kernel.mapIso identifies the two kernels, and essential-image membership is invariant under this isomorphism. (uses [dag-lem-pe-coefficient-fixed-closed-unit-epi], [dag-lem-pe-coefficient-fixed-kernel-comparison])
