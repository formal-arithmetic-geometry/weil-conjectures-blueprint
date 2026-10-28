+++
id = "thm-av-cube-general"
kind = "theorem"
title = "The theorem of the cube for invertible modules on a triple product"
lean = ["AlgebraicGeometry.nonempty_iso_of_nonempty_iso_overPullback_slices"]
order = 469
uses = ["def-sc-invertible-module", "lem-av-seesaw-closed", "lem-av-cube-open", "lem-av-cube-globalise"]
+++
Let $X$ and $Y$ be proper and geometrically integral over a field $k$, let $Z$ be a
connected $k$-scheme, and let $x\in X(k)$, $y\in Y(k)$, $z\in Z(k)$. If two invertible
modules $\mathcal M,\mathcal N$ on $X\times_kY\times_kZ$ become isomorphic on each of
the three slices $x\times Y\times Z$, $X\times y\times Z$ and $X\times Y\times z$, then
$\mathcal M\simeq\mathcal N$.
