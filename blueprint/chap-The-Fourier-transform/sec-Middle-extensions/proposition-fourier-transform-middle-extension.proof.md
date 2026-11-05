+++
kind = "proof"
of = "proposition-fourier-transform-middle-extension"
order = 1268
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-fourier-inversion", "definition-perverse-sheaves-curve", "lemma-perverse-sheaves-curve", "lemma-simple-objects", "proposition-fourier-transform-perverse-heart", "lemma-finite-quasi-finite-direct-images", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
By Fourier inversion, a punctual transform would force every geometric
constituent of $M$ to be a linear character sheaf, and the hypothesis
excludes this.

By Proposition [proposition-fourier-transform-perverse-heart], the transform of the simple
object $(j_*M)[1]$ is simple, and so by
Lemma [lemma-simple-objects] it is either punctual or of the
displayed form. Restricting the kernel to $\{a\}\times\mathbf A^1$
shows that the inverse transform of a geometric skyscraper at $a$ is
$\mathcal L_{\psi(-ax)}(1)[1]$. Now, if the transform were punctual, it
would geometrically be an iterated extension of skyscrapers at
finitely many points $a$, so by Fourier inversion and exactness
$(j_*M)[1]$ would be geometrically an iterated extension of the
objects $\mathcal L_{\psi(-ax)}(1)[1]$. Restricting to $U$, we see
that every geometric constituent of $M$ would be one of these linear
characters, which the hypothesis excludes. Finally, the open $U'_0$ and
the sheaf $M'$ are defined over $k_0$, since we may choose a
Weil-stable open on which the constructible transform is lisse.
