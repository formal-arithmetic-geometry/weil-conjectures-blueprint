+++
kind  = "proof"
of    = "lem-sc-zariski-filtered-cohomology"
+++
Every open of a Noetherian space is quasi-compact; finite
intersections of opens are again opens. Hence every covering
has a finite subcover. Objectwise filtered colimits of the
sheaves satisfy the sheaf equalizer axiom, because filtered
colimits of abelian groups commute with finite products and
kernels. Thus their values on each open compute the sheaf
colimit.

Apply the finite-hypercover computation underlying
[thm-weil-pbc-hypercover-cohomology]. Its proof uses
local effacement of positive cohomology classes and finite
cover refinements; both apply verbatim to this site.
Explicitly, to compute degree $q$, refine the covering in
each degree through $q+1$, successively killing the finitely
many obstruction classes. Each such degree is a finite
disjoint union of opens, and every matching covering has
a finite refinement. The resulting section complex has
finite products in each of the degrees needed to compute
$H^q$. These commute with the given filtered colimit.
Exactness of filtered colimits then makes the cohomology
commute as well. Finally take the colimit over hypercover
refinements. This is the same cochain argument as
[lem-weil-pbc-cohomology-filtered-colimit], with the
Zariski covering basis in place of the etale one.
