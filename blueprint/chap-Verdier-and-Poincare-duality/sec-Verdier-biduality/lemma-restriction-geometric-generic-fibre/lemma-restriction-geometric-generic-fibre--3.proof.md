+++
kind = "proof"
of = "lemma-restriction-geometric-generic-fibre--3"
order = 838006
uses = ["lemma-restriction-geometric-generic-fibre--1", "lemma-flat-models-generators", "lemma-sections-support-closed-subscheme", "theorem-proper-base-change-classical-pro", "corollary-open-direct-image-over-field", "proposition-six-operations-dctf--1"]
+++
Use noetherian induction on the closed subsets of $X$; the empty case is
immediate. The flat model of [lemma-flat-models-generators] has only
finitely many nonzero terms. On a dense open $j:V\hookrightarrow X$
these terms are locally constant and flat, so $j^*K$ has a left dual
$D\in\Dctf(V,A)$. In Lean this is
`AlgebraicGeometry.Etale.exists_dense_open_exactPairing`. Let
$i:W\hookrightarrow X$ be the closed complement.

Dévissage is in the second variable. Apply internal Hom and pullback to
the localization triangle with closed support
([lemma-sections-support-closed-subscheme])

$$
i_*i^!M\longrightarrow M\longrightarrow Rj_*j^*M\longrightarrow.
$$

For the open term, put $N=j^*M$. Internal adjunction gives

$$
\cHom_X(K,Rj_*N)\simeq Rj_*\cHom_V(j^*K,N),
\qquad
\cHom_V(j^*K,N)\simeq D\otimes^{\mathbf L}N.
$$

The latter complex is bounded constructible, because $D$ has finite Tor
amplitude. Apply [lemma-restriction-geometric-generic-fibre--1] to both
$N$ and $D\otimes^{\mathbf L}N$. Both sides of the comparison are then
direct images from $V_S$, so the fully faithful functor $Rj_{S,*}$ lets
us check the comparison after $j_S^*$. Compatibility of the comparison
with composition reduces it to the comparison for the dualizable
complex $j^*K$, which is an isomorphism since pullback preserves tensor
products and duals.

For the closed term, proper base change
([theorem-proper-base-change-classical-pro]) and the same internal
adjunction express both sides as direct images from $W_S$. After
$i_S^*$, the comparison is the one for $(i^*K,i^!M)$ on $W$.
Pullback preserves constructibility and finite Tor amplitude
([proposition-six-operations-dctf--1]). Also $i^!M$ is bounded
constructible: the localization triangle, finiteness of $Rj_*$
([corollary-open-direct-image-over-field]), and $i^*i_*\simeq\mathrm{id}$
give this. The induction hypothesis therefore applies to $W$.

Finally, naturality compares the first two arrows of the resulting
distinguished triangles. The first term vanishes after $j_S^*$, while
the third is an $Rj_{S,*}$-image. Thus every map from the shift of the
first term to the third is zero. The triangulated-category lemma
`CategoryTheory.Pretriangulated.isIso₂_of_isIso₁₃_of_subsingleton`
then makes the middle comparison an isomorphism. This is the gluing step
`AlgebraicGeometry.Etale.isIso_derivedHomUpperStarComparison_of_isIso_open_closed`.
