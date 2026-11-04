+++
id = "proposition-compatibility-purity-composition"
kind = "proposition"
title = "Compatibility of purity with composition"
order = 800
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation_comp_openImmersion", "AlgebraicGeometry.ProEtale.CondensedRing.smoothPurityIso_comp_openImmersion"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "lemma-proper-direct-image-unbounded-complexes", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "theorem-smooth-purity-all-admissible-coefficients", "definition-relative-dualizing-complex", "corollary-dualizing-complex-smooth-scheme", "lemma-perfect-complexes-geometric-point", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
For every admissible $\Lambda$ and $K\in D^b_{\mathrm{ctf}}(Z,\Lambda)$,
the map $\gamma_{g\circ f}(K)$ of (9.2) is the composite

$$
\begin{aligned}
(g\circ f)^{*}K(d+e)[2d+2e]
&\simeq f^{*}\bigl(g^{*}K(e)[2e]\bigr)(d)[2d]\\
&\xrightarrow{\ f^{*}(\gamma_g(K))(d)[2d]\ }
f^{*}\bigl(g^!K\bigr)(d)[2d]\\
&\xrightarrow{\ \gamma_f(g^!K)\ }
f^!g^!K
\simeq(g\circ f)^!K
\end{aligned}
$$

in $D^b_{\mathrm{ctf}}(X,\Lambda)$, where the coefficient $\Lambda$ is omitted
from the displayed composite.
