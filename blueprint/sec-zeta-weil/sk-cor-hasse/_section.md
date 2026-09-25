+++
id = "sk-cor-hasse"
kind = "section"
title = "Hasse–Weil bound"
order = 3133
uses = ["sk-thm-rh", "sk-thm-trace-transport"]
+++
*Corollary (sketch).*

With the hypotheses of [sk-thm-rh],

$$
\bigl|N_1(X_0)-q^{d}\bigr|\;\le\;\sum_{i=1}^{2d-1}b_i\,q^{i/2},
\qquad b_i=\deg P_i .
$$

For a smooth projective curve $X_0/\Fq$ of genus $g$ this reads
$|N_1-(q+1)|\le2g\sqrt q$.

## Proof

By [sk-thm-trace-transport] (a),
$N_1=\sum_{i=0}^{2d}(-1)^{i}\Tr(F_{i,\ell})$. The endpoint terms contribute
$q^{d}$ for $i=2d$ and $1$ for $i=0$ (see [sk-thm-betti]), and each of the
remaining $b_i$ eigenvalues of $F_{i,\ell}$ has absolute value $q^{i/2}$ by
[sk-thm-rh]; the triangle inequality gives the stated bound. For a curve
$d=1$, $b_0=b_2=1$ and $b_1=2g$, so
$|N_1-(q+1)|\le2g\sqrt q$.

Uses: [sk-thm-rh], [sk-thm-trace-transport]
