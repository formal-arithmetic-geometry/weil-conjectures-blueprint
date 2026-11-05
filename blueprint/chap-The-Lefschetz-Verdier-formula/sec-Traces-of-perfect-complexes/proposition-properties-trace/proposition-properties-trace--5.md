+++
id = "proposition-properties-trace--5"
kind = "proposition"
title = "Additivity along long exact sequences"
order = 895006
aliases = ["bp-r270-5"]
lean = ["CategoryTheory.superTrace_eq_add_of_exact"]
uses = ["definition-categorical-trace"]
+++
The filtered-complex statement over an arbitrary ring is bypassed by the
Lean route; its additivity argument uses the following long exact sequence
statement.

Let $\mathcal C$ be an abelian braided monoidal category with finite
biproducts and tensor product additive in each variable. Assume
$\End(\mathbf 1)$ is nonzero and every nonzero endomorphism of
$\mathbf 1$ is invertible. Consider a long exact sequence

$$
\cdots\longrightarrow A^j\longrightarrow B^j\longrightarrow D^j
\longrightarrow A^{j+1}\longrightarrow\cdots
$$

whose objects are finite direct sums of $\mathbf 1$, and are zero outside
a common finite interval of degrees. If endomorphisms $\varphi_A^j$,
$\varphi_B^j$, $\varphi_D^j$ commute with all the maps, including the
connecting maps, then

$$
\sum_j(-1)^j\operatorname{tr}(\varphi_B^j\mid B^j)
=\sum_j(-1)^j\operatorname{tr}(\varphi_A^j\mid A^j)
+\sum_j(-1)^j\operatorname{tr}(\varphi_D^j\mid D^j).
$$
