+++
id = "def-weil-rational-coefficients"
kind = "definition"
title = "Intrinsic rational coefficient category"
order = 14
uses = ["def-completed-integral-coefficient-sheaf", "def-weil-finite-coefficient-datum"]
+++
For a scheme $Y$, fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
The rational coefficient ring sheaf and bounded constructible category are
defined intrinsically by

$$
E_Y:=\widehat{\mathcal O}_{E,Y}[1/\varpi_E],
\qquad
D^b_c(Y,E)\subset D(Y_{\mathrm{proet}},E_Y).
$$

The right-hand side is the full subcategory of complexes with bounded
cohomology whose cohomology sheaves are constructible $E_Y$-modules:
after a finite constructible stratification they are locally constant with
finite-dimensional $E$-vector-space stalks. For $E=\Ql$, the integral
ring and uniformizer are $\Zl$ and $\ell$.

If $E\subset L$ is a finite extension, scalar extension is the exact
triangulated functor

$$
-\otimes^L_{E_Y}L_Y:D^b_c(Y,E)\longrightarrow D^b_c(Y,L),
\qquad L_Y=\widehat{\mathcal O}_{L,Y}[1/\varpi_L].
$$
