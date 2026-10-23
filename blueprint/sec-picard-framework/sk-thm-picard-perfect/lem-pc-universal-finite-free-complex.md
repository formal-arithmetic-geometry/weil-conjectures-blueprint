+++
id = "lem-pc-universal-finite-free-complex"
kind = "lemma"
title = "Local finite free models for higher direct images"
order = 782
lean = ["AlgebraicGeometry.Scheme.Modules.exists_isFiniteFreeComplex_higherDirectImage"]
uses = ["def-pc-base-change", "lem-pc-rf-perfect-base-change"]
+++
Let $f:X\to T$ be a proper morphism of finite presentation and $\mathcal F$
an $\mathcal O_X$-module of finite presentation, flat over $T$. Every point
$t\in T$ has an open neighbourhood $U$, an integer $d\ge0$ and a complex $P$
of finite free $\mathcal O_U$-modules concentrated in degrees $[0,d]$ such
that for every morphism $g:T'\to U$, with $f':X'\to T'$ and $\mathcal F'$
the base changes of $f$ and $\mathcal F$ ([def-pc-base-change]), there are
isomorphisms $H^q(g^*P)\cong R^qf'_*\mathcal F'$ for all $q\ge0$.
