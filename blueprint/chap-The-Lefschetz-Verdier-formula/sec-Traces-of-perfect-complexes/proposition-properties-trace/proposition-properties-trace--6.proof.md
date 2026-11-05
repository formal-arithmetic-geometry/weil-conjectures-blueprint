+++
kind = "proof"
of = "proposition-properties-trace--6"
order = 895013
uses = ["definition-categorical-trace", "proposition-properties-trace--1", "proposition-properties-trace--2", "proposition-properties-trace--3", "proposition-properties-trace--4", "lemma-perfect-complexes-geometric-point--3"]
+++
Write $P$ as a finite sum of shifted units, with inclusions $i_j$ and
projections $p_j$. Since $\sum_j i_jp_j=1$, additivity
[proposition-properties-trace--1] and cyclicity express the trace of
$v$ as the sum of the traces of $p_jvi_j$; this is
`CategoryTheory.ShiftDecomposition.trace_eq_sum`. Apply the same
argument after each cohomology functor, using
`CategoryTheory.traceOrZero_eq_sum`.

An endomorphism of $\mathbf 1[n]$ is $r[0][n]$ for an endomorphism $r$
of the unit of $\mathcal A$, by full faithfulness of placement in
degree zero and of shifting. Represent this object by the unit in
degree $-n$. Conjugacy [proposition-properties-trace--2] and the
termwise computation [proposition-properties-trace--4] give trace
$(-1)^n\iota(r)$, as in
`DerivedCategory.trace_shiftFunctor_map_singleFunctor_map`. Its
cohomology is the unit in degree $-n$ and zero elsewhere, so its
cohomological supertrace is $(-1)^n r$. Sum these equalities over the
finitely many summands and interchange the finite sums.

At the geometric point, the field-coefficient comparison of
[lemma-perfect-complexes-geometric-point--3] is implemented by a fibre
functor to the derived category of vector spaces. Splitting bounded
complexes there supplies the finite decomposition into shifted units
(`AlgebraicGeometry.ProEtale.CondensedRing.nonempty_shiftDecomposition_point`),
and the cohomology sheaves are finite free
(`AlgebraicGeometry.ProEtale.CondensedRing.isFiniteFree_upperStar_homology`).
Apply the first formula in the ambient derived category. The faithful
monoidal inclusion of $\Dbc$ preserves trace by
[proposition-properties-trace--3] and identifies placement in degree
zero with
`AlgebraicGeometry.ProEtale.CondensedRing.homologyUnitEndRingHom`.
Its injectivity on endomorphisms of the unit gives the required equality
in $\Dbc$.
