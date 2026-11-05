+++
id = "theorem-generic-constructibility-base-change-rj"
kind = "theorem"
title = "Generic constructibility and base change for $Rj_*$"
order = 583
lean = ["AlgebraicGeometry.Etale.exists_hasConstructibleDirectImageBaseChangeOn"]
+++
Let $S$ be integral, and let $j:X\hookrightarrow Y$ be an open immersion of
$S$-schemes. For a constructible
$\Fell$-sheaf $F$ on $X_{\acute{e}t}$, there is a nonempty open
$S_0\subset S$ such that

$$
Rj_{S_0,*}(F|_{X_{S_0}})\in\Dbc(Y_{S_0},\Fell),
\tag{6.19}
$$

and such that for every $k$-scheme $T\to S_0$ of finite type, with base change
$j_T:X_T\hookrightarrow Y_T$ and projections $g_X:X_T\to X_{S_0}$ and
$g_Y:Y_T\to Y_{S_0}$, the base change map

$$
\beta_T:g_Y^*Rj_{S_0,*}(F|_{X_{S_0}})
\longrightarrow Rj_{T,*}g_X^*(F|_{X_{S_0}})
\tag{6.20}
$$

is an isomorphism.
