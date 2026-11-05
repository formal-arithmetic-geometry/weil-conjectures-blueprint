+++
kind = "proof"
of = "proposition-weights-under-usual-operations--6"
order = 1070007
uses = ["lemma-filtrations-spectra"]
+++
The Frobenius-equivariant identification
`AlgebraicGeometry.WeilSheaf.stalkTensorObjEquiv` identifies the stalk
of $\mathcal F\otimes\mathcal G$ with
$\mathcal F_{\bar x}\otimes\mathcal G_{\bar x}$. Its eigenvalues
are products $\alpha\beta$, so
$|\iota(\alpha\beta)|=q_x^{a/2}q_x^{b/2}=q_x^{(a+b)/2}$.
This is `FrobeniusModule.IsPureOfWeight.tensor`, transported through
the stalk identification. Lissity of the first factor is a hypothesis
of the tensor product used here.
