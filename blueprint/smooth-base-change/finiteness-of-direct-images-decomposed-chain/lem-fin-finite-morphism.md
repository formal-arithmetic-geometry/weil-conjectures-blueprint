+++
id = "lem-fin-finite-morphism"
kind = "lemma"
title = "Finite direct images of constructible sheaves"
order = 5162
lean = ["AlgebraicGeometry.Etale.IsConstructible.pushforward_of_isFinite"]
uses = ["sbc-def-coefficient-conventions"]
+++
Let $f:X\to S$ be finite with $S$ of finite type over $k$, and let $F$ be a
constructible $\Lambda$-sheaf on $X_{\Et}$. Then the direct image $f_*F$ is
constructible on $S_{\Et}$ and $R^qf_*F=0$ for every $q>0$.

## Proof

Exactness and vanishing of positive direct images are the finite
direct-image exactness lemma of the proper-base-change chapter. Apply the
Noetherian finite-image theorem to the underlying finite constructible
abelian sheaf of $F$. It gives a finite partition on which $f_*F$ is finite
locally constant as an abelian sheaf.

On an étale trivialization with finite group fibre $M$, the action of each
$\lambda\in\Lambda$ is specified by its values on the finite set $M$. After
an étale refinement these finitely many values are constant; the addition
and module relations remain the given relations. Thus the trivialization is
one of constant $\Lambda$-modules. This is module constructibility. The
argument does not use an embedding into a finite constant pushforward.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image, lem:weil-pbc-finite-stalk-formula, lem:weil-pbc-finite-direct-image-exact, lem:weil-pbc-finite-pushforward-constructible-noetherian
