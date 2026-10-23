+++
id = "prop-weil-pbc-reduction-to-projective-line"
kind = "theorem"
title = "Reduction of proper base change to $\\mathbf P^1$"
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_of_projectiveLine_of_isProper_of_isAddTorsion"]
order = 1966
tags = ["latex:proposition"]
uses = ["def-weil-pbc-scheme-conventions", "lemma-weil-pbc-chow-factorization", "lemma-weil-pbc-target-locality"]
+++
Let $\Lambda$ be a commutative ring which is torsion as an abelian group, and use
torsion base change over $\Lambda$ as in [lemma-weil-pbc-target-locality]. Assume
that $\mathbf P^1_S\to S$ has torsion base change over $\Lambda$ for every scheme
$S$. Then every proper morphism of schemes has torsion base change over
$\Lambda$. No finite-presentation hypothesis is needed, because the Chow
factorization [lemma-weil-pbc-chow-factorization] holds for every proper morphism
over an affine base.
