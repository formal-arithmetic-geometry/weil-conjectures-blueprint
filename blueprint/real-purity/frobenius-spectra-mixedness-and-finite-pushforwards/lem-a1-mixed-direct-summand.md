+++
id = "lem-a1-mixed-direct-summand"
kind = "lemma"
title = "Mixedness passes to direct summands"
order = 4171
uses = ["def-weil-frobenius-module-weights", "def-weil-punctual-weights"]
+++
A direct summand of an $\iota$-mixed constructible Weil sheaf is
$\iota$-mixed, and the same upper weight bound is preserved; the
analogous statement holds for Frobenius modules.

## Proof

Choose a Weil filtration as in the sheaf mixedness definition of
[def-weil-punctual-weights],
$0=\mathcal G_0\subset\cdots\subset\mathcal G_m=\mathcal G$ whose
nonzero quotients $\mathcal Q_i$ are punctually pure of weights
$u_i\le w$. For the direct summand inclusion
$\mathcal G'\hookrightarrow\mathcal G$, set
$\mathcal G'_i=\mathcal G'\cap\mathcal G_i$. Then
$\mathcal G'_i/\mathcal G'_{i-1}$ injects into
$\mathcal Q_i$. At every closed point, its Frobenius eigenvalues are
a submultiset of those of the pure module $\mathcal Q_{i,\bar y}$;
when nonzero they therefore all have modulus $q_y^{u_i/2}$. Deleting
zero quotients gives a Weil filtration of $\mathcal G'$ with weights
$\le w$. This proves the sheaf assertion without choosing unrelated
stalk filtrations. For Frobenius modules in the sense of
[def-weil-frobenius-module-weights], intersect a mixed filtration
with the stable summand and use the same triangular-matrix argument.
