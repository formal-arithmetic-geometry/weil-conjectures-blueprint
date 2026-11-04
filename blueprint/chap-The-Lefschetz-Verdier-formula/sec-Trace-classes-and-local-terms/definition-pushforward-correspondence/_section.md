+++
id = "definition-pushforward-correspondence"
kind = "definition"
title = "Pushforward of a correspondence"
order = 923
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.pushforwardCoeffUnit", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.pushforwardCoeffCounit", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.pushforwardCoeff", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.fixMap", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.ProperPushforwardDiagram.isProper_fixMap", "AlgebraicGeometry.ProEtale.CondensedRing.BorelMooreSection.pushforward"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "lemma-proper-direct-image-unbounded-complexes", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "lemma-perfect-complexes-geometric-point", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $f:X\to Y$ and $g:C\to C'$ be proper morphisms, and let
$c'=(c'_1,c'_2):C'\to Y\times Y$ be a correspondence with $c'_ig=fc_i$ for
$i=1,2$. Put $K'=Rf_*K\in D^b_{\mathrm{ctf}}(Y,A)$. For a cohomological
correspondence $u$ on $(X,K)$, the *pushforward*
$u':c_2'^*K'\to c_1'^!K'$ of $u$ is the composite
$u'=\beta\,Rg_*u\,\alpha$, where $\alpha$ is built from the unit and counit
of $(\,)^*\dashv R(\,)_*$,

$$
\alpha:c_2'^*Rf_*K\xrightarrow{\eta_g}
Rg_*c_2^*f^*Rf_*K\xrightarrow{\varepsilon_f}Rg_*c_2^*K,
$$

and $\beta:Rg_*c_1^!K\to c_1'^!Rf_*K$ is built from the counit of
$R(\,)_!\dashv(\,)^!$: it is adjoint to

$$
Rc'_{1!}Rg_*c_1^!K\simeq Rf_*Rc_{1!}c_1^!K
\xrightarrow{Rf_*\varepsilon_{c_1}}Rf_*K.
$$

The map $g$ induces a proper morphism $h:\Fix(c)\to \Fix(c')$ of fixed loci,
and $h_*:H^0(\Fix(c),\omega_{\Fix(c)})\to H^0(\Fix(c'),\omega_{\Fix(c')})$ denotes the
map given by the ordinary unit, proper pushforward and the exceptional
counit.
