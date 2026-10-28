+++
id = "sk-prop-sp-composition"
kind = "proposition"
title = "Composition of purity"
order = 3372
uses = ["sk-thm-smooth-purity", "sk-prop-sp-orientation", "sk-prop-an", "sk-prop-sp-tower-geometric", "sk-lem-sp-reduction", "sk-thm-sf-comp-composition"]
tags = ["sketch"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{g}Z$ be smooth of pure relative dimensions $d$
and $e$. For every admissible $\Lambda$ and $K\in\Dctf(Z,\Lambda)$, the purity
map $\gamma_{g\circ f,\Lambda}(K)$ is the composite

$$
\begin{aligned}
(g\circ f)^{*}K(d+e)[2d+2e]
&\simeq f^{*}\bigl(g^{*}K(e)[2e]\bigr)(d)[2d]\\
&\xrightarrow{\ f^{*}(\gamma_g(K))(d)[2d]\ }f^{*}\bigl(g^!K\bigr)(d)[2d]\\
&\xrightarrow{\ \gamma_f(g^!K)\ }f^!g^!K\simeq(g\circ f)^!K
\end{aligned}
$$

in $\Dctf(X,\Lambda)$, where the coefficient $\Lambda$ is omitted from the
displayed composite, and $(g\circ f)^!\simeq f^!g^!$ is the identification
obtained by composing the adjunctions (compatibly with
$R(g\circ f)_!\simeq Rg_!Rf_!$), whose counit is the composite of the two counits.
