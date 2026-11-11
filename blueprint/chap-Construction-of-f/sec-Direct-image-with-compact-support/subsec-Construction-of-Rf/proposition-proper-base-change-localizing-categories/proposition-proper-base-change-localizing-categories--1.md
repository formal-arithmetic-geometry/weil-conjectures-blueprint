+++
id = "proposition-proper-base-change-localizing-categories--1"
kind = "proposition"
title = "Proper base change on the localizing categories (1)"
name_showing = false
order = 508001
aliases = ["bp-r153-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_of_localizing_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_of_localizing_padicAlgClRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_of_localizingBoundedConstructible_padicIntegersRingObj"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "proposition-pro-etale-site-separably-closed--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-pro-etale-base-change-map--1", "definition-localizing-subcategory--1"]
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
