+++
id = "corollary-open-direct-image-over-field"
kind = "corollary"
title = "Open direct image over a field"
order = 585
lean = ["AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion", "AlgebraicGeometry.Etale.isIso_baseChange_app_of_isOpenImmersion_of_field", "AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_isOpenImmersion_of_field"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-derived-base-change-map", "definition-pro-etale-base-change-map"]
+++
Let $j:X\hookrightarrow Y$ be an open immersion. Then

$$
Rj_*:\Dbc(X,A)\longrightarrow\Dbc(Y,A),
\tag{6.22}
$$

and for every $k$-scheme $T$ of finite type, with projections
$g_X:X_T\to X$ and $g_Y:Y_T\to Y$, and every $K\in\Dbc(X,A)$, the base
change map $g_Y^*Rj_*K\to Rj_{T,*}g_X^*K$ is an isomorphism.
