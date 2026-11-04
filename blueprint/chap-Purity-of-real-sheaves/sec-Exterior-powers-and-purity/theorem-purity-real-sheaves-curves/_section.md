+++
id = "theorem-purity-real-sheaves-curves"
kind = "theorem"
title = "Purity of real sheaves on curves"
order = 1160
lean = ["AlgebraicGeometry.WeilGroup.isPunctuallyPure_of_isConstituent_of_isReal", "AlgebraicGeometry.WeilSheaf.IsReal.exists_isPunctuallyPureOfWeight_cokernel_detWeight"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-weights", "definition-determinant-weight", "definition-weil-representation", "definition-real-sheaves"]
+++
On a smooth geometrically connected curve over $\mathbf F_q$, every
irreducible constituent of an $\iota$-real lisse Weil sheaf is
punctually $\iota$-pure of weight equal to its determinant weight.
In particular, every $\iota$-real lisse Weil sheaf on the curve is mixed.
