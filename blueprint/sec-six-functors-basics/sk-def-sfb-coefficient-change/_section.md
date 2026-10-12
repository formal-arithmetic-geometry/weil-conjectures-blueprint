+++
id = "sk-def-sfb-coefficient-change"
kind = "definition"
title = "Change of condensed coefficients"
order = 1665
uses = ["sk-def-sfb-condensed-ring", "sk-def-sfb-pullback-from-point", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-coefficient-morphisms", "sk-def-sfb-finite-pushforward-pullback", "sk-def-sfb-module-objects", "sk-def-sfb-derived-categories", "sk-def-sfb-derived-extension-of-scalars", "sk-def-sfb-pullback-from-point-comp"]
lean = ["AlgebraicGeometry.ProEtale.coefficientMap", "AlgebraicGeometry.ProEtale.coefficientMap_id", "AlgebraicGeometry.ProEtale.coefficientMap_comp", "AlgebraicGeometry.ProEtale.map_coefficientMap_comp_condensedPullbackHom", "AlgebraicGeometry.ProEtale.condensedPushforwardHom_comp_map_coefficientMap"]
tags = ["sketch"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings
([sk-def-sfb-condensed-ring]). For a scheme $X$, the *coefficient change* on $X$ is

$$
a_X:=p_X^*a\colon\Lambda_X\longrightarrow\Lambda'_X ,
$$

the image of $a$ under the inverse image $p_X^*$ from the point
([sk-def-sfb-pullback-from-point]), a morphism between the coefficient ring objects
$\Lambda_X=p_X^*\Lambda$, $\Lambda'_X=p_X^*\Lambda'$ of $\Sh(X_{\mathrm{proét}},\Ab)$
([sk-def-sfb-pulled-back-coefficients]). It is a morphism of ring objects, and it is
functorial in $a$: $(\mathrm{id}_\Lambda)_X=\mathrm{id}_{\Lambda_X}$ and
$(b\circ a)_X=b_X\circ a_X$. The coefficient change induces the derived extension of scalars
([sk-def-sfb-derived-extension-of-scalars])

$$
T^X:=\Lambda'_X\otimes^{\mathrm L}_{\Lambda_X}-=L(\operatorname{Ext}_{a_X})\colon
D(\Mod_{\Lambda_X})\longrightarrow D(\Mod_{\Lambda'_X}),
$$

between the derived categories ([sk-def-sfb-derived-categories]) of the module categories of
[sk-def-sfb-module-objects]; it is left adjoint to the levelwise restriction of scalars
$D(\operatorname{Res}_{a_X})$.

For a morphism of schemes $f\colon X\to Y$ let $f^*$, $f_*$ be the pullback and pushforward of
abelian sheaves ([sk-def-sfb-finite-pushforward-pullback]), and let
$\alpha_f\colon f^*\Lambda_Y\to\Lambda_X$, $\eta_f\colon\Lambda_Y\to f_*\Lambda_X$ and
$\alpha'_f$, $\eta'_f$ be the coefficient morphisms of [sk-def-sfb-coefficient-morphisms] for
$\Lambda$ and for $\Lambda'$. The coefficient changes are compatible with them: the two squares

$$
\begin{array}{ccc}
f^*\Lambda_Y & \xrightarrow{\ f^*a_Y\ } & f^*\Lambda'_Y\\
{\scriptstyle\alpha_f}\downarrow & & \downarrow{\scriptstyle\alpha'_f}\\
\Lambda_X & \xrightarrow{\ \ a_X\ \ } & \Lambda'_X
\end{array}
\qquad\qquad
\begin{array}{ccc}
\Lambda_Y & \xrightarrow{\ \ a_Y\ \ } & \Lambda'_Y\\
{\scriptstyle\eta_f}\downarrow & & \downarrow{\scriptstyle\eta'_f}\\
f_*\Lambda_X & \xrightarrow{\ f_*a_X\ } & f_*\Lambda'_X
\end{array}
$$

commute, i.e. $\alpha'_f\circ f^*a_Y=a_X\circ\alpha_f$ and $f_*a_X\circ\eta_f=\eta'_f\circ a_Y$.
