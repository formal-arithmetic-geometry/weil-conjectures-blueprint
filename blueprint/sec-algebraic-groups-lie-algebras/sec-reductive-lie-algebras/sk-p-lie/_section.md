+++
id = "sk-p-lie"
kind = "proposition"
title = "Lie algebras with a faithful semisimple representation"
order = 1000
lean = ["LieAlgebra.hasCentralRadical_of_isFaithful", "LieAlgebra.center_sup_derivedSeries_eq_top"]
uses = ["sk-i-cartier", "sk-lem-walg-killing", "sk-lem-walg-lie-eigenvector", "sk-p-comparison"]
tags = ["sketch"]
+++
If $\mathfrak l$ has a faithful semisimple representation, then

$$
\operatorname{rad}\mathfrak l=Z(\mathfrak l),
\qquad
\mathfrak l=Z(\mathfrak l)+[\mathfrak l,\mathfrak l].
$$
