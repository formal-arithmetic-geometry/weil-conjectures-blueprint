+++
id = "prose-02-17"
kind = "hidden"
title = "Weakly contractible objects (1)"
order = 74
+++
On a topological space we check exactness at points, and on the étale
site at geometric points. On $X_{\mathrm{pro}\acute{e}t}$ we check exactness, and compute
limits and colimits, by evaluating on weakly contractible objects. Over
these objects we can compute in the ordinary derived categories of
sheaves of modules by taking sections. Until
Section [sec-Classical-sheaves], $\mathcal R$ denotes a sheaf of rings on
$X_{\mathrm{pro}\acute{e}t}$, for instance the pullback of a condensed ring
(Section [sec-Coefficient-rings]).

The main result is
Corollary [corollary-evaluation-weakly-contractible-objects]. On a weakly
contractible affine $W$, taking sections is exact and commutes with all
limits and colimits of module sheaves. Moreover, these functors, for all
such $W$, are jointly conservative.

Stalk functors behave worse. A stalk functor is exact and commutes with
colimits, but not with infinite products. Products of sheaves on $X_{\acute{e}t}$
need not be exact either. The reason is that a section of a product of
surjections lifts in each factor only after its own refinement of the
cover, and infinitely many refinements cannot in general be made at once.
Evaluation at $W$ avoids both problems. It commutes with products because
limits of sheaves are computed on sections. It is exact because covers of
$W$ split.

In the simplest case, $X$ a geometric point, the site is that of profinite
sets (Proposition [proposition-pro-etale-site-separably-closed], proved
in Section [subsec-Condensed-rings] below). The
weakly contractible affines are then the extremally disconnected ones, among
them $\beta(T^\delta)$ for a set $T$. Indeed, a surjection of profinite sets
onto such an $S$ has a section by Gleason's theorem.
