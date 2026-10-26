+++
id = "lem-wf-rank-one-component-modulus"
kind = "lemma"
title = "A rank-one character has constant modulus on a degree component"
lean = ["AlgebraicGeometry.Monodromy.DegreeDatum.norm_apply_eq_zpow"]
order = 3835
uses = ["def-wf-degree-components", "lem-wf-rank-one-algebraic-extension"]
+++
Let $A,c,j_\chi$ be as in
[lem-wf-rank-one-algebraic-extension], and fix an embedding
$\iota:E\hookrightarrow\mathbf C$. If
$z\in G_{\mathrm{arith}}(\chi)^{[m]}$, then

$$
|\iota(j_\chi(z))|=|\iota(c)|^m.
$$
