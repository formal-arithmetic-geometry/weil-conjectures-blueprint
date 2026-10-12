+++
kind = "proof"
of = "lem-weil-pbc-localization-prime-residue-field-iso"
+++
Apply Mathlib IsLocalization.isPrime_iff_isPrime_disjoint to q' to obtain primality of its contraction q and disjointness from W. For every prime p disjoint from W, apply isPrime_of_isPrime_disjoint and under_map_of_isPrime_disjoint to obtain primality of the extension and contraction of the extension equal to p.

Mathlib IsLocalization.map_under gives extension of contraction equal to q'. For BijOn comap, the preceding prime/disjoint equivalence gives maps-to; IsLocalization.orderEmbedding gives injectivity; and mapping p to its extension, with the preceding contraction identity, gives surjectivity.

Apply Mathlib IsLocalization.isLocalization_isLocalization_atPrime_isLocalization W to the localization of A' at q'. This specializes localization transitivity to prove that it is a localization of A at q. IsLocalization.algEquiv then gives e between the two localizations at q. Localization.localRingHom_unique identifies its ring homomorphism with the required canonical map, since e.commutes and the scalar-tower algebraMap identity give equality on A. (`Localization.AtPrime, Ideal.ResidueField, Ideal.Fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/AtPrime/Basic.lean)), `IsLocalization.localization_localization_isLocalization` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/LocalizationLocalization.lean))).

Rewrite both extended prime ideals as maximal ideals by Localization.AtPrime.map_eq_maximalIdeal. IsLocalRing.map_ringEquiv_maximalIdeal shows that e carries one onto the other. Use IsLocalRing.ResidueField.mapAlgEquiv e for the A-algebra equivalence of residue fields; its mapAlgEquiv_residue identity proves compatibility with every residue class. (`Localization.AtPrime, Ideal.ResidueField, Ideal.Fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Localization/AtPrime/Basic.lean))).
