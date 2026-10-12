+++
kind = "proof"
of = "lem-weil-pbc-etale-near-prime-naive-cotangent-vanishing"
+++
Apply `Algebra.etaleLocus_eq_compl_support` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Etale/Locus.lean)) at q: the hypotheses give q in Algebra.etaleLocus A C. In Lean rewrite Algebra.etaleLocus_eq_compl_support and use Module.notMem_support_iff on each of the two localized modules. Thus Algebra.IsEtaleAt A q holds.

Apply Mathlib Algebra.exists_etale_of_isEtaleAt (Mathlib/RingTheory/Etale/Locus.lean:103) to the finitely presented algebra C and the preceding IsEtaleAt instance. It gives h not in q and Algebra.Etale A (Localization.Away h). This is a single application of the existing theorem, whose proof uses openness of the etale locus and the basic-open basis; no new intermediate theory is needed.

By `AlgebraicGeometry.HasRingHomProperty.Spec_iff` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/RingHomProperties.lean)), the corresponding spectrum morphism is etale. In Lean apply HasRingHomProperty.Spec_iff with P := @AlgebraicGeometry.Etale, then RingHom.etale_algebraMap to the ring-theoretic conclusion. Pair this with h not in q.
