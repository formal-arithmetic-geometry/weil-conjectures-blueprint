+++
kind  = "proof"
of    = "lem-cbc-proetale-stalk-conservative"
+++
*Step 1 (clause (1)).* A morphism of complexes is an
isomorphism if and only if its cone is acyclic, and a complex is
acyclic if and only if all its cohomology sheaves vanish: this is the
definition of the derived category of
[def-weil-pbc-proetale-modules] as the localization at the
quasi-isomorphisms. Vanishing of a sheaf is a local condition for the
topology. Indeed, if $\mathcal H$ is a sheaf on $T_{\Proet}$ whose
inverse images along the members of a covering family vanish, then for
every object $V$ the sheaf axiom presents $\mathcal H(V)$ as the
equalizer of two maps between products of groups
$\mathcal H(V\times_TU_i)$ that are zero, the family being a
covering; hence $\mathcal H(V)=0$, and the converse is functoriality
of inverse image. Applying this to the cohomology sheaves of the cone
gives the equivalence of the first sentence.

*Step 2 (clause (2)).* This is
[lem-weil-pbc-ind-etale-basis]: restriction to the affine
ind-etale basis of [def-weil-pbc-ind-etale-basis] determines a
sheaf and its morphisms uniquely and detects isomorphisms of sheaves.
Restriction of a complex is exact and degreewise, so a morphism of
complexes is a quasi-isomorphism if and only if its restriction is
one. A general $T$ is covered by its affine opens, and clause (1)
reduces the statement to the affine case.

*Step 3 (clause (3)).* Let $\mathcal G'$ be a bounded-below
complex of etale $\Lambda$-sheaves. The etale neighbourhoods of a
geometric point $\bar t$ of $T$ are cofinal among its weakly etale
neighbourhoods, by [def-weil-pbc-proetale-site] and
[def-weil-pbc-site-comparison-morphism], the inverse image of the
comparison morphism being computed on the common objects; hence
$(\nu_T^*\mathcal G')_{\bar t}=\mathcal G'_{\bar t}$, naturally in
$\mathcal G'$. If $\nu_T^*F'\to\nu_T^*G'$ is an isomorphism at
every geometric point, then $F'\to G'$ is an isomorphism at every
geometric point, hence an isomorphism by
[lemma-weil-pbc-geometric-stalk-conservative]; applying the functor
$\nu_T^*$ exhibits $\nu_T^*F'\to\nu_T^*G'$ as an isomorphism. The
converse follows from functoriality. For bounded-below complexes one
applies this degreewise to the cohomology sheaves, inverse image being
exact and the identification of stalks being natural. The final
assertion of the clause is the definition: the bounded constructible
objects of [def-weil-pbc-proetale-modules] are by definition the
pullbacks of the bounded constructible etale objects. Full
faithfulness of $\nu_T^*$ on bounded-below complexes,
[thm-weil-pbc-site-comparison], is not needed for this argument,
but it shows that the etale model of a morphism of etale origin is
unique.

*Step 4 (clause (4)).* The replacement for the false general
statement is the displayed reference. Concretely, on
$T=\operatorname{Spec}k$ the single geometric point of $T$ is the
only point of the small pro-etale site that comes from a strictly
henselian local ring, while the site contains the affine objects
$U=\operatorname{Spec}(\operatorname{colim}\operatorname{Map}(E_n,k))$
for $E=\varprojlim E_n$ an inverse limit of finite sets with
surjective transition maps; such a $U$ is ind-Zariski, hence weakly
etale, over $k$ and has infinitely many points, so the sheaf
$\mathcal F$ of the statement has a nonzero value there while
$\mathcal F(T)=0$. No clause of this lemma asserts conservativity
of geometric-point stalks beyond clause (3), and clause (3) confines
the failure to complexes that are not of etale origin.
