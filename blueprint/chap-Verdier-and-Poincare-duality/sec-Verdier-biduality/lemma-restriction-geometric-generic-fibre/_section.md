+++
id = "lemma-restriction-geometric-generic-fibre"
kind = "lemma"
title = "Restriction to a geometric generic fibre"
order = 838
lean = ["AlgebraicGeometry.Etale.isIso_derivedBaseChangeMap_app_of_isOpenImmersion_of_generic", "AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_app_of_generic", "AlgebraicGeometry.Etale.isIso_derivedHomUpperStarComparison_of_generic"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "definition-exceptional-base-change-map", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
In the setting above, let $X$ be a $B$-scheme of finite type, let
$h:T\to X$ be a separated morphism of $B$-schemes of finite type, let
$i:Z\to X$ be a closed immersion, and let $L$ on $T$ and $K,M$ on $X$
be bounded constructible complexes, with $K\in D^b_{\mathrm{ctf}}(X,A)$. The three maps

$$
\begin{aligned}
g_X^*Rh_*L&\longrightarrow Rh_{\bar\eta,*}g_T^*L,\\
g_Z^*i^!M&\longrightarrow i_{\bar\eta}^!g_X^*M,\\
g_X^*\cHom_X(K,M)&\longrightarrow
\cHom_{X_{\bar\eta}}(g_X^*K,g_X^*M)
\end{aligned}
$$

defined above are isomorphisms.
