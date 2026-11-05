+++
id = "corollary-point-counting-zeta-function"
kind = "corollary"
title = "Point counting and the zeta function"
order = 1040
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.weilPointCount"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "definition-weil-structure", "definition-trace-function", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Give $\Lambda_X$ the Weil structure of constant sheaves defined after
Definition [definition-weil-structure]. For every coefficient
ring $\Lambda$ of Theorem [theorem-grothendieck-lefschetz-trace-formula] and every $m\geq1$ we have

$$
\operatorname{tr}_{\Lambda}
(\operatorname{Frob}_{X,\Lambda_X}^m\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},\Lambda_X))
=\#X_0(\mathbf F_{q^m})\cdot1_{\Lambda}.
\tag{12.9}
$$

For $\Lambda=\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell$, this gives

$$
\#X_0(\mathbf F_{q^m})
=\sum_i(-1)^i\operatorname{Tr}
(\operatorname{Frob}_{X,\Lambda_X}^m\mid H_c^i(X_{\mathrm{pro}\acute{e}t},\Lambda_X)),
$$

and

$$
\begin{aligned}
Z(X_0,T)
&:=\exp\left(\sum_{m\geq1}
\#X_0(\mathbf F_{q^m})\frac{T^m}{m}\right)\\
&=\prod_{x\in|X_0|}(1-T^{\deg(x)})^{-1}
=\prod_i\det(1-T\operatorname{Frob}_{X,\Lambda_X}\mid H_c^i(X_{\mathrm{pro}\acute{e}t},\Lambda_X))^{(-1)^{i+1}}.
\end{aligned}
$$

The first two series lie in $1+T\mathbf Z[[T]]$, and the last equality
holds in $\Lambda[[T]]$. Moreover, $Z(X_0,T)$ belongs to
$\mathbf Q(T)$.
