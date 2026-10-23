+++
id = "det-tf-cone-zero-sections"
kind = "lemma"
title = "The two legs and the zero sections"
order = 3609
uses = ["det-tf-cone-leg-lifts", "pur9-def-normal-cone"]
+++
Let $c=(c_1,c_2):C\to X\times X$, let $Z\subset X$ have ideal $I$, and put
$J=c_1^\cdot I\,\mathcal O_C$, $L=c_2^\cdot I\,\mathcal O_C$ and $E=V(J)$. Assume $L\subset J$
and $L^n\subset J^{n+1}$ for some $n\geq1$, and let $\gamma_i:N_EC\to N_ZX$ be the maps of
normal cones induced by $c_i$ as in [det-tf-cone-leg-lifts]. Then:

1. **(1)** the inverse image under $\gamma_1$ of the zero-section ideal
$\operatorname{gr}^{>0}_I\mathcal O_X$ generates $\operatorname{gr}^{>0}_J\mathcal O_C$, so
$\gamma_1^{-1}(Z)=E$ scheme-theoretically;
2. **(2)** the inverse image under $\gamma_2$ of $\operatorname{gr}^{>0}_I\mathcal O_X$
generates an ideal whose $n$-th power is zero, so $\gamma_2^{-1}(Z)$ is a closed subscheme of
$N_EC$ with the same underlying space, and $(N_EC)_{\mathrm{red}}\to N_ZX$ factors through
$Z$.
