+++
id = "lem-weil-pbc-gabber-principal-open-closed-presentation"
kind = "lemma"
title = "A principal open of a quotient spectrum has a closed presentation over a normal domain with separably closed fraction field"
uses = ["def-pc-separably-closed"]
lean = ["AlgebraicGeometry.gabber_principal_open_closed_presentation"]
source = "literature/stacks-project/etale-cohomology.tex, Lemma 09ZC, proof third and fourth sentences; the empty-open case is written out."
+++
Let R be a normal domain `IsIntegrallyClosed, IsDomain, Localization.AtPrime` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/IntegrallyClosed.lean)) with separably closed fraction field [def-pc-separably-closed]. For an ideal I of R and h in R/I, there exists a normal domain S with separably closed fraction field and a closed immersion `AlgebraicGeometry.IsClosedImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean)) from the open subscheme D(h) of Spec(R/I) `AlgebraicGeometry.Spec` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Scheme.lean)), `AlgebraicGeometry.IsOpenImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/OpenImmersion.lean)) into Spec S. This includes empty D(h) and I = R.
