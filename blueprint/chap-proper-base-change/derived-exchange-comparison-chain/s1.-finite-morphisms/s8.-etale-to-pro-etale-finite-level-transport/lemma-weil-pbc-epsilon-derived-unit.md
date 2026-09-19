+++
id = "lemma-weil-pbc-epsilon-derived-unit"
kind = "lemma"
title = "Derived comparison for the epsilon unit"
order = 817
uses = ["lemma-weil-pbc-epsilon-injective-acyclicity", "lemma-weil-pbc-epsilon-inverse-image-exact", "lemma-weil-pbc-epsilon-unit-isomorphism"]
+++
For $L\in D^+(X_{\mathrm{et}},A)$, the derived unit

$$
L\longrightarrow R\epsilon_{X,*}\epsilon_X^{-1}L
$$

is an isomorphism, naturally in $L$.

## Proof

Choose a bounded-below injective resolution $L\to I^\bullet$. Exactness of
$\epsilon_X^{-1}$ represents the inverse image by
$\epsilon_X^{-1}I^\bullet$. Lemma
[lemma-weil-pbc-epsilon-injective-acyclicity] makes every term
$\epsilon_{X,*}$-acyclic. The bounded-below acyclic-resolution lemma then
computes the derived direct image termwise:

$$
R\epsilon_{X,*}\epsilon_X^{-1}L
\simeq\epsilon_{X,*}\epsilon_X^{-1}I^\bullet.
$$

The unit isomorphism identifies the last complex with $I^\bullet$, including
its differentials. A morphism of bounded-below complexes lifts to the chosen
injective resolutions, and two lifts are homotopic; termwise naturality of the
unit makes the resulting derived isomorphism independent of the lift.
