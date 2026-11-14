+++
id = "proposition-six-operations-dctf"
kind = "proposition"
title = "The six operations on $\\Dctf$"
order = 625
lean = ["AlgebraicGeometry.Etale.constructibleFiniteTor_preservation", "AlgebraicGeometry.ProEtale.DerivedCategory.constructibleFiniteTor_derivedHom_mapDerivedCategory"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-comparison-morphism-inverse-image", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "lemma-inverse-image-tensor-product", "proposition-composition-open-restriction-compactifications-f", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
For every admissible $\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}$, the
operations $f^*$, $Rf_*$, $Rf_!$, $f^!$, $\otimes^{\mathbf L}$ and
$\cHom$ preserve $D^b_{\mathrm{ctf}}(-,\Lambda)$ for morphisms of schemes of finite
type over $k$. Their adjunctions are the restrictions of the adjunctions
$f^*\dashv Rf_*$ and $-\otimes^{\mathbf L}K\dashv\cHom(K,-)$ on
$D(-_{\mathrm{pro}\acute{e}t},\Lambda)$ or of the adjunction $Rf_!\dashv f^!$ on
$\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$.
