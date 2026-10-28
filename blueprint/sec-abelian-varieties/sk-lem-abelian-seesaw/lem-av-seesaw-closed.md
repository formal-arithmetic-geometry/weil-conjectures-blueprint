+++
id = "lem-av-seesaw-closed"
kind = "lemma"
title = "The seesaw principle: the locus of triviality on the fibres is closed"
lean = ["AlgebraicGeometry.Scheme.Modules.isClosed_setOf_nonempty_iso_fiber", "AlgebraicGeometry.isClosed_setOf_nonempty_iso_fiber"]
order = 461
uses = ["def-sc-invertible-module", "lem-av-seesaw-criterion"]
+++
Let $f:P\to T$ be proper, flat, locally of finite presentation and with
geometrically integral fibres, and let $\mathcal M,\mathcal N$ be invertible
$\mathcal O_P$-modules. Then the set of $t\in T$ with
$\mathcal M_t\simeq\mathcal N_t$ on the fibre $P_t$ is closed in $T$.

In particular, for $X,Y$ proper and geometrically integral over a field $k$, any
$k$-scheme $Z$ and invertible modules $\mathcal M,\mathcal N$ on $X\times_kY\times_kZ$,
the set of $t\in Z$ such that $\mathcal M$ and $\mathcal N$ become isomorphic on
$X\times_kY\times_k\operatorname{Spec}\kappa(t)$ is closed.
