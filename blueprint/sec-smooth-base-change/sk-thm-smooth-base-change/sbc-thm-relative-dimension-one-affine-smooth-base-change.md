+++
id = "sbc-thm-relative-dimension-one-affine-smooth-base-change"
kind = "theorem"
title = "Relative-dimension-one affine smooth base change"
order = 1423
uses = ["def-sbc-smooth-morphisms", "def-weil-pbc-scheme-conventions", "sbc-def-base-change-map", "sbc-def-base-change-square", "sbc-thm-smooth-base-change"]
+++
Let $u:V\to S$ be affine and
smooth of relative dimension one,
let $h:T\to S$ be
quasi-compact and
quasi-separated, and let $F$ be a sheaf on $T_{\Et}$ whose geometric
stalks are torsion of orders invertible on $S$. In the induced
Cartesian square

$$
\begin{array}{ccc}
V & \longleftarrow & T\times_SV\\
u\big\downarrow & & \big\downarrow h_V\\
S & \longleftarrow & T
\end{array}
$$

the exchange map

$$
u^{-1}R^qh_*F\xrightarrow{\ \sim\ }R^qh_{V,*}(F|_{T\times_SV})
$$

is an isomorphism for every $q\geq0$.

## Proof

The square displayed is a base-change square of
[sbc-def-base-change-square] with base
$S$, vertical side $u:V\to S$ (smooth of relative dimension one) and
horizontal side $h:T\to S$ (quasi-compact and quasi-separated), the
projections being $h_V$ and the projection $T\times_SV\to V$; the
hypotheses on the torsion stalks of $F$ and the orders invertible on
$S$ are exactly the ones of [sbc-thm-smooth-base-change], so that
theorem gives the displayed isomorphism in every degree, identified
with the base-change map of [sbc-def-base-change-map] (the
smoothness of [def-sbc-smooth-morphisms] and the quasi-compactness
of [def-weil-pbc-scheme-conventions] are the hypotheses used
there).
