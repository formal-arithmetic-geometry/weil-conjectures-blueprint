+++
id = "theorem-compactness-rational-coefficients--1"
kind = "theorem"
title = "Compactness with rational coefficients (1)"
name_showing = false
order = 466001
aliases = ["bp-r142-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isCompactObj_boundedConstructible_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.isCompactObj_boundedConstructible_padicAlgClRingObj"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "proposition-pro-etale-site-separably-closed--3", "lemma-constructible-sheaves--8", "definition-localizing-subcategory--1"]
+++
For $\Lambda=E$ or $\overline{\mathbf Q}_\ell$, every object of $\Dbc(X,\Lambda)$ is compact in $\Loc(\Dbc(X,\Lambda))$.
More precisely, for $C\in\Dbc(X,\Lambda)$ and every family $(K_\lambda)$
of objects of $\Dic(X,\Lambda)$, the natural map

$$
\bigoplus_\lambda\Hom(C,K_\lambda)
\longrightarrow\Hom\Bigl(C,\bigoplus_\lambda K_\lambda\Bigr)
$$

is an isomorphism.
