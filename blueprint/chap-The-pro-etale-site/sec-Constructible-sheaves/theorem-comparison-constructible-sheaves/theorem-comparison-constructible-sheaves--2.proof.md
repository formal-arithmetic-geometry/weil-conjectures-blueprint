+++
kind = "proof"
of = "theorem-comparison-constructible-sheaves--2"
order = 149006
uses = ["theorem-comparison-constructible-sheaves--1", "proposition-comparison-morphism-inverse-image", "proposition-locally-constant-sheaves-finite-presentation", "proposition-comparison-immersions", "theorem-classical-sheaves-essential-image", "corollary-bounded-below-classical-complexes"]
+++
The module comparison criterion supplies full faithfulness of $\nu_X^*$,
an étale antecedent for every classical module, and the test that an
étale module $G$ is constructible if and only if $\nu_X^*G$ is
constructible. In Lean, the first two assertions are obtained by placing
modules in degree zero and applying bounded classical descent
[corollary-bounded-below-classical-complexes]. Exactness identifies
degree-zero cohomology after comparison with inverse image on modules.
The constructibility test uses compatibility with stratum pullbacks
[proposition-comparison-immersions] and comparison for finitely presented
local systems [proposition-locally-constant-sheaves-finite-presentation];
Noetherianity identifies finite generation with finite presentation.

This test restricts $\nu_X^*$ to the two constructible full subcategories,
and ambient full faithfulness restricts with it. For a constructible
pro-étale module $F$, [theorem-comparison-constructible-sheaves--1] makes
$F$ classical. Choose an étale antecedent $G$ with $\nu_X^*G\simeq F$.
Constructibility is invariant under isomorphism, so the same test shows
that $G$ is constructible. This proves essential surjectivity. The
equivalence is formed from this restricted functor itself, which gives
the required identification of its forward functor.
