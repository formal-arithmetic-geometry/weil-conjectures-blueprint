+++
kind = "proof"
of = "proposition-weights-under-usual-operations--7"
order = 1070008
uses = ["lemma-filtrations-spectra"]
+++
The evaluation pairing identifies the stalk of the dual with the dual
of the stalk, compatibly with the inverse-transpose Frobenius; this is
`AlgebraicGeometry.WeilSheaf.stalkAtDualEquiv`. The inverse transpose
has eigenvalues $\alpha^{-1}$, of absolute value $q_x^{-a/2}$.
Lean uses `FrobeniusModule.IsPureOfWeight.dual` at each stalk, followed
by `FrobeniusModule.IsPureOfWeight.of_equiv`; for example, this is the
dual-purity step in
`AlgebraicGeometry.WeilSheaf.IsLisse.isPunctuallyPureOfWeight_of_upperStar`.
There is no separate sheaf theorem named
`AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.dual`.
