+++
id = "def-sc-etale-torsion-cd"
kind = "definition"
title = "Étale torsion cohomological dimension bound"
order = 4902
lean = ["AlgebraicGeometry.Etale.torsionCohomologicalDimensionLE"]
+++
For a scheme $X$ and an integer $c\geq0$, write
$\operatorname{cd}_{\rm tor}(X)\leq c$ if $H^q(X,F)=0$ for every torsion
abelian étale sheaf $F$ and every $q>c$, where cohomology is the ordinary
derived section functor. For a field $K$, write
$\operatorname{cd}_{\rm tor}(K)\leq c$ for this condition on
$\operatorname{Spec}K$.

*Note.* This is an étale torsion bound, not the pro-étale proper-map
predicate of the ambient chapter.

Unresolved dependencies: def:weil-pbc-etale-sheaves, def:weil-pbc-etale-cohomology, def:weil-full-cohomological-dimension
