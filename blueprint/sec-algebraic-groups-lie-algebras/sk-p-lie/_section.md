+++
id = "sk-p-lie"
kind = "proposition"
title = "Lie algebra structure"
order = 2808
uses = ["sk-d-lie"]
lean = ["LieAlgebra.hasCentralRadical_of_isFaithful", "LieAlgebra.center_sup_derivedSeries_eq_top"]
tags = ["sketch"]
+++
A finite-dimensional Lie algebra $L$ over $k$ admitting
a faithful semisimple representation has central radical and satisfies

$$
\rad L=Z(L),\qquad L=Z(L)+[L,L].
$$

The plus sign denotes a sum of subspaces.
