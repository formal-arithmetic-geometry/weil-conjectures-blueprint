+++
id = "lemma-weil-pbc-property-iff-acyclicity"
kind = "lemma"
title = "Equivalence of PBC and IA"
lean = ["AlgebraicGeometry.Etale.HasTorsionBaseChange.quotient", "AlgebraicGeometry.Etale.HasTorsionBaseChange.hasInjectiveAcyclicity", "AlgebraicGeometry.Etale.HasInjectiveAcyclicity.hasTorsionBaseChange_of_isIso_baseChangeMap", "AlgebraicGeometry.Etale.HasInjectiveAcyclicity.hasTorsionBaseChange", "AlgebraicGeometry.Etale.hasTorsionBaseChange_of_hasInjectiveAcyclicity"]
order = 1549
uses = ["def-weil-pbc-derived-exchange", "def-weil-pbc-injective-acyclicity-property", "def-weil-pbc-property", "def-weil-pbc-scheme-conventions", "def-weil-pbc-cartesian-square", "def-weil-pbc-torsion-etale-sheaf"]
+++
For a proper morphism [def-weil-pbc-scheme-conventions] $f$, the following
conditions are equivalent.

1. $\mathrm{PBC}(f)$ holds for torsion coefficients: for every cartesian square
   [def-weil-pbc-cartesian-square] over $f$ and every
   $K\in\Dplus(X_{\Et})$ of abelian sheaves whose cohomology sheaves are torsion
   [def-weil-pbc-torsion-etale-sheaf], the derived exchange morphism
   $\Ex_{\square,K}$ [def-weil-pbc-derived-exchange] is an isomorphism (the
   property of [def-weil-pbc-property] restricted to objects with torsion
   cohomology).
2. $\mathrm{IA}_r(f)$ holds for every prime $r$ in the sense of
   [def-weil-pbc-injective-acyclicity-property].
