+++
kind = "proof"
of = "lemma-change-coefficients-internal-hom--1"
order = 642002
uses = ["proposition-topos-functoriality", "lemma-inverse-image-coefficient-sheaves", "proposition-six-operations-dctf", "proposition-inverting-ell", "proposition-dctf-x-qbar-2-colimit"]
+++
For (1), pull back the short exact sequence of condensed coefficient
modules to $X_{\mathrm{pro}\acute{e}t}$. Exactness of inverse image gives
$$
0\longrightarrow\mathcal O_{E,X}
\xrightarrow{\ell^n}\mathcal O_{E,X}
\longrightarrow(\mathcal O_E/\ell^n)_X\longrightarrow 0.
$$
Write $T$ for derived extension of scalars and $H$ for restriction of
scalars. The object $H(\mathcal O_E/\ell^n)_X$ is dualizable: the displayed
sequence resolves it by two copies of the tensor unit. The projection
formula identifies $HT(M)$ with
$M\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\ell^n)_X$.
Tensoring with a dualizable object commutes with internal Hom in its
second argument. Applying the adjunction $T\dashv H$ therefore identifies
the restriction of the comparison with an isomorphism. Since $H$
reflects isomorphisms, the comparison itself is an isomorphism. This is
the argument of `CategoryTheory.Mod.isIso_ihomComparison_leftDerivedExtendScalars`,
applied to the displayed short exact sequence.

For $E\to F$ in (2), choose a finite basis of $F$ over $E$.
Lemma [lemma-inverse-image-coefficient-sheaves](2) identifies $F_X$ with
a finite free $E_X$-module. Extension of scalars is exact, and its composite
with restriction of scalars is the finite direct sum indexed by this
basis, also on derived categories. Internal Hom commutes with these
finite sums in its second argument. The basis elements act as scalars,
and the resulting isomorphism is the one induced by evaluation.
Restriction of scalars reflects isomorphisms, so the internal Hom
comparison is invertible on the ambient derived categories. Restrict to
bounded constructible complexes, whose internal Hom is the ambient one
by Proposition [proposition-six-operations-dctf].

For $\mathcal O_E\to E$, Proposition [proposition-inverting-ell]
identifies extension of scalars on bounded constructible complexes with
rationalization. The tensor comparison is an isomorphism between the
left adjoints in the tensor--Hom adjunctions. Its mate is an isomorphism
after rationalization, by
`CategoryTheory.Rationalization.isIso_mateEquiv_of_isLocalization`;
this mate is precisely the internal Hom comparison.

For $E\to\overline{\mathbf Q}_\ell$, use the filtered $2$-colimit of
Proposition [proposition-dctf-x-qbar-2-colimit]. Its transition functors
are monoidal and commute with internal Hom by the finite-extension case,
and the structure isomorphisms are monoidal. The internal Hom comparison
for the functor into the colimit is consequently an isomorphism, by
`CategoryTheory.CategoryCocone.isIso_ihomComparison_Φ`.
Finally, the comparison for
$\mathcal O_E\to E\to\overline{\mathbf Q}_\ell$ is the composite of the
two comparisons, so it too is an isomorphism.
