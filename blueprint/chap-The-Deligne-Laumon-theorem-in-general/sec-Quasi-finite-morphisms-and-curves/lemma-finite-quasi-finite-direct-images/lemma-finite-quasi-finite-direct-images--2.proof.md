+++
kind = "proof"
of = "lemma-finite-quasi-finite-direct-images--2"
order = 1321005
uses = ["lemma-finite-quasi-finite-direct-images--1", "lemma-weights-exact-sequence", "proposition-weights-under-usual-operations"]
+++
For a sheaf $F$ in degree zero, $Rg_!F$ has no negative cohomology.
The assumed bounds on $R^rg_!F$ for $r\geq0$ therefore say precisely
that $Rg_!F$ is a complex of weights at most $v$. This is
`AlgebraicGeometry.WeilSheaf.isMixedOfWeightsAtMost_derivedLowerShriek_toComplex`.

Build a bounded constructible Weil complex $K$ from its cohomology
sheaves by truncation triangles. If $K\in D_{\leq w}$, its piece
$\mathcal H^b(K)[-b]$ is sent to a complex of weights at most $w$:
the sheaf has weights at most $w+b$, and the shift subtracts $b$
by [proposition-weights-under-usual-operations]. Applying $Rg_!$ to
the truncation triangles and using [lemma-weights-exact-sequence]
on their cohomology proves the result by induction. Lean packages
this argument in
`AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.map_of_forall_toComplex`.

For a quasi-finite $g$, [lemma-finite-quasi-finite-direct-images--1]
supplies the hypothesis: in degree zero the bound is $v$, and in
positive degrees the sheaf is zero. This is exactly
`AlgebraicGeometry.HasDirectImageWeightBound.of_locallyQuasiFinite`.
