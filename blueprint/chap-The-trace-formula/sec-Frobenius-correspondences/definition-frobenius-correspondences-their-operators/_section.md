+++
id = "definition-frobenius-correspondences-their-operators"
kind = "definition"
title = "Frobenius correspondences and their operators"
order = 952
lean = ["AlgebraicGeometry.ProEtale.stalkFrobenius", "AlgebraicGeometry.ProEtale.weilDatumIterate"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $X_0/k_0$ be separated and of finite type, and put
$X=X_0\times_{k_0}k$. Denote by $\Phi_X:X\to X$ the base change
of the $q$-power scheme Frobenius of $X_0$. It is a finite
$k$-morphism and a universal homeomorphism. A *Frobenius
correspondence* on $K$ is a morphism, not necessarily
invertible,

$$
\psi:\Phi_X^*K\longrightarrow K,
\qquad K\in D^b_{\mathrm{ctf}}(X,A).
$$

Its iterates are the morphisms

$$
\psi_m=\psi\circ\Phi_X^*\psi\circ\cdots\circ
(\Phi_X^{m-1})^*\psi:(\Phi_X^m)^*K\longrightarrow K.
$$

Let $c_m=(\operatorname{id}_X,\Phi_X^m):X\to X\times_sX$ be the graph
of $\Phi_X^m$. Since its first leg is the identity, $\psi_m$ is a
cohomological correspondence on $(X,K)$ for $c_m$. Its operator on
cohomology with compact support
(Definition [definition-action-correspondence]) is the endomorphism

$$
T_{c_m}(\psi_m)
=R\Gamma_c(X,\psi_m)\circ(\Phi_X^m)^*,
$$

where $(\Phi_X^m)^*:R\Gamma_c(X,K)\to R\Gamma_c(X,(\Phi_X^m)^*K)$ is the
pullback map induced by the unit of $(\Phi_X^m)^*\dashv R(\Phi_X^m)_*$.
For $x\in X_0(\mathbf F_{q^m})$ let $\bar x:s\to X$ be the
associated fixed point. The stalk of $\psi_m$ at $\bar x$ is an endomorphism
$\psi_{m,\bar x}:K_{\bar x}\to K_{\bar x}$.
