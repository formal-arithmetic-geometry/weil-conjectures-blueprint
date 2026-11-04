+++
kind  = "proof"
of    = "lem-weil-pbc-cohomology-filtered-colimit"
+++
On the basis of quasi-compact quasi-separated etale objects, every cover has
a finite refinement by basis objects, and their pairwise fibre products stay
in the basis. Hence the objectwise filtered colimit of the $F_a$ satisfies
the sheaf equalizer axiom on this basis: filtered colimits of abelian groups
commute with finite products and kernels. It therefore computes the sheaf
colimit of [def-weil-pbc-etale-sheaves] on every basis object.

For a hypercover finite in each degree, as in
[def-weil-pbc-finite-split-hypercover], this gives
$C^n(U,\varinjlim_aF_a)=\varinjlim_a C^n(U,F_a)$ in each degree. Exactness of
filtered colimits gives the same identity on $H^q$. Now take the colimit over
hypercover refinements and use [thm-weil-pbc-hypercover-cohomology] on both
sides. The two colimits commute, by their universal properties. Every
identification is induced by maps of sheaves and restriction of sections, so
it is the canonical map of the statement. See also
[Stacks Project, Tag 09Z1](https://stacks.math.columbia.edu/tag/09Z1), whose
cohomological input is proved here by refinement. For module sheaves, use the
module version of [thm-weil-pbc-hypercover-cohomology]; filtered colimits of
modules have the same exactness and finite-limit properties.
