+++
id = "theorem-smooth-base-change-all-admissible"
kind = "theorem"
title = "Smooth base change for all admissible coefficients"
order = 701
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_app_padicIntegers_of_smooth", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_smooth"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-comparison-morphism-inverse-image", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "definition-pro-etale-base-change-map", "proposition-six-operations-dctf"]
+++
In (8.1), assume that all schemes are of finite type over $k$
and that $g$ is smooth. For every admissible coefficient ring

$$
\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}
$$

and every $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, the
base change map (4.5) is an isomorphism

$$
g^*Rf_*K\xrightarrow{\sim}Rf'_*g'^*K.
\tag{8.2}
$$
