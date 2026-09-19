+++
id = "def-constructible-truncation-candidates"
kind = "definition"
title = "Common-stage truncation candidates"
order = 72
uses = ["def-qbar-coefficient-category", "def-weil-finite-coefficient-datum", "def-weil-rational-coefficients"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum] and a scheme $Y$.
For every $E'\in\mathcal E_\ell$ and every $m\in\mathbf Z$, take the
ordinary constructible truncation functors on $D^b_c(Y,E')$. If an object
of $D^b_c(Y,\Qlb)$ is represented by $(E',K_{E'})$, define its
representative-level candidates
to be

$$
(E',\tau^{\leq m}K_{E'}),\qquad
(E',\tau^{\geq m}K_{E'}).
$$

For every $i\in\mathbf Z$, the corresponding representative-level
cohomology candidate is

$$
\left(E',\bigl(\tau^{\geq i}\tau^{\leq i}K_{E'}\bigr)[i]\right).
$$
