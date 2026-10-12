+++
id = "lem-pc-universal-divisor"
kind = "lemma"
title = "The universal divisor"
order = 801
uses = ["def-pc-divisor-line-bundle", "def-pc-hilb-functor", "def-pc-relative-effective-cartier", "def-sc-effective-cartier-divisor", "lem-pc-cartier-criterion", "lem-pc-recd-pullback", "thm-pc-hilb-curves"]
+++
Let $X$ be as
in [thm-pc-hilb-curves] and let $d\geq0$. There is a relative
effective Cartier divisor

$$
D_{\mathrm{univ}}\subset \underline{\operatorname{Hilb}}^{d+1}_{X/k}\times_kX
$$

over $\underline{\operatorname{Hilb}}^{d+1}_{X/k}$ (a universal closed object, which is
an effective Cartier divisor via [lem-pc-cartier-criterion]), and
$\mathcal{O}(D_{\mathrm{univ}})$ is the associated invertible module; for a
$k$-rational point $[D]\in\underline{\operatorname{Hilb}}^{d+1}_{X/k}$ corresponding to
an effective Cartier divisor $D\subset X$ of degree $d+1$, the restriction
of $\mathcal{O}(D_{\mathrm{univ}})$ to the fibre $[D]\times X\cong X$ is
$\mathcal{O}_X(D)$.
