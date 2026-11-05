+++
kind = "proof"
of = "theorem-comparison-over-henselian-pair-degree--1"
order = 328002
uses = ["lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "lemma-finite-morphisms"]
+++
First consider abelian sheaves. If a section restricts to zero on $Z_0$,
its vanishing locus is an open neighbourhood of $Z_0$. Every nonempty
closed subset of $Z$ meets $Z_0$: its image in $\operatorname{Spec}R$ is
closed and contains a maximal ideal, which contains $J$. The vanishing
locus is therefore all of $Z$. Applying this to the difference of two
sections proves injectivity.

Let $t\in\Gamma(Z_0,i^*F)$. Étale locally it is the restriction of sections
of $F$. Quasi-compactness gives finitely many such representatives covering
$Z_0$. Their disjoint union, together with $Z\setminus Z_0$ carrying the
zero section, gives a surjective étale morphism $U\to Z$ and a section
whose restriction agrees with $t$. Choose a finite surjection $r:Z'\to Z$
which factors through $U$ Zariski locally on $Z'$. The representatives
then give sections of $r^*F$ on finitely many quasi-compact opens covering
the closed fibre $Z'_0$, with equal germs along $Z'_0$.

The scheme $Z'$ is proper over $R$, and every irreducible closed subset
of $Z'$ meets $Z'_0$ in a nonempty connected subset. Spectral shrinking
replaces the opens by smaller opens which cover $Z'$, still contain their
original intersections with $Z'_0$, and on whose overlaps the sections
agree. The sheaf condition gives a global section $s'$ of $r^*F$ which
restricts to the pullback of $t$.

The two pullbacks of $s'$ to $Z'\times_ZZ'$ agree on its closed fibre.
This scheme is again proper over $R$, so injectivity gives their equality.
Sections of abelian étale sheaves descend along finite surjections; this
follows from the finite-morphism stalk formula in [lemma-finite-morphisms]
and étale gluing. Thus $s'$ descends to a section $s$ of $F$. Since
$Z'_0\to Z_0$ is surjective, equality after this pullback shows that
$s$ restricts to $t$.

For the connectedness assertion, apply Stein factorization to an
irreducible closed subset with its reduced induced structure. Its ring
of global sections is integral over $R$. Henselian idempotent lifting
makes the closed fibre of this affine factor connected, and the proper
map to the affine factor has connected fibres. This gives the required
connectedness on the original closed subset. In the construction of the
Stein factorization over an arbitrary affine base, proper Noetherian
approximation uses Chow's lemma [theorem-chow-s-lemma-projective-form]
and schematic images [lemma-schematic-closure-uniqueness].

Evaluation at the terminal étale scheme identifies the bijection just
proved with the displayed map on global sections. For module sheaves,
inverse image commutes with forgetting to abelian sheaves, and this
forgetful functor reflects isomorphisms. Finally, naturality follows from
naturality of the unit $F\to i_*i^*F$ and of the identifications of global
sections with sections over the terminal objects.
