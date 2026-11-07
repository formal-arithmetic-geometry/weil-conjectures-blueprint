+++
id = "lemma-covers-degree-prime-to-ell--1"
kind = "lemma"
title = "Covers of degree prime to $\\ell$ (1)"
name_showing = false
order = 983001
aliases = ["bp-r299-1"]
lean = ["AlgebraicGeometry.Etale.CurveLocalModel.nonempty_coverDatum", "AlgebraicGeometry.Scheme.exists_sylow_galoisCover_trivializing", "AlgebraicGeometry.exists_finite_smooth_cover_not_dvd_ramificationIdx"]
+++
Let $S$ be the strict localization of a smooth curve over the
algebraically closed field $k$ at a closed
point $s$, and let $\mathcal F_1,\dots,\mathcal F_r$ be finite locally
constant sheaves on $(S-s)_{\acute{e}t}$. There is an integer $d_1$ prime to
$\ell$ with the following property. For every multiple $d$ of $d_1$ that
is prime to $\ell$ there is a finite flat morphism $S'\to S$ of degree $d$
such that

1. $S'$ is the strict localization of a smooth curve over $k$ at a
   closed point $s'$, and $s'$ is the only point of $S'$ over $s$; more
   precisely, $S'\to S$ is the base change of a finite flat morphism
   $C'\to C$ of smooth curves over $k$, where $C$ is an étale
   neighbourhood of $s$, which is étale away from $s$ and has a single
   point over $s$,
2. $S'-s'\to S-s$ is finite étale, and
3. the monodromy of the pullback of each $\mathcal F_i$ to $S'-s'$
   factors through a finite $\ell$-group.
