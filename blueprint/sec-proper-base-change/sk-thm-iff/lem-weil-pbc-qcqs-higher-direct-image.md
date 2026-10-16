+++
id = "lem-weil-pbc-qcqs-higher-direct-image"
kind = "lemma"
title = "Higher direct images for quasi-compact quasi-separated morphisms"
lean = ["AlgebraicGeometry.Etale.isIso_higherDirectImagePresheafToSheaf", "AlgebraicGeometry.Etale.isIso_higherDirectImagePresheafToSheaf_singleFunctor"]
order = 1103
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-etale-sum-extension", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-etale-restriction-injectives", "prop-weil-pbc-cohomology-resolution-independent", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
Let $u:U\to V$ be a quasi-compact and quasi-separated morphism
[def-weil-pbc-scheme-conventions] of schemes and let $F$ be an etale abelian
sheaf on $U$. Then for every $q\geq0$ the sheaf $R^qu_*F$ of
[def-weil-pbc-direct-image] is the sheafification of the presheaf on the
small etale site [def-weil-pbc-etale-site] of $V$

$$
 W\longmapsto H^q(W\times_VU,F|)
 \qquad(W\to V\text{ etale}),
$$

and on $\Dplus(U_{\Et})$ the derived direct image $Ru_*$ is computed in each
degree by the same description, applied to a K-injective resolution
[def-weil-pbc-kinjective-resolutions].
