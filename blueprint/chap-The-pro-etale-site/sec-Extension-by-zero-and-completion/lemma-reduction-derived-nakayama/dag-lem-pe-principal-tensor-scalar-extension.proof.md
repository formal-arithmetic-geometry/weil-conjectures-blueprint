+++
kind = "proof"
of = "dag-lem-pe-principal-tensor-scalar-extension"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-internal-kflat-scalar-tower-realization"]
+++
1. Specialize KFlatScalarTower.derived_realization to the native quotient tower. Its natural_computation identifies extension/restriction with termwise tensor, using the canonical mapModComapIso for the pulled-back finite modules. The scalar comparison satisfies the specified transitions and units. (uses [dag-lem-pe-internal-kflat-scalar-tower-realization])
2. The lax tensorator of Q followed by mapBifunctorSingle₂Iso compares the actual derived right tensor with termwise right tensor. It is natural, invertible on K-flat complexes, and intertwines coefficient morphisms. Its unit equation is lax monoidal right unitality followed by the degreewise right-unitor formula. (uses [dag-lem-pe-internal-kflat-scalar-tower-realization], `def-weil-abstract-derived-category`)
3. On K-flat complexes compose the derived tensor comparison with the inverse scalar comparison. Cancel the scalar comparison to prove transition and unit compatibility. The inclusion of K-flat complexes followed by Q is a localization. Fully faithful precomposition descends this natural isomorphism and both equations to the derived category. (uses [dag-lem-pe-internal-kflat-scalar-tower-realization])

Proof dependencies not drawn: `def-weil-abstract-derived-category`, `def-sfb-modobj-transport`, `sk-def-sfb-transport`.
