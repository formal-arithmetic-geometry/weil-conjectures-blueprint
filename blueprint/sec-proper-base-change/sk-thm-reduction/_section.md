+++
id = "sk-thm-reduction"
kind = "theorem"
title = "Reduction to $\\Pone$"
order = 1250
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_of_projectiveLine_of_isProper"]
uses = ["sk-def-conv", "sk-def-pbc", "sk-thm-chow", "sk-thm-groth-ss", "sk-thm-iff", "sk-thm-p1"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring. Assume that $\Pone_S\to S$ satisfies
$\mathrm{PBC}$ with $\Lambda$-coefficients for every scheme $S$ (in the
sense of [sk-def-pbc]: the exchange morphism is an isomorphism, for every
base change, on every object of $\Dplus$ of $\Lambda$-module sheaves with
torsion cohomology sheaves). Then every proper morphism of schemes
satisfies $\mathrm{PBC}$ with $\Lambda$-coefficients.
