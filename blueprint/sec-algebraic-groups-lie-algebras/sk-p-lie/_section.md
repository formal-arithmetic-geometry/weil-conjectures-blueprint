+++
id = "sk-p-lie"
kind = "proposition"
title = "Lie algebras with a faithful semisimple representation"
lean = ["LieAlgebra.hasCentralRadical_of_isFaithful", "LieAlgebra.center_sup_derivedSeries_eq_top"]
order = 3920
uses = ["sk-i-cartier", "sk-lem-walg-killing", "sk-lem-walg-lie-eigenvector", "sk-p-comparison"]
tags = ["sketch"]
+++
The sum of two solvable ideals of a Lie algebra is solvable, because its
quotient by one of them is a quotient of the other, and an extension of
solvable Lie algebras is solvable. Hence the radical
$\rad\mathfrak l$, the sum of all solvable ideals of $\mathfrak l$, is a
finite sum and a solvable ideal.

If $\mathfrak l$ has a faithful semisimple representation, then

$$
\rad\mathfrak l=Z(\mathfrak l),
\qquad
\mathfrak l=Z(\mathfrak l)+[\mathfrak l,\mathfrak l].
$$
