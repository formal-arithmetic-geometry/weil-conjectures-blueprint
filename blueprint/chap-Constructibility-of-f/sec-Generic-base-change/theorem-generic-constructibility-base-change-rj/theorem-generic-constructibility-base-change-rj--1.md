+++
id = "theorem-generic-constructibility-base-change-rj--1"
kind = "theorem"
title = "Generic constructibility and base change for $Rj_*$ (1)"
name_showing = false
order = 582001
aliases = ["bp-r177-1"]
lean = ["AlgebraicGeometry.Etale.exists_hasConstructibleDirectImageBaseChangeOn"]
uses = ["definition-constructible-sheaves"]
+++
Let $k$ be a field, let $S$ be integral and of finite type over $k$, and
let $Y\to S$ be of finite type. Let $\Lambda$ be a finite commutative ring
such that some positive integer annihilating $\Lambda$ is invertible on
$S$, and let $j:X\hookrightarrow Y$ be an open immersion. We work on the
étale site, and write $\Dbc(Z,\Lambda)$ for bounded complexes of étale
$\Lambda$-sheaves with constructible cohomology.

For a constructible $\Lambda$-sheaf $F$ on $X_{\acute{e}t}$, there is a
nonempty open $S_0\subset S$ such that for every noetherian scheme $T$
and every morphism $t:T\to S$ whose image lies in $S_0$, with base change
$j_T:X_T\hookrightarrow Y_T$ and projection $g_X:X_T\to X$, one has

$$
Rj_{T,*}g_X^*F\in\Dbc(Y_T,\Lambda).
$$

In particular, taking $T=S_0$ gives

$$
Rj_{S_0,*}(F|_{X_{S_0}})\in\Dbc(Y_{S_0},\Lambda).
$$
