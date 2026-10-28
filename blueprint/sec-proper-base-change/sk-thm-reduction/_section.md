+++
id = "sk-thm-reduction"
kind = "proposition"
title = "Proper base change on the étale site"
order = 2059
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_of_projectiveLine_of_isProper_of_isAddTorsion"]
uses = ["sk-def-conv", "sk-def-pbc", "sk-thm-chow-projective", "sec-nagata-compactification", "sk-thm-picard-perfect", "sk-thm-iff", "sk-thm-p1", "sk-lem-pbc-finite", "sk-lem-pbc-symmetric-product", "sk-lem-pbc-composition-cancellation"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring which is torsion as an abelian group. If
$\mathrm{PBC}_\Lambda(\mathbf P^1_S\to S)$ [sk-def-pbc] holds for every scheme
$S$, then $\mathrm{PBC}_\Lambda(f)$ holds for every proper morphism of schemes
$f$.
