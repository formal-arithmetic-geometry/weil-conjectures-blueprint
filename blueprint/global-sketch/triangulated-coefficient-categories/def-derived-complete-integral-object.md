+++
id = "def-derived-complete-integral-object"
kind = "definition"
title = "Derived-complete integral object"
order = 12
uses = ["def-finite-reduction", "def-strict-reduction-tower", "def-weil-finite-coefficient-datum"]
+++
For a scheme $Y$, fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
An object
$K\in D(Y_{\mathrm{proet}},\widehat{\mathcal O}_{E,Y})$ is
*derived complete* if
the canonical map

$$
K\longrightarrow R\varprojlim_n
\operatorname{Res}_{Y,n}\operatorname{red}_{Y,n}(K)
$$

is an isomorphism, where the reductions are represented by a strict tower as
in Definition [def-strict-reduction-tower].
