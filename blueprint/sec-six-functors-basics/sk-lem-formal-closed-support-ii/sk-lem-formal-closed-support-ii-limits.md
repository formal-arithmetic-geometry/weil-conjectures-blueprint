+++
id = "det-formal-closed-support-ii-limits"
kind = "lemma"
title = "Closed support commutes with derived limits of sequences"
order = 2199
uses = ["sk-lem-formal-closed-support", "sk-prop-pe-products"]
+++
In the situation of [sk-lem-formal-closed-support], let $F$ be one of the functors

$$
j^*,\quad u^*,\quad i^*,\quad Rj_*,\quad R\underline\Gamma_Z=i^*\fib(\mathrm{id}\to Rj_*j^*),
\quad u^*R\underline\Gamma_Z,\quad L\otimes_{\Lambda_S}-,
$$

the last for a finite locally free $\Lambda_S$-module $L$. Then $F$ preserves products and fibers,
and for every tower $(K_n)_{n\ge0}$ in the source the natural map
$F(R\varprojlim_nK_n)\to R\varprojlim_nF(K_n)$ is an isomorphism.
