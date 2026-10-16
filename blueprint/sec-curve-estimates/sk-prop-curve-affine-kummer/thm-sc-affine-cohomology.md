+++
id = "thm-sc-affine-cohomology"
kind = "theorem"
title = "Kummer computation on an affine curve"
lean = ["AlgebraicGeometry.IsConnectedCurve.sheafH_constantZMod_of_isAffine"]
order = 1029
uses = ["def-sc-curves", "def-sc-kummer-sequence", "def-sc-mu-trivialization", "lem-sc-affine-cohomological-dimension", "lem-sc-affine-unit-quotient", "lem-sc-brauer-zero", "lem-sc-h1-gm-pic", "lem-sc-pic-affine", "lem-sc-primitive-root"]
+++
Let $k$ be algebraically closed, let $C$ be a
smooth affine connected curve over $k$, and let
$n\geq1$ be prime to $\operatorname{char}k$. Then, under the
canonical trivialization $\theta_\zeta$ of
[def-sc-mu-trivialization],

$$
H^0(C_{\Et},\mathbf F_n)\cong\mathbf Z/n\mathbf Z,\qquad
\mathcal O_C(C)^\times/\mathcal O_C(C)^\times{}^{\,n}
\text{ is finite},
$$

and there is a canonical short exact sequence

$$
0\longrightarrow\mathcal O_C(C)^\times/\mathcal O_C(C)^\times{}^{\,n}
\longrightarrow H^1(C_{\Et},\mathbf F_n)\longrightarrow
\operatorname{Pic}(C)[n]\longrightarrow0
$$

($\operatorname{Pic}(C)[n]$ finite, by [lem-sc-pic-affine]; the
unit term vanishes when $\mathcal O_C(C)^\times$ is $n$-divisible,
e.g. when $C=\mathbf A^1$), and
$H^q(C_{\Et},\mathbf F_n)=0$ for all $q>1$.
