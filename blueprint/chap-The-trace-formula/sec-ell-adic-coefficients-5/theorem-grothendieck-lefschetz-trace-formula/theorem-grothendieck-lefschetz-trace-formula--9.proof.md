+++
kind = "proof"
of = "theorem-grothendieck-lefschetz-trace-formula--9"
order = 1017019
uses = ["proposition-properties-trace", "theorem-grothendieck-lefschetz-trace-formula--5", "theorem-grothendieck-lefschetz-trace-formula--6"]
+++
First use `AlgebraicGeometry.WeilSheaf.exists_hasWeilObjectComparison` to choose a single additive map $\iota$ which works for all Weil sheaves in degree zero. Its proof reduces by Noetherian induction and filtrations to irreducible lisse Weil sheaves on smooth strata. Such a sheaf is a constant twist of a sheaf pulled back from the stratum over $\Fq$; the twisting scalar becomes the automorphism of the corresponding Weil object. Comparison of stalks and compactly supported cohomology gives both trace identities.

Next apply `AlgebraicGeometry.WeilComplex.hasWeilObjectComparison_of_toComplex`. Both traces are additive in distinguished triangles and change sign under a shift. Induction on the cohomological amplitude, using truncation triangles, therefore extends the comparison from sheaves to bounded complexes. Extract the resulting $K'$ and its two trace identities.
