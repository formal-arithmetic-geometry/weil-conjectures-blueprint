+++
id = "prose-02-39"
kind = "hidden"
title = "Constructible sheaves (1)"
order = 142
+++
The six operations act on constructible complexes, and their finiteness
theorems are proved on the étale site. To use these theorems we show that
constructible pro-étale sheaves are classical, so that they correspond to
constructible étale sheaves, and that the comparison preserves finite Tor
amplitude.

A sheaf of modules on $X_{\mathrm{pro}\acute{e}t}$ is locally constant if it is trivialized by
a pro-étale covering, and it is of finite presentation if its constant
models are finitely presented $\Lambda$-modules. Building on this, for Noetherian
$\Lambda$, a sheaf is constructible if, locally on $X$, there is a finite
partition into constructible locally closed strata such that it is locally
constant of finite type on each stratum. We write $\Cons(X,\Lambda)$ for the
category of constructible sheaves and $\Dbc(X,\Lambda)$ for the bounded
complexes with constructible cohomology sheaves. For a discrete ring these notions
agree with Definition [definition-constructible-sheaves], which is stated
for all coefficient rings in Section [sec-Constructibility] below. These conditions
refer only to pro-étale covers, so the main step is to descend torsors
from pro-étale to étale covers.

A priori there could be more pro-étale local systems than étale
ones, since the covers are larger. For finite groups, however, there are not. Indeed, a
torsor under a finite group is described by a cocycle on one pro-étale
affine cover. That cover is a limit of étale covers and the group is
classical, so the cocycle is defined at a finite stage. For $\mathbf Z_\ell$, by contrast, there
are more local systems, and this is the reason for using the pro-étale
site. For example, over $\operatorname{Spec}\mathbf F_q$, a rank-one $\mathbf Z_\ell$-local system
on which Frobenius acts by a unit $u\in\mathbf Z_\ell^\times$ of infinite order is
trivialized by a pro-étale cover but by no étale one. Our comparison
therefore concerns only finite coefficients, and we study $\ell$-adic
local systems through their reductions.

What we use later is the case of a finite ring $A$. For such $A$,
Theorem [theorem-comparison-constructible-sheaves] and
Corollary [corollary-finite-tor-amplitude-under-comparison] identify the
category $D^b_{\mathrm{ctf}}(X,A)$ on the pro-étale site with the classical one.
