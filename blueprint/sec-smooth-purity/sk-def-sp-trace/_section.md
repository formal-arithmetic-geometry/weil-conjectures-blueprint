+++
id = "sk-def-sp-trace"
kind = "definition"
title = "Smooth trace"
order = 1837
uses = ["sk-thm-smooth-purity", "sk-thm-purity-transport"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$, and let $\Lambda$ be
any admissible coefficient ring. We omit $\Lambda$ from the notation and let
$\varepsilon_f(K):Rf_!f^!K\to K$ be the counit of the adjunction
$Rf_!\dashv f^!$, restricted to $\Dctf(X,\Lambda)$ and $\Dctf(Y,\Lambda)$; it is a
morphism in $\Dctf(Y,\Lambda)$. For $K\in\Dctf(Y,\Lambda)$, the *smooth trace*
is the composite in $\Dctf(Y,\Lambda)$

$$
\operatorname{Tr}_{f}(K):\quad
Rf_!\bigl(f^{*}K(d)[2d]\bigr)
\xrightarrow{\ Rf_!\gamma_{f}(K)\ }Rf_!f^!K
\xrightarrow{\ \varepsilon_{f}(K)\ }K,
$$

where $\gamma_f$ is the purity isomorphism.
