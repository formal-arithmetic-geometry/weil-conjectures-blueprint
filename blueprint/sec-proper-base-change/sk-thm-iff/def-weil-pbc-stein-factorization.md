+++
id = "def-weil-pbc-stein-factorization"
kind = "definition"
title = "Stein factorization"
order = 1073
lean = ["AlgebraicGeometry.Scheme.Hom.steinFactorizationBase", "AlgebraicGeometry.Scheme.toSpecΓ_steinFactorizationBase"]
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $p:Y\to S=\operatorname{Spec}A$ be a morphism of schemes
[def-weil-pbc-scheme-conventions] with $A$ a commutative ring. Put
$B=H^0(Y,\mathcal O_Y)$, an $A$-algebra through $p$, and let
$q:Y\to\operatorname{Spec}B$ be the canonical morphism and
$s:\operatorname{Spec}B\to\operatorname{Spec}A$ the morphism of the algebra
structure, so that $p=s\circ q$. The factorization

$$
 Y\xrightarrow{\ q\ }\operatorname{Spec}B\xrightarrow{\ s\ }\operatorname{Spec}A
$$

is the *Stein factorization* of $p$; it is used when $p$ is proper.
