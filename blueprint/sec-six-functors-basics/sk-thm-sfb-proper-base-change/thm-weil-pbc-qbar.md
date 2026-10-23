+++
id = "thm-weil-pbc-qbar"
kind = "theorem"
title = "Proper base change for Weil complexes"
order = 2216
lean = ["AlgebraicGeometry.WeilComplex.nonempty_upperStar_derivedLowerStar_iso_of_isProper", "AlgebraicGeometry.WeilSheaf.nonempty_upperStar_higherLowerStar_iso_of_isProper"]
uses = ["def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "det-def-sfb-module-pushforward-pullback", "sk-def-sfb-base-change-morphism"]
+++
Fix the finite-field datum $(p,a,q,k_0,k)$ of [def-weil-finite-field-fiber]
and a prime $\ell\neq p$, and use Weil sheaves and Weil complexes with
coefficients $\Lambda=\Qlb$ as in [def-weil-weil-sheaf-complex]. Let

$$
\begin{array}{ccc}
X'_0 & \xrightarrow{\;h'_0\;} & X_0\\
{\scriptstyle f'_0}\downarrow & & \downarrow{\scriptstyle f_0}\\
Y'_0 & \xrightarrow{\;h_0\;} & Y_0
\end{array}
$$

be a cartesian square of $k_0$-schemes with $f_0$ proper and $h_0$ arbitrary,
where $Y_0$ and $Y'_0$ are of finite type over $k_0$
([def-weil-scheme-morphism-properties]). Write $X=X_0\times_{k_0}k$, and
similarly $X'$, $Y$, $Y'$, for the geometric fibres, $f,f',h,h'$ for the
induced morphisms (again a cartesian square, with $f$ and $f'$ proper), and
$g_X,g_{X'},g_Y,g_{Y'}$ for the geometric Frobenius automorphisms of
[def-weil-frobenius-detailed], which commute with $f,f',h,h'$.

On Weil modules, the pullback $h^*(M,\theta)$ is the module pullback $h^*M$
([det-def-sfb-module-pushforward-pullback]) with the Weil structure
$g_{Y'}^*h^*M\cong h^*g_Y^*M\xrightarrow{h^*\theta}h^*M$, and the pushforward
$f_*(M,\theta)$ is $f_*M$ with the Weil structure
$g_Y^*f_*M\cong f_*g_X^*M\xrightarrow{f_*\theta}f_*M$ (the first isomorphism
holds because $g_X,g_Y$ are automorphisms with $fg_X=g_Yf$); likewise for
$h'$ and $f'$. Write $h^*$ for the functor induced by the exact pullback on
derived categories of Weil modules, and $Rf_*$ for the right derived functor
of the pushforward.

1. For every Weil complex $K$ on $X_0$, the objects $h^*Rf_*K$ and
   $Rf'_*h'^*K$ are Weil complexes on $Y'_0$, and the base change morphism
   $$
   \mathrm{BC}_K\colon h^*Rf_*K\xrightarrow{\ \sim\ }Rf'_*h'^*K,
   $$
   formed by the formula of [sk-def-sfb-base-change-morphism] from the
   derived adjunctions $f^*\dashv Rf_*$ and $f'^*\dashv Rf'_*$ of Weil modules
   and the pullback comparison $f'^*h^*\cong h'^*f^*$, is an isomorphism of
   Weil complexes.
2. For every Weil sheaf $\mathcal F$ on $X_0$ and every $i\geq0$, with
   $R^if_*\mathcal F=\mathcal H^i(Rf_*\mathcal F)$, there is an isomorphism of
   Weil sheaves on $Y'_0$
   $$
   h^*R^if_*\mathcal F\cong R^if'_*h'^*\mathcal F .
   $$
