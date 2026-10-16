+++
id = "lem-sc-finite-constant-length-flat"
kind = "lemma"
title = "Finite morphisms with constant fibre length are flat"
lean = ["Module.projective_of_finrank_fiber_eq", "Module.rankAtStalk_eq_of_finrank_fiber_eq", "AlgebraicGeometry.Scheme.Hom.finrank_residueField_genericPoint_of_fiberDegree_eq", "AlgebraicGeometry.Scheme.Hom.flat_of_fiberDegree_eq", "AlgebraicGeometry.Scheme.Hom.finrank_eq_of_fiberDegree_eq", "AlgebraicGeometry.Scheme.Hom.flat_of_fiberDegree_eq_of_isClosed", "AlgebraicGeometry.Scheme.Hom.finrank_eq_of_fiberDegree_eq_of_isClosed", "AlgebraicGeometry.Scheme.Hom.finrank_residueField_genericPoint_of_fiberDegree_eq_of_isClosed"]
order = 563
uses = ["def-sc-function-field"]
+++
Let $f:X\to Y$ be a finite surjective morphism of varieties over
a field $k$ such that the fibre length
$\dim_{k(y)}f_*\mathcal O_X\otimes k(y)$ is constant, equal to
$r$, as $y$ ranges over the closed points of $Y$. Then
$f$ is finite flat, $f_*\mathcal O_X$ is locally free of rank
$r$, and $\deg(f)=[k(X):k(Y)]$ of
function fields equals $r$.
