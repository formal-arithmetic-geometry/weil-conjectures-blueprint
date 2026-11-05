+++
kind = "proof"
of = "theorem-direct-image-mixed-sheaf"
order = 1362
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "proposition-weights-under-usual-operations", "lemma-finite-quasi-finite-direct-images", "lemma-weights-exact-sequence", "lemma-weight-bounds-partitions", "proposition-relative-affine-line", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Say that a morphism has the property if the conclusion holds for it,
for every $w$ and every mixed $F$ of weights at most $w$. Quasi-finite
maps and projections of relative affine lines have the property, and by
Lemma [lemma-relative-noether-normalization-over-stratification]
every $f$ is built from these two kinds of maps. So it suffices to show
that the property is stable under composition and under finite partitions.

For composition, let $X_0\xrightarrow{h}Z_0\xrightarrow{g}Y_0$ and consider the Leray
spectral sequence for compact supports,

$$
E_2^{a,b}=R^ag_!(R^bh_!F)\ \Longrightarrow\ R^{a+b}(gh)_!F.
$$

It is Frobenius-equivariant by the naturality of the truncation tower
and of the composition isomorphism for direct image with compact
support. If both maps have the property, then $E_2^{a,b}$ is mixed of
weights at most $w+a+b$. Since each later page is a subquotient of the
previous one, the same holds for $E_\infty^{a,b}$. The abutment
filtration of $R^n(gh)_!F$ is finite, because the operations preserve
bounded constructible complexes. Its quotients are the
$E_\infty^{a,n-a}$, and by Lemma [lemma-weights-exact-sequence]
$R^n(gh)_!F$ is mixed of weights at most $w+n$.

For partitions, we apply Lemma [lemma-relative-noether-normalization-over-stratification] and refine the
partitions to filtrations by open and closed pieces. After this
refinement we can order the pieces so that each is open in the union
of itself and the later ones. This lets us apply the localization
sequences one piece at a time. On the pieces, the restriction
of $F$ to each source piece is again mixed of weights at most $w$, and on
every refined source piece the finite map to $\mathbf A^d_V$ restricts
to a separated quasi-finite map, which has the property by
Lemma [lemma-finite-quasi-finite-direct-images]. Moreover, the projection
$\mathbf A^d_V\to V$ is a composition of $d$ projections of relative
affine lines. Each of them has the property by
Proposition [proposition-relative-affine-line], and by the
composition argument the map from the piece to $V$ has the property.
Finally, we assemble the pieces one at a time in the chosen order. By
Lemma [lemma-weight-bounds-partitions](1) on the source and
Lemma [lemma-weight-bounds-partitions](2) on the target, the bound
for the pieces implies the bound for $R^if_!F$ on $Y_0$.
