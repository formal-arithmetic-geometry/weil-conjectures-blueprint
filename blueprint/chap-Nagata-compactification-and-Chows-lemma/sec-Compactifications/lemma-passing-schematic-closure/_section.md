+++
id = "lemma-passing-schematic-closure"
kind = "lemma"
title = "Passing to the schematic closure"
order = 1415
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleLowerShriekRefinementIso", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekRefinementIso", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward_padicAlgCl"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $X\xrightarrow{j}\overline X\xrightarrow{p}S$ be any
compactification with $\overline X$ Noetherian, and let
$i:Z\hookrightarrow\overline X$ be the
schematic closure of $X$, with $j_Z:X\hookrightarrow Z$ the induced
open immersion. For a condensed coefficient ring $\Lambda$, we use the
pullbacks of its coefficient sheaf to these schemes as coefficients. For every
$K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda_X)$ there are canonical identifications

$$
j_!K\simeq i_*j_{Z,!}K,\qquad
Rp_*j_!K\simeq R(p\circ i)_*j_{Z,!}K.
$$
