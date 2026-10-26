+++
id = "d-lines"
kind = "definition"
title = "The affine and projective lines"
lean = ["AlgebraicGeometry.ProjectiveLine.affineChart", "AlgebraicGeometry.ProjectiveLine.infinityChart", "AlgebraicGeometry.ProjectiveLine.isPullback_affineChart_infinityChart", "AlgebraicGeometry.ProjectiveLine.opensRange_affineChart_sup_opensRange_infinityChart", "AlgebraicGeometry.ProjectiveLine.infinity", "AlgebraicGeometry.ProjectiveLine.range_infinity", "AlgebraicGeometry.ProjectiveLine.compl_opensRange_affineChart_eq_singleton", "AlgebraicGeometry.ProjectiveLine.affineChart_comp_eq_of_isFrobenius", "AlgebraicGeometry.ProjectiveLine.infinityChart_comp_eq_of_isFrobenius"]
order = 3662
uses = ["def-trf-coefficient-conventions", "prop-trf-compact-support-perfectness"]
+++
Over a finite field $F$ from the coefficient setup,
put $\mathbf A^1_F=\operatorname{Spec}F[t]$.
Glue $\operatorname{Spec}F[t]$ to $\operatorname{Spec}F[z]$ along
$F[t,t^{-1}]=F[z,z^{-1}]$, with $z=t^{-1}$, to obtain $\mathbf P^1_F$.
The first chart is $\mathbf A^1_F$ and its complement is the point
$\infty$ defined by $z=0$. Frobenius acts by $t\mapsto t^{|F|}$ and
$z\mapsto z^{|F|}$ on these charts.
