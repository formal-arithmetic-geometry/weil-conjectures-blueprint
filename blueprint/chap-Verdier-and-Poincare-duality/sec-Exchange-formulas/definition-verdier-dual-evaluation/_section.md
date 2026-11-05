+++
id = "definition-verdier-dual-evaluation"
kind = "definition"
title = "Verdier dual and evaluation"
order = 828
lean = ["AlgebraicGeometry.ProEtale.dualizingComplex", "AlgebraicGeometry.ProEtale.verdierDual", "AlgebraicGeometry.ProEtale.CondensedRing.dualizingComplex"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-comparison-morphism-inverse-image", "proposition-pro-etale-site-separably-closed", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-composition-open-restriction-compactifications-f", "proposition-six-operations-change-coefficients", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
The *dualizing complex* and the *Verdier dual* are

$$
\omega_X=a_X^!\Lambda_s,\qquad
\mathbb D_XK=\cHom_{\Lambda_X}(K,\omega_X).
$$

Thus $\mathbb D_X:D(X_{\mathrm{pro}\acute{e}t},\Lambda)^{\mathrm{op}}\to
D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is an exact functor. The *double-dual
morphism*

$$
\delta_K:K\longrightarrow\mathbb D_X\mathbb D_XK
$$

is the tensor–Hom adjoint of the composite
$K\otimes^{\mathbf L}\mathbb D_XK\simeq\mathbb D_XK\otimes^{\mathbf L}K
\to\omega_X$ of the symmetry isomorphism, with its Koszul sign, and
evaluation.
