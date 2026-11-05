+++
id = "lemma-generic-smooth-open--1"
kind = "lemma"
title = "The étale formulation with strict specialization"
name_showing = false
order = 580001
aliases = ["bp-r176-1"]
lean = ["AlgebraicGeometry.exists_isFinite_universallyInjective_smooth_dense"]
uses = []
+++
Let $k$ be any field, let $S$ be an integral scheme of finite type over
$k$, and let $f:X\to S$ be of finite type with $X$ nonempty. No
separatedness hypothesis is needed. Let $\Lambda$ be any commutative ring
and let $F$ be a constructible sheaf of $\Lambda$-modules on
$X_{\acute{e}t}$. Here constructibility means that there is a finite
stratification by constructible locally closed subschemes on which $F$
is locally constant with finitely generated geometric stalks; we call
such locally constant sheaves finite locally constant.

There are a nonempty open $U\subset S$, an integral scheme $S'$, and a
finite, surjective, universally injective morphism $\pi:S'\to U$ with
the following property. Write $X'=X_U\times_U S'$, with projections
$f':X'\to S'$ and $p:X'\to X$. There are a reduced scheme $V$ and an
immersion $v:V\to X'$ whose image is open and dense, such that
$f'\circ v$ is smooth and $(p\circ v)^*F$ is finite locally constant.
Moreover, if $\eta'$ is the generic point of $S'$, then every
$x\in X'$ with $f'(x)=\eta'$ and $x\notin v(V)$ admits a point
$y\in v(V)$ such that
$$
f'(y)=\eta',\qquad x\in\overline{\{y\}},\qquad y\ne x.
$$
