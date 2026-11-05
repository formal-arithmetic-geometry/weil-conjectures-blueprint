+++
kind = "proof"
of = "lemma-weight-bounds-partitions--1"
order = 1352004
uses = ["proposition-weights-under-usual-operations", "proposition-extension-zero-restriction-closed-subscheme", "proposition-composition-base-change-rf-shriek", "lemma-weights-exact-sequence"]
+++
Fix $w$, $K$ and $q\geq0$. The restrictions $j^*K$ and $i^*K$ are
mixed of weights at most $w$ by
Proposition [proposition-weights-under-usual-operations]. Applying
$Rf_!$ to the localization triangle from
Proposition [proposition-extension-zero-restriction-closed-subscheme],
using the composition isomorphisms of
Proposition [proposition-composition-base-change-rf-shriek], and taking
cohomology gives an exact sequence of Weil sheaves with terms
isomorphic to

$$
R^q(fj)_!j^*K\longrightarrow R^qf_!K\longrightarrow R^q(fi)_!i^*K.
$$

This is
`AlgebraicGeometry.WeilSheaf.exists_exact_higherLowerShriek_of_openClosed`.
The hypotheses for $fj$ and $fi$ bound the outer terms by $w+q$.
Lemma [lemma-weights-exact-sequence] bounds the middle term, and
transport along the three isomorphisms gives the assertion.
