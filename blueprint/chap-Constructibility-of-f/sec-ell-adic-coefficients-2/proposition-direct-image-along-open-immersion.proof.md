+++
kind = "proof"
of = "proposition-direct-image-along-open-immersion"
order = 597
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
For $\mathcal O_E$ we use the criterion of
Proposition [proposition-integral-constructibility-criterion], which
asks for derived completeness and constructible reduction. Let
$K\in\Dbc(U,\mathcal O_E)$. Since $Rj_*$ commutes with $R\varprojlim$
[Stacks, [099L](https://stacks.math.columbia.edu/tag/099L)], $Rj_*K$ is derived complete. Since $Rj_*$ also commutes with
cones, the reduction of $Rj_*K$ modulo $\pi_E$ is $Rj_*$ of the reduction
of $K$. That reduction comes from $U_{\acute{e}t}$. Its direct image is
therefore the pullback of the étale one [Stacks, [09A6](https://stacks.math.columbia.edu/tag/09A6)], which is bounded
constructible by Corollary [corollary-open-direct-image-over-field]. Both
conditions of the criterion hold, and so $Rj_*K\in\Dbc(X,\mathcal O_E)$.

For $E$ and $\overline{\mathbf Q}_\ell$ we reduce to the integral case. Since $Rj_*$ is
exact, the objects $K$ with $Rj_*K\in\Dbc$ form a triangulated
subcategory. It therefore suffices to treat the generators of
Lemma [lemma-integral-models](4). These come from integral objects by
inverting $\ell$ and by a colimit over finite extensions of $E$. Both
operations are filtered colimits of systems with a common lower bound,
and $Rj_*$ commutes with such colimits
(Corollary [corollary-continuity-cohomology]). Hence $Rj_*$ of a generator
is obtained from $Rj_*$ of an integral object by the same operations, and
it lies in $\Dbc$.
