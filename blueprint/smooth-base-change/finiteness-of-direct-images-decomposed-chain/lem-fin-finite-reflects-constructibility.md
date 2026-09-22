+++
id = "lem-fin-finite-reflects-constructibility"
kind = "lemma"
title = "Finite direct image reflects constructibility"
order = 5163
lean = ["AlgebraicGeometry.Etale.isConstructible_of_isConstructible_pushforward"]
+++
Let $p:Z\to S$ be a finite morphism of Noetherian schemes, let $\Lambda$ be
a finite commutative ring, and let $F$ be an étale sheaf of
$\Lambda$-modules on $Z$. If its direct image $p_*F$ is constructible, then
$F$ is constructible.

## Proof

At a geometric point $\bar z$, with induced point $\bar s$ of $S$, the
counit has stalk
$$
(p^*p_*F)_{\bar z}=\prod_{\bar z'\in|Z_{\bar s}|}F_{\bar z'}\longrightarrow F_{\bar z},
$$
the projection of the finite stalk formula. It is surjective for modules,
hence the counit is surjective by conservativity of geometric stalks.

Pulling back a finite partition and its étale trivializations proves that
$p^*p_*F$ is constructible. Its kernel is constructible because
constructible sheaves on a Noetherian scheme are closed under subobjects;
now take its cokernel, using that constructible sheaves form a Serre
subcategory. No surjectivity of $p$ onto $S$ is required.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-direct-image, def:weil-pbc-constructible-complexes, lem:weil-pbc-finite-stalk-formula, lem:weil-pbc-geometric-stalk-conservative, lem:weil-pbc-constructible-subobjects-noetherian, lem:weil-pbc-constructible-serre
