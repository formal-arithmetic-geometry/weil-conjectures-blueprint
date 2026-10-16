+++
id = "thm-sc-theorem-of-the-base"
kind = "theorem"
title = "The theorem of the base"
lean = ["AlgebraicGeometry.exists_picardDegree_equiv_picardFunctorDegree", "AlgebraicGeometry.theorem_of_the_base", "AlgebraicGeometry.exists_abelClass_eq", "AlgebraicGeometry.smoothOfRelativeDimension_of_representableBy_picardFunctorDegree_genus", "AlgebraicGeometry.exists_surjective_of_representableBy_picardFunctorDegree_genus", "AlgebraicGeometry.isProper_of_representableBy_picardFunctorDegree_genus", "AlgebraicGeometry.isProper_of_representableBy_picardFunctorDegree", "AlgebraicGeometry.smoothOfRelativeDimension_of_representableBy_picardFunctorDegree", "AlgebraicGeometry.smoothOfRelativeDimension_of_representableBy_picardFunctor"]
order = 855
uses = ["def-pc-genus", "def-pc-geometrically-irreducible", "def-pc-smooth-projective-curve", "def-sc-picard-functor", "lem-sc-riemann-roch", "prop-pd-picard-degree-decomposition", "thm-pc-picard-representable"]
+++
Let $k$ be a separably closed field and let $C$ be a
smooth projective curve over $k$
which is geometrically integral,
of genus $g=g(C)=\dim_kH^1(C,\mathcal O_C)$ ([def-pc-genus]). Then the
Picard functor $\operatorname{Pic}_{C/k}$ of
[def-sc-picard-functor] is a disjoint union over $d\in\mathbf Z$ of smooth proper $g$-dimensional $k$-varieties
$\operatorname{Pic}^d_{C/k}$, whose $k$-points are the
degree-$d$ invertible modules, and
$\operatorname{Pic}^0_{C/k}$ is an open and closed subgroup
scheme; in particular $\operatorname{Pic}^0_{C/k}$ is a proper
smooth group scheme of dimension $g$.
