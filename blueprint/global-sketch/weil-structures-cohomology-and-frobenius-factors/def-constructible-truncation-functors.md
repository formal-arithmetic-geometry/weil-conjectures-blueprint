+++
id = "def-constructible-truncation-functors"
kind = "definition"
title = "Constructible truncation and cohomology functors"
order = 74
uses = ["def-constructible-truncation-candidates", "def-weil-finite-coefficient-datum", "prop-constructible-truncations"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$, a scheme $Y$, and
$\Lambda\in\{E,\Qlb\}$. By
Proposition [prop-constructible-truncations], the candidates of
Definition [def-constructible-truncation-candidates] are independent of
the common-stage representative. Define
$\tau^{\leq m},\tau^{\geq m}:D^b_c(Y,\Lambda)\to D^b_c(Y,\Lambda)$
for every $m\in\mathbf Z$ to be the descended functors, and for every
$i\in\mathbf Z$ define

$$
\mathcal H^i(K)=\bigl(\tau^{\geq i}\tau^{\leq i}K\bigr)[i]
\qquad\bigl(K\in D^b_c(Y,\Lambda)\bigr).
$$
