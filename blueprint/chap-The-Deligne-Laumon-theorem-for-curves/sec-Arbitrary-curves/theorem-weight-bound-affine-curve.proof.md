+++
kind = "proof"
of = "theorem-weight-bound-affine-curve"
order = 1316
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "theorem-grothendieck-lefschetz-trace-formula", "theorem-trace-formula-euler-product", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "lemma-degree-zero-top-cohomology", "lemma-boundary-stalk", "lemma-point-count-bound", "lemma-extreme-degrees-affine-curve", "lemma-cohomological-range-curve", "lemma-unramified-at-infinity-no-linear-characters", "corollary-h-1-c-stalk-fourier", "proposition-exactness-fixed-pure-weight", "lemma-finite-quasi-finite-direct-images", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
We push the sheaf forward to the line and realize $H^1_c$ as a
quotient of a group bounded by
Theorem [theorem-weight-bound-affine-line]. This uses two
surjections: one removes the points where the direct image fails
to be lisse and pure, and the other moves a lisse point to infinity.

Choose $\pi$ as in
Lemma [lemma-finite-generically-etale-map-line] and put $K=\pi_*j_!F$. Let $W_0$ be the dense
open on which $K$ is lisse and pure. Since its complement is finite,
localization gives

$$
H_c^1(W,K|_W)\twoheadrightarrow
H_c^1(\mathbf A^1,K)=H_c^1(C,F).
$$

By Lemma [lemma-finite-extension-base-field-moving], after a finite extension of
the constant field there is a further surjection from $H_c^1(V,G)$
onto $H_c^1(W,K|_W)$, with $G$ pure of weight $w$ and unramified at
infinity. Let $v:V\hookrightarrow\mathbf A^1$ be the inclusion and
$i:Z\hookrightarrow\mathbf A^1$ its finite complement. The
localization sequence for $v_*G$ reads

$$
H_c^0(Z,i^*v_*G)\longrightarrow H_c^1(V,G)
\longrightarrow H_c^1(\mathbf A^1,v_*G)\longrightarrow0.
$$

The first group has weights at most $w$. Indeed, the stalks of
$i^*v_*G$ at the closed points of $Z_0$ have weights at most $w$ by
Proposition [proposition-weights-j-boundary-points], and
$H_c^0(Z,i^*v_*G)$ is the direct sum, over the closed points $z$ of $Z_0$,
of the stalks at the $e=[\kappa(z):k_m]$ geometric points over $z$, where
$k_m$ is the constant field of $V_0$. The geometric Frobenius of $k_m$
permutes these $e$ stalks cyclically, and its $e$th power on each of them
is conjugate to the local Frobenius $F_z$. An eigenvalue $\beta$ on such a
cycle therefore satisfies $\beta^e=\alpha$ for an eigenvalue $\alpha$ of
$F_z$, so that $|\iota\beta|^e=|\iota\alpha|\le q_z^{w/2}=(q^m)^{ew/2}$,
and $|\iota\beta|\le(q^m)^{w/2}$, which is weight at most $w$ over $k_m$.
This is the case of the finite map $Z_0\to\operatorname{Spec}k_m$ in
Lemma [lemma-finite-quasi-finite-direct-images], whose proof is the same
computation. The last group has weights at most $w+1$ by
Theorem [theorem-weight-bound-affine-line]. As an extension of a
subgroup of the last by a quotient of the first, the middle group therefore has
weights at most $w+1$. This bound passes to quotients under the two
surjections, and by Lemma [lemma-weight-bound-constant-extension] it holds over
the original constant field.
