+++
id = "pqf-def-quasifinite"
kind = "definition"
title = "Quasi-finite morphisms and finite fibres"
order = 300
lean = ["AlgebraicGeometry.Scheme.Hom.IsQuasiFiniteAtPoint", "AlgebraicGeometry.Scheme.Hom.IsLocallyQuasiFinite", "AlgebraicGeometry.Scheme.Hom.IsQuasiFinite", "AlgebraicGeometry.Scheme.Hom.HasFiniteFibres", "AlgebraicGeometry.Scheme.Hom.fiber"]
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $f:X\to S$ be a morphism of schemes.

1. $f$ is *quasi-finite at a point $x\in X$* if there exist an
affine neighbourhood $\operatorname{Spec}A=U\subset X$ of $x$ and
an affine open $\operatorname{Spec}R=V\subset S$ with
$f(U)\subset V$ such that the ring map $R\to A$ is of finite type
and quasi-finite at the prime of $A$ corresponding to $x$.
1. $f$ is *locally quasi-finite* if it is quasi-finite at every
point of $X$.
1. $f$ is *quasi-finite* if it is of finite type and every point
of $X$ is an isolated point of its fibre.

We say that
$f$ *has finite fibres* if for every $s\in S$ the set
$f^{-1}(\{s\})$ is finite; the *fibre* of $f$ at $s$ is the scheme
$X_s=X\times_S\operatorname{Spec}\kappa(s)$.
