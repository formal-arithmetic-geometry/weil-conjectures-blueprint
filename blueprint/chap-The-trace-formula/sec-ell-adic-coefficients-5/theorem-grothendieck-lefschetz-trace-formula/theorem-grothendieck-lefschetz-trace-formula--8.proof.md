+++
kind = "proof"
of = "theorem-grothendieck-lefschetz-trace-formula--8"
order = 1017017
uses = ["theorem-grothendieck-lefschetz-trace-formula--4", "theorem-grothendieck-lefschetz-trace-formula--5", "theorem-grothendieck-lefschetz-trace-formula--6", "theorem-grothendieck-lefschetz-trace-formula--9", "definition-trace-function"]
+++
Write $m=n+1$ and choose the Weil object $K'$ and additive map $\iota$ of [theorem-grothendieck-lefschetz-trace-formula--9]. Apply [theorem-grothendieck-lefschetz-trace-formula--4] with $e=1$, and then apply $\iota$. The global comparison identifies the left side with the alternating Frobenius trace on $H_c^i(X,K)$, and additivity moves $\iota$ through the finite sum on the right.

The bijection `AlgebraicGeometry.ProEtale.CondensedRing.fieldPointsEquivFrobeniusFixedPointsRefl` identifies the points fixed by $\sigma^m$ with $X_0(\mathbf F_{q^m})$. Under this bijection the local comparison identifies each summand with $t_{K,m}(y)$. This is the proof of `AlgebraicGeometry.WeilComplex.finsum_trace_compactlySupportedCohomology_eq_of_comparison`; the tagged theorem is its wrapper.

Expand the trace function as in [definition-trace-function]. The finiteness in [theorem-grothendieck-lefschetz-trace-formula--5] and [theorem-grothendieck-lefschetz-trace-formula--6] makes the degree sums finite; `AlgebraicGeometry.WeilComplex.traceFunction_eq_sum` gives the finite local sum explicitly. Finite type over a finite field makes the set of rational points finite.
