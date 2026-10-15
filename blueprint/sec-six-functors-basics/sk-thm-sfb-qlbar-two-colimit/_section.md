+++
id = "sk-thm-sfb-qlbar-two-colimit"
kind = "proposition"
title = "$\\Dctf(X,\\Qlb)$ as a $2$-colimit"
order = 1579
lean = ["AlgebraicGeometry.ProEtale.derivedExtendScalarsSubfield", "AlgebraicGeometry.ProEtale.derivedExtendScalarsToPadicAlgCl", "CategoryTheory.Mod.extendScalarsIsoOfEq", "AlgebraicGeometry.ProEtale.derivedExtendScalarsCompIso", "AlgebraicGeometry.ProEtale.PadicSubfieldConstructible", "AlgebraicGeometry.ProEtale.PadicAlgClConstructible", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalarsSubfield_obj", "AlgebraicGeometry.ProEtale.boundedConstructible_derivedExtendScalarsToPadicAlgCl_obj", "AlgebraicGeometry.ProEtale.constructibleExtendScalars", "AlgebraicGeometry.ProEtale.constructibleToPadicAlgCl", "AlgebraicGeometry.ProEtale.constructibleToPadicAlgClCompIso", "AlgebraicGeometry.ProEtale.constructibleCocone", "AlgebraicGeometry.ProEtale.constructibleCocone_homSurj", "AlgebraicGeometry.ProEtale.constructibleCocone_homInj", "AlgebraicGeometry.ProEtale.constructibleCocone_essSurjObj", "AlgebraicGeometry.ProEtale.constructibleCocone_isFilteredTwoColimit"]
uses = ["sk-def-sfb-bounded-constructible", "sk-def-sfb-filtered-two-colimit", "sk-prop-sfb-finite-extension-compatibility", "sk-lem-coefficient-finite-descent", "sk-lem-constructible-ext-continuity"]
tags = ["sketch"]
+++
For rational coefficients $\Dctf=\Dbc$; these are the bounded constructible categories
$D_{\mathrm{cons}}$ of [sk-def-sfb-bounded-constructible]. Extension of scalars identifies

$$
\Dctf(X,\Qlb)\simeq\mathop{\text{2-colim}}_{E\subset\Qlb}\Dctf(X,E)
$$

as ordinary categories (in the sense of [sk-def-sfb-filtered-two-colimit]): every object of $\Dctf(X,\Qlb)$ is
isomorphic to $K_{\Qlb}$ for some finite $E$ and some $K\in\Dctf(X,E)$, and for $K,L\in\Dctf(X,E)$ extension of
scalars induces a bijection

$$
\varinjlim_{F\supset E}\Hom_{\Dctf(X,F)}(K_F,L_F)\xrightarrow{\ \sim\ }\Hom_{\Dctf(X,\Qlb)}(K_{\Qlb},L_{\Qlb}),
$$

the colimit running over finite extensions $F$ of $E$ in $\Qlb$.
