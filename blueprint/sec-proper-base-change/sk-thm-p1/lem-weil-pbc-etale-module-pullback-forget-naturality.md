+++
id = "lem-weil-pbc-etale-module-pullback-forget-naturality"
kind = "lemma"
title = "Naturality of etale module pullback under forgetting coefficients"
uses = ["def-pc-scheme", "def-weil-pbc-etale-sheaves", "def-weil-pbc-inverse-image"]
lean = ["AlgebraicGeometry.Etale.exists_upperStar_forget₂_natIso"]
order = 1734
+++
Let $X$ and $Y$ be schemes [def-pc-scheme], $f:X\to Y$ a morphism and $\Lambda$ a commutative ring. Let $f^{-1}_{\Lambda}$ be the inverse image on sheaves of $\Lambda$-modules on the small étale sites [def-weil-pbc-etale-sheaves] and $f^{-1}_{\mathrm{Ab}}$ the inverse image on abelian sheaves [def-weil-pbc-inverse-image], and let $U_X$, $U_Y$ be the functors forgetting the $\Lambda$-module structure. Then there is a natural isomorphism of functors $U_X\circ f^{-1}_{\Lambda}\cong f^{-1}_{\mathrm{Ab}}\circ U_Y$. In particular its components commute with $U_X f^{-1}_\Lambda(\alpha)$ and $f^{-1}_{\mathrm{Ab}}U_Y(\alpha)$ for every morphism $\alpha:C\to F$ of sheaves of $\Lambda$-modules on $Y_{\Et}$. No finiteness, torsion, properness or henselian hypothesis is required. (Unlike an independent choice of objectwise isomorphisms, this single isomorphism of functors supplies the commuting squares needed on cohomology.)
