+++
id = "proposition-proper-base-change-localizing-categories"
kind = "proposition"
title = "Proper base change on the localizing categories"
order = 508
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_of_localizing_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_of_localizing_padicAlgClRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_of_localizingBoundedConstructible_padicIntegersRingObj"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "definition-pro-etale-base-change-map", "definition-localizing-subcategory"]
+++
Let $\Lambda$ be admissible. Consider a cartesian square

$$
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
\downarrow p'&&\downarrow p\\
Y'&\xrightarrow{g}&Y
\end{array}
$$

with $p$ proper. The base change map $g^*Rp_*K\to Rp'_*g'^*K$ is an isomorphism for every
$K\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$.
