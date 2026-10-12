+++
id = "sk-d-weil-push"
kind = "definition"
title = "Weil $!$-pushforward"
order = 2701
uses = ["sk-d-operator", "sk-d-relative-frob", "sk-d-six", "sk-d-weil", "sk-i-relative-frob", "sk-i-topology"]
lean = ["AlgebraicGeometry.ProEtale.WeilComplex.lowerShriekPush"]
tags = ["sketch"]
+++
Let $(K,\varphi)$ be a Weil complex on $X$ with Frobenius $\Phi_X=\Phi_{X,1}$, let
$f:X\to Y$ be compactifiable, and let $\Phi_Y=\Phi_{Y,1}$ be an endomorphism of
$Y$ over $s$ with $\Phi_Yf=f\Phi_X$ such that the relative Frobenius $r_1$ of
[sk-d-relative-frob] is proper. Put $L=Rf_!K$.
Cartesian $!$-base change for
$X'_m$, the unit of $r_m^*\dashv Rr_{m*}$, and the proper identification
$Rr_{m*}=Rr_{m!}$ give the comparison

$$
\theta_{f,m}:\Phi_{Y,m}^*Rf_!K
\simeq Rf'_{m!}p_m^*K
\xrightarrow{\eta_{r_m}^*}Rf'_{m!}Rr_{m!}r_m^*p_m^*K
\simeq Rf_!\Phi_{X,m}^*K.
$$

When $r_m$ is a finite universal homeomorphism, topological invariance makes
the middle unit invertible. Define
$\psi=Rf_!\varphi\circ\theta_{f,1}$; the Weil $!$-pushforward is the Weil complex
$(L,\psi)$ on $Y$ with Frobenius $\Phi_Y$. Its iterates are
$\psi_m=Rf_!\varphi_m\circ\theta_{f,m}$ by base-change composition.
The same definition and identity apply to arbitrary Frobenius
coefficient morphisms of [sk-d-weil].
