+++
kind = "proof"
of = "lemma-bounding-weights-mixed-sheaf--1"
order = 1062002
uses = ["proposition-topos-functoriality", "lemma-filtrations-spectra", "proposition-weights-under-usual-operations"]
+++
Choose a mixed filtration
$$
0=G_0\hookrightarrow G_1\hookrightarrow\cdots\hookrightarrow G_n\simeq K
$$
whose successive quotients are pure of weights $v_i\le w$.
At a closed point $x$, the stalk functor is exact and its maps
commute with local Frobenius. Each quotient stalk has eigenvalues
of absolute value $q_x^{v_i/2}\le q_x^{w/2}$. Starting from the zero
stalk, induction along the filtration gives the same bound for
each $G_i$ and hence for $K$.

This is `AlgebraicGeometry.WeilSheaf.stalkAt_hasWeightsAtMost_of_filtration`.
At each step Lean uses `FrobeniusModule.HasWeightsAtMost.of_exact`:
an eigenvector in the middle term either has nonzero image in the
quotient, or lifts to an eigenvector in the subobject. This gives
the eigenvalue inclusion of Lemma [lemma-filtrations-spectra].
The final isomorphism $G_n\simeq K$ transports the bound to $K$.

For the converse, Lean rewrites mixedness using
`AlgebraicGeometry.WeilSheaf.isMixedOfWeightsAtMost_iff_filtrationClosure`
and inducts along a mixed filtration. Punctual upper bounds pass
to subobjects and quotients, since the corresponding stalk maps
are injective and surjective and commute with Frobenius. For a
pure quotient $Q$ of weight $v$, distinguish two cases. If $Q=0$,
it is pure of weight $w$ and contributes no restriction. Otherwise,
`AlgebraicGeometry.WeilSheaf.exists_nontrivial_stalk_of_not_isZero`
gives a closed point $x$ with $Q_{\bar x}\ne0$. This stalk is
finite dimensional over $\overline{\mathbf Q}_\ell$, so Frobenius
has an eigenvalue $\alpha$. Purity and the inherited upper bound give
$$
q_x^{v/2}=|\iota(\alpha)|\le q_x^{w/2}.
$$
Since $q_x>1$, we obtain $v\le w$. This comparison is
`AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.le_of_hasWeightsAtMost`.
Induction therefore gives a mixed filtration with all quotient
weights at most $w$.
