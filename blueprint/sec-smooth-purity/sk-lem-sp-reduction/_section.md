+++
id = "sk-lem-sp-reduction"
kind = "lemma"
title = "Coefficient comparison"
order = 1832
uses = ["sk-def-sp-scalar-extension", "sk-lem-sp-finite-existence", "sk-lem-sf-flat-model", "sk-def-sfb-coefficient-comparisons", "sk-prop-geo-p1-adjunction"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$, and let $A\to B$ be a
map of finite commutative rings, each killed by a power of $\ell$; subscripts
$B$ denote extension of coefficients as in [sk-def-sp-scalar-extension]. For
$M\in\Dctf(X_{\mathrm{proét}},A)$ and $K\in\Dctf(Y_{\mathrm{proét}},A)$ there are
isomorphisms, natural in $M$ and $K$,

$$
\begin{aligned}
b(M)&:(Rf_{!,A}M)_B\xrightarrow{\ \sim\ } Rf_{!,B}(M_B)
&&\text{in }\Dctf(Y_{\mathrm{proét}},B),\\
c_{A,B}(K)&:(f_A^!K)_B\xrightarrow{\ \sim\ }f_B^!(K_B)
&&\text{in }\Dctf(X_{\mathrm{proét}},B).
\end{aligned}
$$

The map $c_{A,B}(K)$ is determined by the counit identity

$$
\varepsilon_B(K_B)\circ Rf_{!,B}\bigl(c_{A,B}(K)\bigr)
=(\varepsilon_A(K))_B\circ b(f_A^!K)^{-1},
$$

where $\varepsilon_A:Rf_{!,A}f_A^!\to\mathrm{id}$, a natural transformation of
endofunctors of $\Dctf(Y_{\mathrm{proét}},A)$, and $\varepsilon_B$ are the
counits of [sk-lem-sp-finite-existence].

