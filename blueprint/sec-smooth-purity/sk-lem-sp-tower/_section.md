+++
id = "sk-lem-sp-tower"
kind = "lemma"
title = "Integral complexes as normalized towers"
order = 2967
uses = ["sk-def-sp-coefficient-towers", "sk-def-sp-normalized-towers", "sk-def-pe-derived-completion", "sk-prop-pe-replete", "sk-prop-integral-criterion", "sk-prop-sp-integral-towers"]
tags = ["sketch"]
+++
Let $E/\Ql$ be finite and $T$ a scheme. The functor
$\operatorname{red}_TM=(M/\ell^n)_n$ from $D(T_{\mathrm{proét}},\mathcal O_E)$ to the
derived category $D(\operatorname{Tow}(T,\mathcal O_E))$ of towers
([sk-def-sp-coefficient-towers]) is left adjoint to

$$
R\varprojlim:D(\operatorname{Tow}(T,\mathcal O_E))\longrightarrow D(T_{\mathrm{proét}},\mathcal O_E),
$$

with unit the derived completion map $M\to R\varprojlim_nM/\ell^n$
([sk-def-pe-derived-completion]). This adjunction restricts to an equivalence
between $\Dbc(T,\mathcal O_E)$ and the normalized constructible towers
$\Dctf(T_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)_{\mathrm{norm}}$
([sk-def-sp-normalized-towers]).
