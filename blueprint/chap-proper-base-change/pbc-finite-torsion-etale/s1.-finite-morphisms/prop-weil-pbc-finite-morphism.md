+++
id = "prop-weil-pbc-finite-morphism"
kind = "theorem"
title = "Finite morphisms satisfy proper base change"
order = 1555
lean = ["AlgebraicGeometry.Etale.isBaseChangeIsoSheaf_of_isFinite", "AlgebraicGeometry.Etale.isBaseChangeIso_of_isFinite"]
tags = ["latex:proposition"]
uses = ["def-weil-pbc-property", "lemma-weil-pbc-finite-exchange", "lemma-weil-pbc-property-iff-acyclicity"]
+++
Every finite morphism satisfies $\mathsf{PBC}$.

## Proof

The finite exchange lemma supplies the required isomorphism for every base
change and every torsion sheaf, which is exactly Definition
[def-weil-pbc-property]. Equivalently, the vanishing in the exactness
lemma gives $\mathsf{IA}$ and Lemma [lemma-weil-pbc-property-iff-acyclicity]
gives $\mathsf{PBC}$.
