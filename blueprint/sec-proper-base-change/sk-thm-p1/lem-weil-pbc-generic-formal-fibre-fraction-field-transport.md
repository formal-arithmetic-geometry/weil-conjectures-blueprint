+++
id = "lem-weil-pbc-generic-formal-fibre-fraction-field-transport"
kind = "lemma"
title = "Transport of generic formal-fibre regularity to a chosen fraction field"
lean = ["genericFormalFiber_geometricallyRegular_of_fractionField_transport"]
source = "literature/stacks-project/more-algebra.tex, Proposition Tag 07PS and Lemma Tag 07PP, decomposition of the assigned proof"
+++
theorem genericFormalFiber_geometricallyRegular_of_fractionField_transport (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] (K : Type u) [Field K] [Algebra A K] [IsFractionRing A K] (P : Ideal A) [P.IsPrime] (h : let C := AdicCompletion (IsLocalRing.maximalIdeal (Localization.AtPrime P)) (Localization.AtPrime P) Algebra.IsGeometricallyRegular (⊥ : Ideal A).ResidueField ((⊥ : Ideal A).Fiber C)) : let C := AdicCompletion (IsLocalRing.maximalIdeal (Localization.AtPrime P)) (Localization.AtPrime P) Algebra.IsGeometricallyRegular K (TensorProduct A K C)
