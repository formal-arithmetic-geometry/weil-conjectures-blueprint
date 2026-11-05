+++
id = "theorem-generic-constructibility-base-change-rj--2"
kind = "theorem"
title = "Generic constructibility and base change for $Rj_*$ (2)"
name_showing = false
order = 583003
aliases = ["bp-r177-2"]
lean = ["AlgebraicGeometry.Etale.exists_hasConstructibleDirectImageBaseChangeOn"]
+++
With the data of clause [theorem-generic-constructibility-base-change-rj--1], the same nonempty open $S_0$
can be chosen so that, for every noetherian scheme $T$ and every morphism
$t:T\to S$ whose image lies in $S_0$, the base change map

$$
g_Y^*Rj_*F\longrightarrow Rj_{T,*}g_X^*F
$$

is an isomorphism. Here $g_X:X_T\to X$ and $g_Y:Y_T\to Y$ are the
projections. Thus bounded constructibility and base change hold on one
open, uniformly for all such $T$; no finite type hypothesis on $T$ is
needed.

Equivalently, writing $F_0=F|_{X_{S_0}}$ and
$g_{X,0}:X_T\to X_{S_0}$, $g_{Y,0}:Y_T\to Y_{S_0}$ for the projections,
the map

$$
g_{Y,0}^*Rj_{S_0,*}F_0\longrightarrow Rj_{T,*}g_{X,0}^*F_0
\tag{6.20}
$$

is an isomorphism for every morphism $T\to S_0$ with $T$ noetherian.
