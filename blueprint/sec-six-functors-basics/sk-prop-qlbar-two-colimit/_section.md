+++
id = "sk-prop-qlbar-two-colimit"
kind = "proposition"
title = "$\\Dctf(X,\\Qlb)$ as a $2$-colimit"
order = 2842
lean = ["AlgebraicGeometry.ProEtale.constructibleCocone", "AlgebraicGeometry.ProEtale.constructibleCocone_homSurj", "AlgebraicGeometry.ProEtale.constructibleCocone_homInj", "AlgebraicGeometry.ProEtale.constructibleCocone_essSurjObj", "AlgebraicGeometry.ProEtale.constructibleCocone_isFilteredTwoColimit"]
uses = ["sk-def-sfb-constructible"]
tags = ["sketch"]
+++
Extension of scalars identifies

$$
\Dctf(X,\Qlb)\simeq\mathop{\text{2-colim}}_{E\subset\Qlb}\Dctf(X,E)
$$

as ordinary categories ([sk-def-sfb-constructible]). In other words, every object of $\Dctf(X,\Qlb)$ is
isomorphic to $K_{\Qlb}$ for some finite $E$ and some $K\in\Dctf(X,E)$, and for $K,L\in\Dctf(X,E)$ extension
of scalars induces a bijection

$$
\varinjlim_{F\supset E}\Hom_{\Dctf(X,F)}(K_F,L_F)\xrightarrow{\ \sim\ }\Hom_{\Dctf(X,\Qlb)}(K_{\Qlb},L_{\Qlb}),
$$

the colimit running over finite extensions $F$ of $E$ in $\Qlb$.
