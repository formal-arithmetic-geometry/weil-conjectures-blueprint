+++
id = "theorem-compactness-rational-coefficients"
kind = "theorem"
title = "Compactness with rational coefficients"
order = 466
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isCompactObj_boundedConstructible_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.isCompactObj_boundedConstructible_padicAlgClRingObj"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "lemma-constructible-sheaves", "definition-localizing-subcategory"]
+++
For $\Lambda=E$ or $\overline{\mathbf Q}_\ell$, every object of [$\Dbc(X,\Lambda)$](@definition-constructible-sheaves) is compact in [$\Loc(\Dbc(X,\Lambda))$](@definition-localizing-subcategory).
More precisely, for $C\in\Dbc(X,\Lambda)$ and every family $(K_\lambda)$
of objects of [$\Dic(X,\Lambda)$](@corollary-ambient-ind-derived), the natural map

$$
\bigoplus_\lambda\Hom(C,K_\lambda)
\longrightarrow\Hom\Bigl(C,\bigoplus_\lambda K_\lambda\Bigr)
$$

is an isomorphism.
