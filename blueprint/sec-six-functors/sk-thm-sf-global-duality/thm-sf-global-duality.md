+++
id = "thm-sf-global-duality"
kind = "theorem"
title = "Global Verdier duality"
order = 3306
uses = ["def-sf-datum", "def-sf-pf", "def-trf-admissibility", "def-weil-exceptional-inverse-image", "def-weil-finite-coefficient-point", "lem-sf-point", "thm-sf-verdier-exchange"]
+++
In the setting of [def-sf-datum], assume that $k$ is separably closed, and
let $X$ be smooth, separated of finite
type and geometrically connected of pure dimension $d$ over $k$, with
structure morphism $a_X$ (no admissibility hypothesis: $Ra_X^!$ is the
constructible exceptional inverse image of
[def-weil-exceptional-inverse-image], and $a_X$ is exceptionally admissible
in the sense of [def-trf-admissibility] as every separated finite-type
morphism is). Assume either
that $X$ is proper, or that $X=X_0\times_{k_0}k$ for a smooth, separated
finite-type, geometrically connected $k_0$-scheme $X_0$; in the latter
case no properness is required. Let $K\in D^b_{ctf}(X,\Lambda)$. Then
there is a canonical isomorphism

$$
R\Gamma_c(X,K)^\vee\xrightarrow{\ \sim\ }R\Gamma\bigl(X,\mathbb D_XK\bigr)
$$

in the point category $D^b_c(s,\Lambda)$ of
[def-weil-finite-coefficient-point], natural in $K\in D^b_{ctf}(X,\Lambda)$
and compatible with shifts. For
$K=\Lambda_X$ it specializes to
$R\Gamma_c(X,\Lambda)^\vee\cong R\Gamma(X,\omega_X)$.
