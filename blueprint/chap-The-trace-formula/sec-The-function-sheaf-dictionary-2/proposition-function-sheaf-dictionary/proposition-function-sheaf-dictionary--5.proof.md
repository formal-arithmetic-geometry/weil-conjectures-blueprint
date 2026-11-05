+++
kind = "proof"
of = "proposition-function-sheaf-dictionary--5"
order = 1028011
uses = ["theorem-grothendieck-lefschetz-trace-formula", "proposition-function-sheaf-dictionary--3", "proposition-function-sheaf-dictionary--4"]
+++
The Lean form of [theorem-grothendieck-lefschetz-trace-formula] uses
`AlgebraicGeometry.WeilComplex.exists_weilBoundedConstructible_comparison`.
It gives a Weil object $K'$ for the identity automorphism of $X_0$ and an
additive map $\iota$ from categorical traces to $\Qbarl$, identifying both
its local traces with $t_{K,m}$ and its global traces with the alternating
Frobenius traces on $H_c^r(X,K)$. The comparison is extended from sheaves to
complexes by truncation triangles and trace additivity; open–closed
comparison uses [proposition-function-sheaf-dictionary--4].

Apply [proposition-function-sheaf-dictionary--3] to the structure morphism
of $X_0$. The base has a single Frobenius-fixed point, giving
`AlgebraicGeometry.ProEtale.CondensedRing.weilTraceFormula` for $K'$.
Apply $\iota$, move it through the finite sum, and identify Frobenius-fixed
points for the identity automorphism with $X_0(\mathbf F_{q^m})$. The local
and global comparison equalities give the formula, as in
`AlgebraicGeometry.WeilComplex.finsum_trace_compactlySupportedCohomology_eq_of_comparison`.
