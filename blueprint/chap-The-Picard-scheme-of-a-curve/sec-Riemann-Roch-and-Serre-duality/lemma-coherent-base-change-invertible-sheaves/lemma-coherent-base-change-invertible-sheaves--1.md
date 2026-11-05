+++
id = "lemma-coherent-base-change-invertible-sheaves--1"
kind = "lemma"
title = "A finite free complex computing all base changes"
name_showing = false
order = 1530001
aliases = ["bp-r477-1"]
lean = ["AlgebraicGeometry.Scheme.Modules.exists_isFiniteFreeComplex_higherDirectImage"]
+++
Let $f:X\to T$ be proper and of finite presentation, and let $\mathcal F$
be an $\mathcal O_X$-module of finite presentation, flat over $T$.
Every point $t\in T$ has an open neighbourhood $U$ and a complex
$P^\bullet$ of finite free $\mathcal O_U$-modules, zero outside degrees
$[0,d]$ for some $d\geq0$, with the following property. For every
$a:T'\to U$ and every cartesian square defining
$f':X'\to T'$ and $b:X'\to X$ over $T'\to U\to T$, there exist
isomorphisms
$$
\mathcal H^q(a^*P^\bullet)\simeq R^qf'_*b^*\mathcal F
\qquad(q\geq0).
$$
These isomorphisms are asserted to exist separately for each base change
and degree. In particular, $P^\bullet$ computes the restrictions of
the higher direct images to $U$.

This applies to $f_T:C_T\to T$ and $\mathcal F=\mathcal L$:
$f_T$ is flat, proper and of finite presentation, and an invertible
module is of finite presentation and flat over the base of a flat morphism.
