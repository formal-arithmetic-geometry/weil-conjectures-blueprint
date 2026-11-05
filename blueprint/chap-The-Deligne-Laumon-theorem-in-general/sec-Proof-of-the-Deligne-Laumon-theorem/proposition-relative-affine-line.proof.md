+++
kind = "proof"
of = "proposition-relative-affine-line"
order = 1358
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "lemma-finite-quasi-finite-direct-images", "theorem-pure-lisse-sheaves-over-relative", "lemma-weights-exact-sequence", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
We stratify the target so that over each stratum, $G$ is lisse off a
subscheme that is finite over the base. On the lisse part the
projection is a relative affine curve, and we apply
Theorem [theorem-pure-lisse-sheaves-over-relative]. On the finite
part it is quasi-finite, and we apply
Lemma [lemma-finite-quasi-finite-direct-images].

Take a finite mixed filtration of $G$. In the long exact
sequences of $R^ip_!$ for its steps, the bound $w+i$ passes from the
pure quotients to $G$ by Lemma [lemma-weights-exact-sequence]. We
may therefore assume that $G$ is pure and constructible of weight
$v\leq w$.

Suppose first that the target $Y_0=\operatorname{Spec}R$ is integral
and affine, so that $\mathbf A^1_{Y_0}$ is integral. We construct the
strata as follows. Choose a dense open $U$ on which $G$ is lisse. Since the
locus where $G$ is lisse is stable under Frobenius, we may replace
$U$ by the intersection of its finitely many Frobenius conjugates. Then
$U$ is defined over $k_0$, and so are the ideal $I\subset R[T]$ of its
reduced complement and the choices below. If the complement is
nonempty, choose a nonzero $g\in I$ and invert its nonzero leading
coefficient $b$. Then over $R_b$ the polynomial $b^{-1}g$ is monic and
vanishes in $R_b[T]/I$. Hence the image of $T$ is integral over $R_b$,
and $R_b[T]/I$ is generated as an $R_b$-module by the powers $T^k$ with
$k<\deg g$. In particular $R_b[T]/I$ is finite over $R_b$; if $g$ has
degree zero, the complement is empty over $D(b)$.

Over $D(b)$ the complement is therefore finite, hence quasi-finite. The
open $U$ is smooth of relative dimension one over $D(b)$, and each of its
fibres is an affine line minus finitely many points. So $U\to D(b)$
satisfies the hypotheses of
Theorem [theorem-pure-lisse-sheaves-over-relative]. Applying that
theorem on $U$ and
Lemma [lemma-finite-quasi-finite-direct-images] on the complement,
we obtain the bound over $D(b)$ from
Lemma [lemma-weight-bounds-partitions](1).

For a general target we argue by induction on $\dim Y_0$. Since
nilpotents do not change the étale site, we may replace $Y_0$ by its
reduction. Take disjoint integral affine opens containing the generic
points of its components, and perform this construction on each of
them. Their union is open, and its complement has smaller dimension.
The case of dimension zero is contained in the construction, because a
reduced zero-dimensional scheme is a finite disjoint union of integral
affine pieces. In general, the restriction of $G$ over the closed
complement is again mixed of weights at most $w$, and the inductive
hypothesis gives the bound there.
Lemma [lemma-weight-bounds-partitions](2), applied to the open
union and its closed complement in the target, gives the bound over
all of $Y_0$.
