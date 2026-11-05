+++
id = "proposition-six-operations-dctf"
kind = "proposition"
title = "The six operations on $\\Dctf$"
order = 624
lean = ["AlgebraicGeometry.Etale.boundedConstructible_preservation", "AlgebraicGeometry.Etale.constructibleFiniteTor_preservation", "AlgebraicGeometry.ProEtale.DerivedCategory.constructibleFiniteTor_derivedHom_mapDerivedCategory"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
For every admissible $\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}$, the
operations $f^*$, $Rf_*$, $Rf_!$, $f^!$, $\otimes^{\mathbf L}$ and
$\cHom$ preserve $D^b_{\mathrm{ctf}}(-,\Lambda)$ for morphisms of schemes of finite
type over $k$. Their adjunctions are the restrictions of the adjunctions
$f^*\dashv Rf_*$ and $-\otimes^{\mathbf L}K\dashv\cHom(K,-)$ on
$D(-_{\mathrm{pro}\acute{e}t},\Lambda)$ or of the adjunction $Rf_!\dashv f^!$ on
$\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$.
