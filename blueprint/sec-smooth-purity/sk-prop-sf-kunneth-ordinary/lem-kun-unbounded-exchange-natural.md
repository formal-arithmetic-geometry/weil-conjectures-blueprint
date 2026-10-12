+++
id = "lem-kun-unbounded-exchange-natural"
kind = "lemma"
title = "Naturality of the unbounded exchange morphism"
order = 2004
uses = ["def-kun-unbounded-exchange", "def-weil-pbc-kinjective-resolutions", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
Let $\square=(f,f',g,g',\alpha)$ be a cartesian square and $\Lambda$
a commutative ring. For every morphism $\varphi:K\to K'$ in
$D(X_{\Et},\Lambda)$ the square

$$
\begin{array}{ccc}
g^{-1}Rf_*K&\xrightarrow{\ \Ex_{\square,K}\ }&Rf'_*g'^{-1}K\\
\Big\downarrow{\scriptstyle g^{-1}Rf_*(\varphi)}&&
\Big\downarrow{\scriptstyle Rf'_*g'^{-1}(\varphi)}\\
g^{-1}Rf_*K'&\xrightarrow{\ \Ex_{\square,K'}\ }&Rf'_*g'^{-1}K'
\end{array}
$$

commutes; that is, $K\mapsto\Ex_{\square,K}$ is natural in $K$.
