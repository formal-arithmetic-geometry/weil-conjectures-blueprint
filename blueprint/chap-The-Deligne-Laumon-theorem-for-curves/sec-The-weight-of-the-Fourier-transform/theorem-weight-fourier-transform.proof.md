+++
kind = "proof"
of = "theorem-weight-fourier-transform"
order = 1288
uses = ["proposition-etale-implications", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "lemma-additivity-open-subscheme-complement", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-function-sheaf-dictionary", "lemma-growth-finite-corrections", "theorem-weights-sums-squared-traces", "corollary-plancherel", "proposition-purity-lisse-part-fourier-transform", "lemma-finite-quasi-finite-direct-images", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $v$ be the weight of $M'$ given by
Proposition [proposition-purity-lisse-part-fourier-transform].
Shifts do not change the squared absolute values of traces, and,
if a nonzero lisse sheaf on a dense open of the line is pure of weight
$u$, then its direct image $j_*$ has $\nu=u$
(Corollary [corollary-sums-squared-traces-j-shriek]). Applying this
to $M'$ and to $M$, and using the Plancherel formula
(Corollary [corollary-plancherel]), we get

$$
v=\nu(j'_*M')
=\nu(\operatorname{FT}_\psi((j_*M)[1]))
=\nu((j_*M)[1])+1=w+1.
$$

The first equality holds because $M'$ is pure of weight $v$, the second
is the defining isomorphism of $M'$, the third is Plancherel, and the
last holds because $M$ is pure of weight $w$.
