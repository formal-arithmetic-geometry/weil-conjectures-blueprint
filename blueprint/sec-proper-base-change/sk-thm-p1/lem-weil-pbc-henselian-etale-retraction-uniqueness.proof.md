+++
kind = "proof"
of = "lem-weil-pbc-henselian-etale-retraction-uniqueness"
uses = ["lem-weil-pbc-root-lifting-etale-retraction"]
+++
Use HenselianLocalRing.TFAE to obtain monic simple-root lifting. Let x be the prime q' in Spec B and y its image in Spec S. The affine residue-field isomorphisms identify beta:B→kappa(x) and alpha:S→kappa(y). Naturality gives beta composed with phi equal to the scheme residue-field map composed with alpha. The given ideal residue-field bijection, composed with S→kappa(m), makes S→kappa(q') surjective; transport across the affine residue-field isomorphism makes beta composed with phi surjective. Thus the scheme residue-field map is surjective, and it is injective because it is a homomorphism of fields. (`AlgebraicGeometry.Scheme.residueField` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/ResidueField.lean))).

Apply the already proved root-lifting retraction theorem with phi.toAlgebra, this root-lifting property, and the converted residue-field bijection. Both given algebra maps have maximal-ideal preimage q', so uniqueness identifies each with the unique retraction, and transitivity identifies them with each other. The standard-etale presentation and simple-root uniqueness argument remain in the imported theorem, so the unit route is preserved. ([lem-weil-pbc-root-lifting-etale-retraction]).
