+++
kind = "proof"
of = "proposition-function-sheaf-dictionary--3"
order = 1028009
uses = ["corollary-trace-functions-direct-image-compact", "proposition-frobenius-local-term-curve"]
+++
The Lean proof of the relative identity in
[corollary-trace-functions-direct-image-compact] first establishes its
generic form (`AlgebraicGeometry.ProEtale.CondensedRing.shriekTraceFunctionGenericallyHolds`).
The base cases are finite étale maps, coordinate projections of affine
spaces, and closed immersions. The affine-line case is obtained from the
relative projective line, using the trace formula on its proper smooth
curve fibres and [proposition-frobenius-local-term-curve]. The base cases
are combined by composition after
passing to a stable open subset and a finite étale quotient by the
finite-order automorphism. Noetherian induction, using open–closed
additivity, then gives
`AlgebraicGeometry.ProEtale.CondensedRing.weilShriekTraceFunction_of_genericallyHolds`.
Write $m=n+1$ and convert the finitely supported sum into the finite sum
over the fibre of the map of Frobenius-fixed points.
