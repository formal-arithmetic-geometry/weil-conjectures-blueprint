+++
id = "prose-02-12"
kind = "hidden"
title = "Weakly contractible objects and module sheaves"
order = 52
+++
Weakly contractible objects play the role that points play for sheaves
on a topological space, or geometric points for the étale site: we
check exactness and compute limits and colimits by evaluating on them.
On these objects, we can compute in the ordinary derived
categories of sheaves of modules by taking sections. Until
Section [sec-pe-comparison], $\mathcal R$ denotes a sheaf of rings on
$X_{\mathrm{pro}\acute{e}t}$, for instance the pullback of a condensed ring
(Section [sec-n-coefficients]).

The main result is Corollary [sk-cor-pe-sections]: on a weakly contractible
affine $W$, taking sections is exact and commutes with all limits and
colimits of module sheaves, and these functors are jointly conservative.
A comparison with stalks shows what is gained. A stalk functor is exact
and commutes with colimits, but not with infinite products. Products of
sheaves on $X_{\acute{e}t}$ need not be exact either: a section of a product of
surjections lifts in each factor only after its own refinement of the
cover, and infinitely many refinements cannot in general be made at
once. Evaluation at $W$
commutes with products because limits of sheaves are computed on
sections, and it is exact because covers of $W$ split. In the simplest
case, $X$ a geometric point, the site is that of profinite sets
(Proposition [sk-prop-pe-condensed-point]) and the weakly contractible
affines are the extremally disconnected ones, $\beta(T^\delta)$ for a set
$T$ among them: a surjection of profinite sets onto such an $S$ has a
section by Gleason's theorem.
