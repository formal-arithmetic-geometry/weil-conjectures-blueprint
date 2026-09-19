+++
id = "def-finite-reduction"
kind = "definition"
title = "Finite reduction"
order = 10
uses = ["def-completed-integral-coefficient-sheaf", "def-weil-finite-coefficient-datum"]
+++
For a scheme $Y$, fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
For $n\geq1$, restriction of scalars along

$$
\widehat{\mathcal O}_{E,Y}\twoheadrightarrow
(\mathcal O_E/\varpi_E^n)_Y
$$

is denoted $\operatorname{Res}_{Y,n}$. For
$K\in D(Y_{\mathrm{proet}},\widehat{\mathcal O}_{E,Y})$, its
$n$-th derived reduction is the explicitly typed object

$$
\operatorname{red}_{Y,n}(K):=
K\otimes^L_{\widehat{\mathcal O}_{E,Y}}
(\mathcal O_E/\varpi_E^n)_Y
\in D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr).
$$
