+++
id = "lem-sc-finite-constant-length-flat"
kind = "lemma"
title = "Finite morphisms with constant fibre length are flat"
lean = ["Module.projective_of_finrank_fiber_eq", "Module.rankAtStalk_eq_of_finrank_fiber_eq", "AlgebraicGeometry.Scheme.Hom.finrank_residueField_genericPoint_of_fiberDegree_eq", "AlgebraicGeometry.Scheme.Hom.flat_of_fiberDegree_eq", "AlgebraicGeometry.Scheme.Hom.finrank_eq_of_fiberDegree_eq", "AlgebraicGeometry.Scheme.Hom.flat_of_fiberDegree_eq_of_isClosed", "AlgebraicGeometry.Scheme.Hom.finrank_eq_of_fiberDegree_eq_of_isClosed", "AlgebraicGeometry.Scheme.Hom.finrank_residueField_genericPoint_of_fiberDegree_eq_of_isClosed"]
order = 549
uses = ["def-sc-function-field"]
+++
Let $f:X\to Y$ be a finite morphism of schemes which is locally of
finite presentation, with $Y$ reduced and Jacobson (for example $Y$ a
reduced scheme of finite type over a field). For $y\in Y$ let
$\deg_y(f):=\dim_{\kappa(y)}\Gamma(X_y,\mathcal O_{X_y})
=\dim_{\kappa(y)}f_*\mathcal O_X\otimes\kappa(y)$ be the length of the
fibre $X_y=f^{-1}(y)$, and suppose that $\deg_y(f)=r$ for every closed
point $y$ of $Y$. Then $\deg_y(f)=r$ for every $y\in Y$, $f$ is flat,
and $f_*\mathcal O_X$ is locally free of rank $r$. If moreover $X$ is
integral with generic point $\eta$, then
$[\kappa(\eta):\kappa(f(\eta))]=r$; in particular, for a finite
surjective morphism $f$ of varieties over a field $k$, the degree
$\deg(f)=[k(X):k(Y)]$ of function fields
([def-sc-function-field]) equals $r$.
