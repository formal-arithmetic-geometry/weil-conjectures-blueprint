+++
id = "corollary-degreewise-duality-over-fields"
kind = "corollary"
title = "Degreewise duality over fields"
order = 859
lean = ["AlgebraicGeometry.Etale.TateOrientation.isPerfPair_degreewisePoincarePairing", "AlgebraicGeometry.Etale.TateOrientation.isPerfPair_degreewisePoincarePairing_of_isProper", "AlgebraicGeometry.WeilSheaf.exists_isPerfPair_compactlySupportedCohomology_dual", "AlgebraicGeometry.WeilSheaf.exists_isPerfPair_compactlySupportedCohomology_adicConstant", "AlgebraicGeometry.WeilSheaf.poincareDuality_compactlySupportedCohomology_adicConstant"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $X/k$ be smooth and separated of pure dimension $d$, with $k$
algebraically closed, let $\Lambda$ be a field (a finite coefficient
field, $\mathbf Q_\ell$, $E$ or $\overline{\mathbf Q}_\ell$), let $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, and put
$K^\vee=\cHom_X(K,\Lambda_X)$. For every $i$ the pairings induced by
$\beta_K$,

$$
H_c^i(X,K)\times H^{2d-i}(X,K^\vee(d))\longrightarrow\Lambda,
\qquad
H_c^i(X,K)\times H^{2d-i}(X,K^\vee)\longrightarrow\Lambda(-d),
$$

are perfect pairings of finite-dimensional vector spaces. If $X$ is
proper, the same holds with $H_c^i$ replaced by $H^i$.
