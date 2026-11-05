+++
id = "proposition-compatibility-purity-composition"
kind = "proposition"
title = "Compatibility of purity with composition"
order = 801
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation_comp_openImmersion", "AlgebraicGeometry.ProEtale.CondensedRing.smoothPurityIso_comp_openImmersion"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "theorem-smooth-purity-all-admissible-coefficients", "definition-relative-dualizing-complex", "corollary-dualizing-complex-smooth-scheme", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
