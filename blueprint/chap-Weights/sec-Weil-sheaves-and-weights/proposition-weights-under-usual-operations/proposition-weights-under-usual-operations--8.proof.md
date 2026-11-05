+++
kind = "proof"
of = "proposition-weights-under-usual-operations--8"
order = 1070009
uses = ["lemma-filtrations-spectra"]
+++
Identify the stalk of the tensor product with the tensor product of
the stalks using `AlgebraicGeometry.WeilSheaf.stalkTensorObjEquiv`.
For every product eigenvalue,
$|\iota(\alpha\beta)|\le q_x^{a/2}q_x^{b/2}=q_x^{(a+b)/2}$.
Lean applies `FrobeniusModule.HasWeightsAtMost.tensor` and transports
the bound through this identification. No mixed filtration is
constructed in this argument.
