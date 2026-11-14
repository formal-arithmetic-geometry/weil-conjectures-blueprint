+++
id = "lemma-fourier-transform-boundary-sequence"
kind = "lemma"
title = "Fourier transform of the boundary sequence"
order = 1276
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.hasWeightsAtMost", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.isLisse"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "definition-weights", "definition-middle-extension", "lemma-artin-schreier-character-sheaf", "proposition-fourier-transform-middle-extension", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Put $B=j_*M/j_!M$. There are sheaves $G$ and $B'$ on the dual line such
that $\operatorname{FT}_\psi(j_!M)=G$, $\operatorname{FT}_\psi(B)=B'[1]$,
and the sequence

$$
0\longrightarrow B'\longrightarrow G
\longrightarrow j'_*M'\longrightarrow0
$$

is exact. The sheaf $B'$ is lisse on the entire dual line and has weights at
most $w$.
