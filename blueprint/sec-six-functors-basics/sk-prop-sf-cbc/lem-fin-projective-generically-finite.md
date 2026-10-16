+++
id = "lem-fin-projective-generically-finite"
kind = "lemma"
title = "A projective family with finite generic fibre is generically finite"
lean = ["AlgebraicGeometry.ProjectiveSpace.exists_isFinite_morphismRestrict_of_generic_fibre"]
order = 1960
uses = ["def-pc-projective-space-twist", "def-weil-pbc-scheme-conventions", "lem-pc-projective-coherent-finiteness", "lem-pc-projective-space-serre-vanishing", "lem-weil-pbc-proper-closed-image"]
+++
Let $A$ be a Noetherian domain with fraction field $K$, and let
$D\to\operatorname{Spec}A$ be
projective.
If $D_K$ has dimension at most zero, this morphism is finite after
restriction to a nonempty open of $\operatorname{Spec}A$.
