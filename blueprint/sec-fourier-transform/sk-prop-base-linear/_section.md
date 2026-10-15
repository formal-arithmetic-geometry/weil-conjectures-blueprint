+++
id = "sk-prop-base-linear"
kind = "proposition"
title = "P7: the transform is linear over the base"
order = 3048
lean = ["AlgebraicGeometry.Etale.nonempty_iso_fourierTransform_tensor"]
uses = ["sk-def-ft"]
tags = ["sketch"]
+++
Let $p:V\to S$ and $p':V^\vee\to S$ be the structure morphisms. For
$K\in\Dbc(V,E)$ and $N\in\Dbc(S,E)$,

$$
\FT_\psi\bigl(K\otimes^Lp^*N\bigr)\cong\FT_\psi(K)\otimes^L{p'}^*N .
$$

In particular, for $N$ from the base,
$\FT_\psi(p^*N)\cong\FT_\psi(\underline{E})\otimes^L{p'}^*N$, so the
transform of a base-changed sheaf is the base change of the transform of the
unit.
