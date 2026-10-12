+++
id = "thm-pur-weil-equivariance-of-purity-and-trace"
kind = "theorem"
title = "Weil equivariance of purity and trace"
order = 2578
uses = ["def-coefficient-twists-detailed", "def-pur-compact-support-transport", "def-pur-conventions", "def-pur-scheme-geometric-frobenius", "def-pur-smooth-pullback-exchange", "def-pur-smooth-trace", "def-pur-tate-datum", "def-sbc-smooth-morphisms", "def-weil-frobenius-coefficient-twists", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "thm-pur-adic-reconstruction", "thm-pur-smooth-base-change-coherence"]
+++
In the purity conventions of this chapter ([def-pur-conventions]), fix the
geometric-Frobenius datum of [def-pur-scheme-geometric-frobenius],
and let $f:X\to Y$ be smooth of relative dimension $d$ with strict
Weil datum $(K,\varphi_K)$ as in [def-pur-tate-datum]. Then smooth
purity is equivariant: the square

$$
\begin{array}{ccc}
Lg_{X,\gamma}^*Lf^*K(d)[2d]
& \xrightarrow{\ Lg_{X,\gamma}^*(\gamma_{f,K})\ }
& Lg_{X,\gamma}^*Rf^!K\\
\big\downarrow\ \varphi^{\mathrm{pur}}_{f,K}
& \sim & \big\downarrow\ \varphi^!_{f,K}\\
Lf^*K(d)[2d]
& \xrightarrow{\ \gamma_{f,K}\ }
& Rf^!K
\end{array}
$$

commutes. If $\varphi_{f_!Rf^!K}$ is formed from $\varphi^!_{f,K}$ by
[def-pur-compact-support-transport], then the exceptional counit is
equivariant, and if $\varphi_{f_!Lf^*K(d)[2d]}$ is formed from
$\varphi^{\mathrm{pur}}_{f,K}$, then the normalized smooth trace of
[def-pur-smooth-trace] is equivariant:

$$
\begin{array}{ccc}
Lg_{Y,\gamma}^*Rf_!Lf^*K(d)[2d]
& \xrightarrow{\ Lg_{Y,\gamma}^*(\operatorname{Tr}^{\mathrm{sm}}_{f,K})\ }
& Lg_{Y,\gamma}^*K\\
\big\downarrow\ \varphi_{f_!Lf^*K(d)[2d]}
& \sim & \big\downarrow\ \varphi_K\\
Rf_!Lf^*K(d)[2d]
& \xrightarrow{\ \operatorname{Tr}^{\mathrm{sm}}_{f,K}\ }
& K.
\end{array}
$$
