+++
kind = "proof"
of = "lemma-extending-isomorphism-over-closure-closed"
order = 1453
uses = ["lemma-schematic-closure-uniqueness", "lemma-making-open-schematically-dense", "lemma-products-composites-u-admissible-blow", "lemma-separation-closures", "theorem-elimination-indeterminacy", "lemma-extending-isomorphism-over-closure-closed--1"]
+++
We separate the closure of $F$ from the closure of the locus where $q$
fails to be an isomorphism, and then apply elimination of
indeterminacy on the complement of the second closure.

Inside $V$, the set $F$ is disjoint from the closed complement of the
largest open over which $q$ is an isomorphism. Since $V$ is spectral, both
closed subsets can be enlarged to disjoint constructible closed subsets. To these we apply Lemma [lemma-separation-closures] so that their closures
in $T$ become disjoint. Then, on the complement $T_0$ of the second closure,
the restriction of $q$ is an isomorphism over an open $V_0$ containing
$F$. After making this open schematically dense, we apply
Theorem [theorem-elimination-indeterminacy] on $T_0$. The resulting strict transform is both open and proper over the
modification, and hence it is an isomorphism there.
By the extension part of Lemma [lemma-products-composites-u-admissible-blow],
this blow-up of $T_0$ extends to a $V$-admissible blow-up of $T$,
which is an isomorphism over an open containing the closure of $F$. We have only sketched the argument; the precise version, including the choice of constructible enlargements, is [Stacks, [0F3W](https://stacks.math.columbia.edu/tag/0F3W)].
