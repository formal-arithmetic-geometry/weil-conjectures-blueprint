+++
id = "lem-av-cube-open"
kind = "lemma"
title = "Triviality on a fibre spreads out"
lean = ["AlgebraicGeometry.exists_mem_nonempty_iso_preimageSnd_of_nonempty_iso_fiber", "AlgebraicGeometry.exists_mem_nonempty_iso_preimageSnd"]
order = 466
uses = ["def-sc-invertible-module", "lem-av-seesaw-criterion"]
+++
Let $X$ and $Y$ be proper and geometrically integral over a field $k$, with points
$x\in X(k)$ and $y\in Y(k)$, let $Z$ be a $k$-scheme, and let $\mathcal M,\mathcal N$
be invertible modules on $X\times_kY\times_kZ$ which become isomorphic on the slices
$x\times Y\times Z$ and $X\times y\times Z$. If $\mathcal M$ and $\mathcal N$ become
isomorphic on the fibre $X\times_kY\times_k\operatorname{Spec}F$ over a point
$\varphi:\operatorname{Spec}F\to Z$ with values in a field $F$, then they are
isomorphic on $X\times_kY\times_kU$ for an open neighbourhood $U$ of the image of
$\varphi$.

In particular, if $z\in Z(k)$ and $\mathcal M,\mathcal N$ are moreover isomorphic on
the slice $X\times Y\times z$, they are isomorphic on $X\times_kY\times_kU$ for an
open neighbourhood $U$ of $z$.
