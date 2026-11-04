+++
id = "theorem-poincare-duality"
kind = "theorem"
title = "Poincaré duality"
order = 850
lean = ["AlgebraicGeometry.Etale.TateOrientation.isPerfectPairing_poincarePairing", "AlgebraicGeometry.Etale.isPerfectPairing_poincarePairing_of_isSepClosed_of_isDualizable", "AlgebraicGeometry.Etale.TateOrientation.isPerfectPairing_properPoincarePairing", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerStar_coefficientDual_of_orientation", "AlgebraicGeometry.Etale.Orientation.nonempty_iso_verdierDual_coefficientDual"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "theorem-proper-base-change-classical-pro", "definition-relative-dualizing-complex", "definition-perfect-pairing", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
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
