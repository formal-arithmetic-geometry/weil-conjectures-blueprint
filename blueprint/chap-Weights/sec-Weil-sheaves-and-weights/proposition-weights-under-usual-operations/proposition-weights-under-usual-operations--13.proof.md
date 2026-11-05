+++
kind = "proof"
of = "proposition-weights-under-usual-operations--13"
order = 1070014
uses = ["definition-weights"]
+++
The isomorphism `AlgebraicGeometry.WeilComplex.homologySheafShiftIso`
gives $\mathcal H^i(K[r])\simeq\mathcal H^{r+i}(K)$. Transport the
mixed bound $w+(r+i)$ through this isomorphism using
`AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.of_iso`, and rewrite
it as $(w+r)+i$. This is the defining bound for $K[r]$.
