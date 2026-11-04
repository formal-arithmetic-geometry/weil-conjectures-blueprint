+++
id = "proposition-compatibility-purity-composition"
kind = "proposition"
title = "Compatibility of purity with composition"
order = 794
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation_comp_openImmersion", "AlgebraicGeometry.ProEtale.CondensedRing.smoothPurityIso_comp_openImmersion"]
+++
For every admissible $\Lambda$ and $K\in D^b_{\mathrm{ctf}}(Z,\Lambda)$,
the map $\gamma_{g\circ f}(K)$ of (9.2) is the composite

$$
\begin{aligned}
(g\circ f)^{*}K(d+e)[2d+2e]
&\simeq f^{*}\bigl(g^{*}K(e)[2e]\bigr)(d)[2d]\\
&\xrightarrow{\ f^{*}(\gamma_g(K))(d)[2d]\ }
f^{*}\bigl(g^!K\bigr)(d)[2d]\\
&\xrightarrow{\ \gamma_f(g^!K)\ }
f^!g^!K
\simeq(g\circ f)^!K
\end{aligned}
$$

in $D^b_{\mathrm{ctf}}(X,\Lambda)$, where the coefficient $\Lambda$ is omitted
from the displayed composite.
