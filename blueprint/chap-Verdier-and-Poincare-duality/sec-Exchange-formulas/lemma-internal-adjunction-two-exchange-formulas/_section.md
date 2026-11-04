+++
id = "lemma-internal-adjunction-two-exchange-formulas"
kind = "lemma"
title = "Internal adjunction and two exchange formulas"
order = 823
lean = ["AlgebraicGeometry.Etale.derivedHomRightDerivedLowerShriekIsoOfFinite", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_verdierExchange", "AlgebraicGeometry.Etale.nonempty_verdierDual_rightDerivedLowerShriek_natIso", "AlgebraicGeometry.Etale.nonempty_iso_verdierDual_leftDerivedUpperStar", "AlgebraicGeometry.Etale.nonempty_arrowIso_rightDerivedLowerStar_map_verdierDualDoubleDual"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-relative-dualizing-complex", "definition-verdier-dual-evaluation", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
Let $f:X\to Y$ be a morphism, $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and
$L\in D^b_{\mathrm{ctf}}(Y,\Lambda)$. The map
(10.1) and the two maps derived from it
and defined above are isomorphisms

$$
\begin{align}
\cHom_Y(Rf_!K,L)&\simeq
Rf_*\cHom_X(K,f^!L),\tag{10.2}\\
\mathbb D_YRf_!K&\simeq Rf_*\mathbb D_XK,
\tag{10.3}\\
f^!\mathbb D_YL&\simeq\mathbb D_Xf^*L.
\tag{10.4}\end{align}
$$

If $f$ is proper, then the composite

$$
Rf_*K\xrightarrow{Rf_*\delta_K}Rf_*\mathbb D_X\mathbb D_XK
\simeq\mathbb D_YRf_*\mathbb D_XK
$$

of $Rf_*\delta_K$ and (10.3) for $\mathbb D_XK$
equals the composite

$$
Rf_*K\xrightarrow{\delta_{Rf_*K}}\mathbb D_Y\mathbb D_YRf_*K
\simeq\mathbb D_YRf_*\mathbb D_XK
$$

of $\delta_{Rf_*K}$ and $\mathbb D_Y$ applied to
(10.3) for $K$.
