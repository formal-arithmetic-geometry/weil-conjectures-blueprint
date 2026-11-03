+++
id = "lemma-weil-pbc-curve-filtered-cohomology"
kind = "lemma"
title = "Filtered cohomology continuity on a curve"
lean = ["AlgebraicGeometry.Scheme.H_map_isColimit_of_isFiltered"]
order = 1617
uses = ["def-weil-pbc-etale-sheaves", "lem-weil-pbc-cohomology-filtered-colimit"]
+++
Let $X$ be a quasi-compact and quasi-separated scheme and let
$(F_\lambda)$ be a filtered system of abelian etale sheaves on $X$, indexed by
a small filtered category. For every $q\geq0$ the canonical map

$$
\varinjlim_\lambda H^q(X,F_\lambda)\longrightarrow
H^q(X,\varinjlim_\lambda F_\lambda)
$$

is an isomorphism: every class on the colimit comes from some
$H^q(X,F_\lambda)$, and a class in $H^q(X,F_\lambda)$ which dies in
$H^q(X,\varinjlim F)$ already dies in $H^q(X,F_\mu)$ for some
$\lambda\to\mu$.
