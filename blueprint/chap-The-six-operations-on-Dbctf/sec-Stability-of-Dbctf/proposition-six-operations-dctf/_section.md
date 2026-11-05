+++
id = "proposition-six-operations-dctf"
kind = "proposition"
title = "The six operations on $\\Dctf$"
order = 625
lean = ["AlgebraicGeometry.Etale.boundedConstructible_preservation", "AlgebraicGeometry.Etale.constructibleFiniteTor_preservation", "AlgebraicGeometry.ProEtale.DerivedCategory.constructibleFiniteTor_derivedHom_mapDerivedCategory"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "proposition-composition-open-restriction-compactifications-f", "definition-relative-dualizing-complex"]
+++
For every admissible $\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}$, the
operations $f^*$, $Rf_*$, $Rf_!$, $f^!$, $\otimes^{\mathbf L}$ and
$\cHom$ preserve $D^b_{\mathrm{ctf}}(-,\Lambda)$ for morphisms of schemes of finite
type over $k$. Their adjunctions are the restrictions of the adjunctions
$f^*\dashv Rf_*$ and $-\otimes^{\mathbf L}K\dashv\cHom(K,-)$ on
$D(-_{\mathrm{pro}\acute{e}t},\Lambda)$ or of the adjunction $Rf_!\dashv f^!$ on
$\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$.
