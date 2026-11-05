+++
id = "lemma-extension-across-finite-subset--1"
kind = "lemma"
title = "Extension across a finite subset over a fixed open"
name_showing = false
order = 576001
aliases = ["bp-r174-1"]
lean = ["AlgebraicGeometry.Etale.HasDirectImageBaseChangeOnPlus.of_finite_boundary"]
uses = ["definition-derived-base-change-map"]
+++
Let $k$ be a field, let $S$ be of finite type over $k$, and let $\Lambda$
be a finite commutative ring whose exponent is invertible on $S$.
Let $b:Y\to S$ be proper, let $X$ be any scheme, let $j:X\to Y$ be a
morphism, and let
$G\subset Y$ be open with a closed immersion $i:Z\hookrightarrow Y$
whose image is $Y\setminus G$. Fix an open $U\subset S$ such that
$Z\times_S U\to U$ is finite, and let
$K\in D^+(X_{\acute{e}t},\Lambda)$. Throughout this statement,
$\Dbc$ denotes bounded complexes with constructible cohomology on the
étale site.

Put $a=bj$, $X_G=j^{-1}(G)$, $j_G:X_G\to G$, and $K_G=K|_{X_G}$.
For a morphism $t:T\to S$, use a subscript $T$ for base change, write
$g_Y:Y_T\to Y$ and $g_G:G_T\to G$ for the projections, and write
$K_T$ and $K_{G,T}$ for the pullbacks of $K$ and $K_G$.
Suppose that for every noetherian scheme $T$ and every $t:T\to S$
whose image is contained in $U$, both

$$
Rj_{G,T,*}K_{G,T}\in\Dbc(G_T,\Lambda),\qquad
Ra_{T,*}K_T\in\Dbc(T,\Lambda),
$$

and the two base change maps

$$
g_G^*Rj_{G,*}K_G\longrightarrow Rj_{G,T,*}K_{G,T},\qquad
t^*Ra_*K\longrightarrow Ra_{T,*}K_T
$$

are isomorphisms. Then, for every such $t:T\to S$,

$$
Rj_{T,*}K_T\in\Dbc(Y_T,\Lambda),
$$

and the base change map

$$
g_Y^*Rj_*K\longrightarrow Rj_{T,*}K_T
$$

is an isomorphism.
