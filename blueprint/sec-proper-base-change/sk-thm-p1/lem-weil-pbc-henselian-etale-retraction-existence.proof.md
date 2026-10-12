+++
kind = "proof"
of = "lem-weil-pbc-henselian-etale-retraction-existence"
uses = ["lem-weil-pbc-root-lifting-etale-retraction"]
+++
Use HenselianLocalRing.TFAE to obtain lifting of simple roots of monic polynomials from the henselian local ring instance. This is exactly the root-lifting hypothesis of lem-weil-pbc-root-lifting-etale-retraction.

Convert the ideal residue-field hypothesis to the scheme residue-field hypothesis. Put x=q' and y=Spec(phi)(x). The affine residue-field isomorphisms give maps beta:B→kappa(x) and alpha:S→kappa(y). Naturality of global evaluation gives beta composed with phi equal to the scheme residue-field map composed with alpha. The composite S→kappa(q') is surjective: it is the given bijective ideal residue-field map composed with the surjective map S→kappa(m). Transport through the affine residue-field isomorphism makes beta composed with phi surjective. Therefore the scheme residue-field map is surjective; it is injective as a homomorphism of fields. (`AlgebraicGeometry.Scheme.residueField` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/ResidueField.lean))).

Apply lem-weil-pbc-root-lifting-etale-retraction with this root-lifting property and the converted residue-field bijectivity. Forget the uniqueness part to obtain the requested algebra homomorphism with maximal-ideal preimage q'. ([lem-weil-pbc-root-lifting-etale-retraction]).
