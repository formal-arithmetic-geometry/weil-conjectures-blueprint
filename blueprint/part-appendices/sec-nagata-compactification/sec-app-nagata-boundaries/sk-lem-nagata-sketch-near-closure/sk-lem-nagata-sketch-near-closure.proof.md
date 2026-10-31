+++
kind = "proof"
of = "sk-lem-nagata-sketch-near-closure"
uses = ["sk-lem-nagata-sketch-boundary", "sk-lem-nagata-sketch-elimination", "sk-lem-nagata-sketch-blowups"]
+++
Inside $V$, the set $F$ is disjoint from the closed complement of the
largest open over which $q$ is an isomorphism. Since $V$ is spectral, both
closed subsets can be enlarged to disjoint constructible closed
subsets, and we apply Lemma [sk-lem-nagata-sketch-boundary] so that their closures
in $T$ become disjoint. On the complement $T_0$ of the second closure,
the restriction of $q$ is an isomorphism over an open $V_0$ containing
$F$. We make this open schematically dense and then apply Theorem [sk-lem-nagata-sketch-elimination] on $T_0$. The
resulting strict transform is both open and proper over the modification,
and hence it is an isomorphism there.
The extension part of Lemma [sk-lem-nagata-sketch-blowups]
extends this blow-up from $T_0$ to a $V$-admissible blow-up of $T$,
which is an isomorphism over an open containing the closure of $F$. The precise argument, including
the choice of constructible enlargements, is [Stacks, Tag 0F3W](https://stacks.math.columbia.edu/tag/0F3W).
