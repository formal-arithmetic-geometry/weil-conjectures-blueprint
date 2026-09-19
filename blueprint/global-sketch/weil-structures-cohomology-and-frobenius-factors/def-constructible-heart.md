+++
id = "def-constructible-heart"
kind = "definition"
title = "Constructible heart"
order = 76
uses = ["def-constructible-truncation-functors", "def-weil-finite-coefficient-datum", "prop-constructible-t-structure"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum] and a scheme $Y$.
For $\Lambda=E$ or $\Qlb$, define

$$
\begin{aligned}
D^{\leq0}_c(Y,\Lambda)&=
\{K:\tau^{\geq1}K=0\},\\
D^{\geq0}_c(Y,\Lambda)&=
\{K:\tau^{\leq-1}K=0\}.
\end{aligned}
$$

Using the bounded $t$-structure of
Proposition [prop-constructible-t-structure], define its constructible
heart by

$$
\Sh_c(Y,\Lambda)=D^{\leq0}_c(Y,\Lambda)
\cap D^{\geq0}_c(Y,\Lambda).
$$

Its objects are the constructible $\Lambda$-adic sheaves.
