+++
id = "lemma-weil-pbc-epsilon-geometric-morphism-construction-v1"
kind = "lemma"
title = "Construction of the comparison geometric morphism"
order = 1761
uses = ["def-weil-pbc-epsilon-comparison", "def-weil-pbc-epsilon-factorization-index-v1", "lemma-weil-pbc-epsilon-factorization-index-filtered-v1", "lemma-weil-pbc-etale-proetale-continuous", "lemma-weil-pbc-etale-proetale-left-exact"]
+++
Restriction along $\iota_X^{\mathrm{op}}$, pro-etale sheafification of left
Kan extension, and the displayed evaluation maps define an adjoint pair
$\epsilon_X^{-1}\dashv\epsilon_{X,*}$. The adjunction bijection is natural
in both variables, and $\epsilon_X^{-1}$ preserves finite limits.

## Proof

Continuity makes restriction of a pro-etale sheaf an etale sheaf. Presheaf
left Kan extension is left adjoint to presheaf restriction, and sheafification
is left adjoint to inclusion of sheaves. Composing these two adjunctions gives

$$
\operatorname{Hom}(\epsilon_X^{-1}F,G)
\cong\operatorname{Hom}(F,\epsilon_{X,*}G).
$$

The two universal properties make this bijection natural in $F$ and $G$ and
make its identity and composition equations automatic.

Before sheafification, evaluation at $W$ is
$\varinjlim_{I_W}F(U)$. The preceding lemma makes $I_W$ filtered, so this
colimit of $A$-modules commutes with finite limits. Sheafification of
$A$-module presheaves is left exact, and the left-exactness of $\iota_X$
identifies the transition diagrams for terminal objects and fibre products.
Thus $\epsilon_X^{-1}$ preserves finite limits. All maps used are induced by
the same restriction maps, so they are compatible with restriction in $W$ and
with morphisms of coefficient sheaves.
