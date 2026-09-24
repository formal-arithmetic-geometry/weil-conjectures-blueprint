+++
id = "lemma-weil-pbc-epsilon-unit-isomorphism"
kind = "lemma"
title = "The comparison unit is an isomorphism"
order = 1910
uses = ["def-weil-pbc-epsilon-comparison", "def-weil-pbc-epsilon-unit-counit"]
+++
For every $A$-module sheaf $F$ on $X_{\mathrm{et}}$, the unit

$$
\eta^X_F:F\longrightarrow\epsilon_{X,*}\epsilon_X^{-1}F
$$

is an isomorphism.

## Proof

Evaluate at an etale object $U\to X$. Restriction of the left-Kan-extension
presheaf in Definition [def-weil-pbc-epsilon-comparison] back to
$\iota_XU$ has the identity factorization
$\iota_XU\to\iota_XU$. Refining any other factorization by its fiber product
with $U$ shows that the associated sheaf value is $F(U)$. Under this
identification, the formula in Definition
[def-weil-pbc-epsilon-unit-counit] sends $s$ to the same section $s$.
Thus every component of $\eta^X_F$ is the identity. Etale objects detect
maps of etale sheaves, so the unit is an isomorphism.
