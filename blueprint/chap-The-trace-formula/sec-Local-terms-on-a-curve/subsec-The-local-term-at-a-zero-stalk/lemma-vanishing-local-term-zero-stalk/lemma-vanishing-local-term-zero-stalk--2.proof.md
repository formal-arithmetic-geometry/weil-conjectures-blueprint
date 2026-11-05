+++
kind = "proof"
of = "lemma-vanishing-local-term-zero-stalk--2"
order = 989004
uses = ["lemma-vanishing-local-term-zero-stalk--1", "lemma-local-term-restriction-map", "lemma-frobenius-fixed-scheme"]
+++
Let $z:\operatorname{Spec}k\to F$ be the point determined by $y$.
Lemma [lemma-vanishing-local-term-zero-stalk--1] gives
$z^*\rho_{K\boxtimes\mathbb D_XK}=0$.
By Lemma [lemma-frobenius-fixed-scheme], $F$ is a finite disjoint union
of reduced points. Hence $B\simeq\operatorname{Spec}k$, and the
restriction of $\rho_{K\boxtimes\mathbb D_XK}$ to $B$ is zero.
Lemma [lemma-local-term-restriction-map] writes the local term as the
integral of the composite of the supported class, this restriction,
and evaluation. This composite is zero. Lean packages this implication
as
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_frobeniusGraph_eq_zero_of_supportedRestriction`.
