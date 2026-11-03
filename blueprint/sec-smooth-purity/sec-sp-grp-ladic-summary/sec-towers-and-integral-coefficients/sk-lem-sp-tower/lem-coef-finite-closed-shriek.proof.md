+++
kind  = "proof"
of    = "lem-coef-finite-closed-shriek"
+++
Let $j$ be the open complement. Tensor the triangle of
[lem-exc-closed-support-triangle] by $B$:

$$
(i_*Ri_A^!M)\otimes_A^LB\longrightarrow M_B
\longrightarrow(Rj_{*,A}j^*M)\otimes_A^LB\longrightarrow.
$$

Closed direct image is exact, commutes with sums, and is extension
by zero on stalks; hence it commutes with derived tensor by the
constant coefficient complex. Open restriction also commutes
with that tensor. The third term is
$Rj_{*,B}j^*(M_B)$ by [lem-coef-finite-direct-image].
The resulting triangle is therefore the closed-support triangle
for $M_B$. Its map on the first term is obtained from the
displayed exceptional counit, so it is $i_*b_{i,M}$.
The full faithfulness of $i_*$, as in
[def-weil-open-closed-recollement], shows that $b_{i,M}$
is an isomorphism.

All the finite-Tor domains used here are justified: the previously
proved finite boundary exchange
[cor-weil-boundary-duality-discharge] and finite biduality
[thm-fix-general-biduality] identify
$Ri_A^!M\cong D_Zi^*D_XM$, so it is finite-Tor constructible.
The assertion on the $B$-side is the same finite theorem.
This use of finite biduality introduces no integral-duality input.
For composition or successive coefficient changes, transpose
both composites to the same composite of exceptional counits.
Their equality proves the required coherence. Open exceptional
inverse image is ordinary restriction, whose coefficient
comparison is reassociation of tensor product. Factoring a
locally closed immersion proves its version with the same
evaluation and counit compatibilities.
