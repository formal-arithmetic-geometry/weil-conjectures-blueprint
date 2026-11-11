+++
id = "proposition-compatibility-purity-composition--4"
kind = "proposition"
title = "Algebraically closed coefficients"
order = 801008
aliases = ["bp-r240-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation_comp_openImmersion", "AlgebraicGeometry.ProEtale.CondensedRing.smoothPurityIso_comp_openImmersion"]
+++
For $K\in D^b_{\mathrm{ctf}}(Z_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)$,
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

in $D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)$, where the coefficient $\overline{\mathbf Q}_\ell$ is omitted
from the displayed composite.
