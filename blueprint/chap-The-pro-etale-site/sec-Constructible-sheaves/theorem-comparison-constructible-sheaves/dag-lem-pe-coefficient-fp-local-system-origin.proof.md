+++
kind = "proof"
of = "dag-lem-pe-coefficient-fp-local-system-origin"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-fp-local-system-etale-cover", "dag-lem-pe-coefficient-comparison-constant-chart-counit"]
+++
1. Apply coefficientFpLocalSystem_etaleCover to obtain etale objects V_i whose pro-etale images cover the final object, with constant finitely presented slice models of F. (uses [dag-lem-pe-coefficient-fp-local-system-etale-cover])
2. For each chart apply coefficientComparison_counit_isIso_of_constant_over to its actual slice isomorphism. Finite presentation is unnecessary for this counit calculation. Mathlib Sheaf.isIso_of_coversTop then makes the global canonical comparison counit at F invertible. (uses [dag-lem-pe-coefficient-comparison-constant-chart-counit])
3. Take the canonical sectionwise comparison direct image of F as the etale antecedent. The isomorphism asIso of its comparison counit is exactly an isomorphism from the prescribed comparison inverse image to F; this witnesses essential-image membership.
