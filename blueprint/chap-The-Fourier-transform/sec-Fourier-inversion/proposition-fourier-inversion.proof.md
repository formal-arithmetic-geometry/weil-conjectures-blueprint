+++
kind = "proof"
of = "proposition-fourier-inversion"
order = 1235
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "lemma-integral-linear-character", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
The composite of two transforms is again an integral
transform, and we compute its kernel. It will turn out to be the
constant sheaf on the diagonal, twisted by $(-r)$, which up to this twist
is the kernel of the identity functor. Let $r_{ij}$ be the projections of
$V\times_SV^\vee\times_SV$ onto pairs of factors. By base change and
the projection formula, the composite of two transforms is the
transform with the convolution kernel

$$
Rr_{13!}(r_{12}^*\mathcal K_\psi\otimes
r_{23}^*\mathcal K_{\psi^{-1}})[2r].
$$

At a point $(x,z)$, the unshifted integral over the middle factor is
the cohomology of the character sheaf attached to
$y\mapsto\psi\langle x-z,y\rangle$, and hence it vanishes for $x\ne z$
by Lemma [lemma-integral-linear-character]. Thus the unshifted convolution
is supported on the diagonal, so the localization triangle identifies
it canonically with the direct image of its restriction to the
diagonal. There the unit trivialization of the character sheaf and
the trace map for the vector bundle identify the restriction with
$E(-r)[-2r]$. Since the shift $[2r]$ cancels $[-2r]$, we obtain the first
inversion formula. If instead the two kernels use the same character, then
$x-z$ is replaced by $x+z$, the support is the antidiagonal, and we
obtain the second formula. Since the traces and unit trivializations
used here are defined over $k_0$, these isomorphisms commute with the
Weil structures.
