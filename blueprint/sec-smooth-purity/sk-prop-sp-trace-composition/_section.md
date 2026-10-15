+++
id = "sk-prop-sp-trace-composition"
kind = "proposition"
title = "Transitivity of the smooth trace"
order = 1838
uses = ["sk-def-sp-trace", "sk-prop-sp-composition"]
tags = ["sketch"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{g}Z$ be smooth of pure relative dimensions $d$
and $e$, and $K\in\Dctf(Z,\Lambda)$ for any admissible $\Lambda$. Then
$\operatorname{Tr}_{g\circ f}(K)$ (see [sk-def-sp-trace]) is the composite in
$\Dctf(Z,\Lambda)$

$$
\begin{gathered}
R(g\circ f)_!\bigl((g\circ f)^{*}K(d+e)[2d+2e]\bigr)
\simeq Rg_!Rf_!\bigl(f^{*}(g^{*}K(e)[2e])(d)[2d]\bigr)\\
\xrightarrow{\ Rg_!(\operatorname{Tr}_{f}(g^{*}K(e)[2e]))\ }
Rg_!\bigl(g^{*}K(e)[2e]\bigr)
\xrightarrow{\ \operatorname{Tr}_{g}(K)\ }K.
\end{gathered}
$$
