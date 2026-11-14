+++
id = "theorem-poincare-duality"
kind = "theorem"
title = "Poincaré duality"
order = 857
lean = ["AlgebraicGeometry.Etale.TateOrientation.isPerfectPairing_poincarePairing", "AlgebraicGeometry.Etale.isPerfectPairing_poincarePairing_of_isSepClosed_of_isDualizable", "AlgebraicGeometry.Etale.TateOrientation.isPerfectPairing_properPoincarePairing", "AlgebraicGeometry.Etale.Orientation.nonempty_iso_verdierDual_coefficientDual"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "theorem-proper-base-change-classical-pro", "lemma-inverse-image-tensor-product", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "lemma-smooth-morphisms-locally-constant-sheaves", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "theorem-sp-qbar", "definition-trace-map", "definition-verdier-dual-evaluation", "definition-perfect-pairing", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
+++
Let $X/k$ be smooth, separated of pure dimension $d$, with
$k$ algebraically closed. For every admissible $\Lambda$ and
$K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, Theorem [theorem-smooth-purity-all-admissible-coefficients] gives isomorphisms

$$
\omega_X\simeq\Lambda_X(d)[2d],\qquad
\mathbb D_XK\simeq
\cHom_X(K,\Lambda_X)(d)[2d].
$$

Put $K^\vee=\cHom_X(K,\Lambda_X)$. If $K$ is locally perfect over
$\Lambda_X$, then so is $K^\vee$, and it is the ordinary dual. Let $\operatorname{Tr}_X$ be the map induced on $R\Gamma_c$ by
the trace map of $a_X$ (Definition [definition-trace-map]). The
pairing

$$
\begin{split}
\beta_K:\quad
R\Gamma_c(X,K)\otimes^{\mathbf L}
R\Gamma(X,K^\vee(d))[2d]
&\longrightarrow R\Gamma_c(X,\Lambda_X(d))[2d]\\
&\xrightarrow{\operatorname{Tr}_X}\Lambda
\end{split}
\tag{10.7}
$$

is perfect, and its adjoint is the canonical isomorphism

$$
R\Gamma(X,K^\vee(d))[2d]
\xrightarrow{\sim}
R\!\operatorname{Hom}_\Lambda(R\Gamma_c(X,K),\Lambda).
\tag{10.8}
$$

If $X$ is proper, $R\Gamma_c$ may be replaced by
$R\Gamma$. For a map $\Lambda\to\Lambda'$ of admissible coefficient
rings, the change-of-coefficients isomorphisms of
Proposition [proposition-six-operations-change-coefficients] for
$R\Gamma_c$, $R\Gamma$ and $\cHom$ carry
$\beta_K\otimes^{\mathbf L}_\Lambda\Lambda'$ to $\beta_{K_{\Lambda'}}$,
where $K_{\Lambda'}=K\otimes^{\mathbf L}_\Lambda\Lambda'$.
