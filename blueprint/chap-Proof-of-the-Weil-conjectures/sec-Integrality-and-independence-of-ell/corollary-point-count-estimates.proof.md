+++
kind = "proof"
of = "corollary-point-count-estimates"
order = 1398
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "proposition-exceptional-inverse-image-smooth-morphism", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-relative-dualizing-complex", "theorem-trace-isomorphism-top-degree", "corollary-cup-product-pairing", "lemma-additivity-open-subscheme-complement", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-function-sheaf-dictionary", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "lemma-finite-quasi-finite-direct-images", "theorem-pure-lisse-sheaves-over-relative", "lemma-hankel-rank-rationality", "theorem-weil-conjectures-smooth-proper-schemes", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Since $X_0$ is proper, the point-counting formula of
Corollary [corollary-point-counting-zeta-function] reads

$$
\#X_0(\mathbf F_{q^m})
=\sum_{i=0}^{2d}(-1)^i\operatorname{Tr}(F^m\mid H^i_\ell).
$$

The terms in degrees $0$ and $2d$ are $1$ and $q^{dm}$ by
Theorem [theorem-weil-conjectures-smooth-proper-schemes](3). The
left side of the estimate is therefore the absolute value of the sum of
the remaining terms. In degree $i$, the trace is a sum of $b_i$
eigenvalues of $F^m$, each of complex modulus $q^{mi/2}$ by
Theorem [theorem-weil-conjectures-smooth-proper-schemes](2). Its
absolute value is thus at most $b_iq^{mi/2}$, and the triangle
inequality proves the first bound. For a curve, $b_1=2g$ by the
cohomology calculation of Appendix [chap-Cohomology-of-torsion-sheaves-on-curves].
