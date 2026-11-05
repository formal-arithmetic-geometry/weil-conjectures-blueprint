+++
kind = "proof"
of = "proposition-fourier-transform-middle-extension"
order = 1268
uses = ["proposition-etale-implications", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "proposition-fourier-inversion", "lemma-largest-punctual-subsheaf", "lemma-perverse-sheaves-curve", "lemma-simple-objects", "lemma-finite-quasi-finite-direct-images", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
