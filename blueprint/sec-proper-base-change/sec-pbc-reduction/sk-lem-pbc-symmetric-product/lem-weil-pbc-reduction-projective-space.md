+++
id = "lem-weil-pbc-reduction-projective-space"
kind = "lemma"
title = "Reduction of projective space to products of lines"
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_projectiveSpace"]
order = 2058
uses = ["def-weil-pbc-symmetric-product-morphism", "lem-weil-pbc-symmetric-product-finite", "lem-weil-pbc-symmetric-product-surjective", "lemma-weil-pbc-cancellation", "prop-weil-pbc-composition-stability", "prop-weil-pbc-finite-morphism"]
+++
Let $\Lambda$ be a commutative ring which is torsion as an abelian group, and use
torsion base change over $\Lambda$ as in [lemma-weil-pbc-cancellation]. Assume that
for every scheme $S$ the projection $\mathbf P^1_S\to S$ has torsion base change
over $\Lambda$. Then for every scheme $T$ and every $n\geq0$ the projection
$\mathbf P^n_T\to T$ has torsion base change over $\Lambda$.
