+++
id = "prop-weil-pbc-projective-line"
kind = "theorem"
title = "Projective-line proper base change"
order = 1597
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_projectiveLine", "AlgebraicGeometry.Etale.hasInjectiveAcyclicity_projectiveLine"]
tags = ["latex:proposition"]
uses = ["def-weil-pbc-injective-acyclicity-property", "def-weil-pbc-property", "lemma-weil-pbc-p1-exchange-geometric-stalk", "lemma-weil-pbc-property-iff-acyclicity", "prop-weil-pbc-proper-curve-sepclosed-invariance"]
+++
Let $\Lambda$ be a commutative ring, let $S$ be a scheme and let
$p:\mathbf P^1_S\to S$ be the projection. For every morphism $g:T\to S$, with
$p':\mathbf P^1_T\to T$ and $g':\mathbf P^1_T\to\mathbf P^1_S$ the other two
sides of the cartesian square, the following hold.

1. For every $K\in\Dplus(\mathbf P^1_{S,\Et},\Lambda)$ all of whose
   cohomology sheaves are torsion (every geometric stalk is a torsion abelian
   group), the derived exchange morphism
   $g^{-1}Rp_*K\to Rp'_*g'^{-1}K$ of [def-weil-pbc-property] is an
   isomorphism.
2. For every injective sheaf $I$ of $\Lambda$-modules on
   $\mathbf P^1_{S,\Et}$ which is torsion,
   $R^qp'_*g'^{-1}I=0$ for all $q>0$.
