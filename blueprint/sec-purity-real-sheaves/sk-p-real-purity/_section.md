+++
id = "sk-p-real-purity"
kind = "theorem"
title = "Purity of real sheaves on curves"
order = 3881
uses = ["sk-cor-walg-curve-calculus", "sk-cor-wrp-rankone-pure", "sk-d-real-detweights", "sk-d-real-weights", "sk-d-real-weil", "sk-def-wrp-real-definition", "sk-p-exterior", "sk-p-real-rankin", "sk-r-real-linear"]
lean = ["AlgebraicGeometry.WeilGroup.isPunctuallyPure_of_isConstituent_of_isReal"]
tags = ["sketch"]
+++
On a smooth geometrically connected curve over $\mathbf F_q$, every
irreducible constituent of an $\iota$-real lisse Weil sheaf
([sk-def-wrp-real-definition]) is punctually $\iota$-pure of weight equal to
its determinant weight ([sk-d-real-detweights]). In particular, every
$\iota$-real lisse Weil sheaf on the curve is mixed ([sk-d-real-weights]).
