+++
kind = "proof"
of = "lemma-finite-quasi-finite-direct-images"
order = 1325
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-w-local-components", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "theorem-enough-affine-weakly-contractible-objects", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "theorem-grothendieck-lefschetz-trace-formula", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "lemma-weights-exact-sequence", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
We first treat a finite map and then reduce to it by Zariski's main
theorem, which writes a quasi-finite map as an open immersion followed
by a finite map. All the computation is in the finite case, since
extension by zero does not change any nonzero stalk.

For a finite map, exactness follows from
Lemma [lemma-finite-morphisms] and the comparison of coefficients. The same
lemma shows that the stalk at a geometric point $\bar y$ over a closed point $y$
is the direct sum of the stalks at the geometric points of $Z_0$ over
$\bar y$, and the local Frobenius at $y$ permutes these summands. Let
$z$ be a point of residue degree $e=[\kappa(z):\kappa(y)]$. Frobenius
cycles through the $e$ summands over $z$, and its $e$th power on each
of them is conjugate to the local Frobenius at $z$. Each eigenvalue
$\beta$ on this cycle therefore satisfies $\beta^e=\alpha$ for an
eigenvalue $\alpha$ at $z$. If the input has weight $w$, then

$$
|\iota(\beta)|^e=|\iota(\alpha)|=q_z^{w/2}=q_y^{ew/2},
$$

and we find $|\iota(\beta)|=q_y^{w/2}$. This proves that finite direct
image preserves purity. For example, for the constant sheaf on
$\operatorname{Spec}\mathbf F_{q^2}$ over $\operatorname{Spec}\mathbf F_q$,
the direct image has rank two and Frobenius swaps the two summands.
Its eigenvalues $\pm1$ have weight $0$, as the constant sheaf does.

In general, $Y_0$ is Noetherian, hence quasi-compact and
quasi-separated, and Zariski's main theorem in the form
[Stacks, [05K0](https://stacks.math.columbia.edu/tag/05K0)] applies. It factors $g$ as an open immersion
$j:Z_0\hookrightarrow\overline Z_0$ followed by a finite map
$\bar g:\overline Z_0\to Y_0$. By
Proposition [proposition-composition-base-change-rf-shriek] we have
$Rg_!=\bar g_*j_!$, and both functors are exact. Extension by zero
preserves purity, since its other stalks are zero. Now take a mixed
sheaf of weights at most $w$ on $Z_0$, with a finite filtration by
Weil subsheaves whose quotients are pure of weights at most $w$. Since
$j$ and $\bar g$ are defined over $k_0$, the functors $j_!$ and
$\bar g_*$ take Weil subsheaves to Weil subsheaves. Being exact, they
take the filtration to a finite filtration of the direct image whose
quotients are the direct images of the pure quotients. By the first
part these are pure of the same weights, which proves the assertion on
sheaves. Since $Rg_!$ is exact, it commutes with taking cohomology
sheaves, and the assertion on $D_{\leq w}$ follows.
