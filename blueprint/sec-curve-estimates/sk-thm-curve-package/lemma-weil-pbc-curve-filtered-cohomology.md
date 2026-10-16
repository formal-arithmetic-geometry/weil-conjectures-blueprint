+++
id = "lemma-weil-pbc-curve-filtered-cohomology"
kind = "lemma"
title = "Filtered cohomology continuity on a curve"
lean = ["AlgebraicGeometry.Scheme.H_map_isColimit_of_isFiltered"]
order = 1206
uses = ["def-weil-pbc-eight-curve-assertions", "def-weil-pbc-etale-sheaves", "lem-weil-pbc-cohomology-filtered-colimit"]
+++
Let $X$ be quasi-compact and quasi-separated and let $(F_\lambda)$ be a
filtered system of torsion etale sheaves. For every $q\geq0$ the canonical
map

$$
\varinjlim_\lambda H^q(X,F_\lambda)\longrightarrow
H^q(X,\varinjlim_\lambda F_\lambda)
$$

is an isomorphism, naturally in $X$, the system, and pullback along a field
extension.
