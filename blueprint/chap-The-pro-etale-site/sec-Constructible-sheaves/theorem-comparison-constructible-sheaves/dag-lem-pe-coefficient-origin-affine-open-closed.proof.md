+++
kind = "proof"
of = "dag-lem-pe-coefficient-origin-affine-open-closed"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-origin-localization-kernel", "dag-lem-pe-coefficient-origin-closed-direct-image", "dag-lem-pe-coefficient-comparison-injective-acyclic"]
+++
1. Let eta:F→i_*i^*F be the unit of the canonical fixed-module adjunction. By [dag-lem-pe-coefficient-origin-localization-kernel], eta is epic and its kernel has etale origin, using only the hypothesis on j^*F. The canonical kernel sequence ker eta→F→i_*i^*F is therefore short exact. (uses [dag-lem-pe-coefficient-origin-localization-kernel])
2. The hypothesis on i^*F and [dag-lem-pe-coefficient-origin-closed-direct-image] put the right endpoint i_*i^*F in the comparison essential image. (uses [dag-lem-pe-coefficient-origin-closed-direct-image])
3. Prove closure under extensions rather than restating it: [dag-lem-pe-constructible-comparison-module-exact] makes intrinsic comparison exact; [dag-lem-pe-coefficient-comparison-injective-acyclic] and the existing derived-adjunction acyclicity theorem make its bounded-below derived unit invertible. Lift the connecting map of the short exact sequence through this fully faithful derived functor, complete it to a triangle, and compare with the single-complex triangle of the sequence. Take zeroth homology: exact comparison commutes with homology, so H^0 of the lifted middle term is an antecedent of the given middle sheaf. Use the proved scalar equivalence of `lem-ctf-finite-comparison-model-realization`. The constant-section unit equation makes intrinsic and fixed-scalar direct image commute; conjugating this square through their adjunctions gives comparisonFixedLeft. This proved private isomorphism transports extension closure to fixed-module sheaves. Apply it to the canonical kernel sequence. No finite or Noetherian assumption is used. (uses [dag-lem-pe-coefficient-comparison-injective-acyclic], `lem-pe-constructible-comparison-module-exact`, `lem-ctf-finite-comparison-model-realization`)

Proof dependencies not drawn: `lem-pe-constructible-comparison-module-exact`, `lem-ctf-finite-comparison-model-realization`.
