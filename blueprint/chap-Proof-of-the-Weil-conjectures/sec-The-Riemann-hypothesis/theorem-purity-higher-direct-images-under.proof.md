+++
kind = "proof"
of = "theorem-purity-higher-direct-images-under"
order = 1370
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-w-local-components", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "theorem-comparison-over-henselian-pair-degree", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "proposition-sp-unique-adjoint", "corollary-degreewise-duality-over-fields", "lemma-bounding-weights-mixed-sheaf", "proposition-weights-under-usual-operations", "lemma-global-lattice-normal-scheme", "theorem-weights-rf-shriek", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Since $f_0$ is proper, the definition of $Rf_{0!}$ by
compactification identifies it with $Rf_{0*}$. This identification
commutes with the base change maps that define the Weil structures,
which proves the first assertion.

Fix a closed point $y$. By proper base change, the stalk at $\bar y$
with its local Frobenius is $H^i(X_{\bar y},F)$. By
Theorem [theorem-direct-image-mixed-sheaf], $R^if_{0*}F$ is mixed
of weights at most $w+i$, so every eigenvalue $\alpha$ there
satisfies

$$
|\iota(\alpha)|\leq q_y^{(w+i)/2}.
$$

The opposite inequality comes from duality. The dual $F^\vee$ is
lisse of weight $-w$, so $F^\vee(d)$ has weight $-w-2d$. On the
smooth proper geometric fibre, Corollary [corollary-degreewise-duality-over-fields] and
Theorem [theorem-poincare-duality-frobenius] give a Frobenius-equivariant perfect
pairing

$$
H^i(X_{\bar y},F)\times
H^{2d-i}(X_{\bar y},F^\vee(d))\longrightarrow\overline{\mathbf Q}_\ell.
$$

Since the pairing is perfect and takes values in the trivial Weil
line, it identifies the second factor with the dual of the first as a
Frobenius module, so the eigenvalues on the second factor are the
$\alpha^{-1}$, with multiplicities. Applying
Theorem [theorem-direct-image-mixed-sheaf] once more, now to the
structure map of the fibre over $\kappa(y)$ and to $F^\vee(d)$, of
weight $-w-2d$, and to its cohomology in degree $2d-i$, we get

$$
|\iota(\alpha)|^{-1}
\leq q_y^{(-w-2d+2d-i)/2}=q_y^{(-w-i)/2}.
$$

The two inequalities give $|\iota(\alpha)|=q_y^{(w+i)/2}$ at every
closed point $y$. Every nonzero pure quotient in a mixed filtration of
$R^if_{0*}F$ has a nonzero stalk at some closed point, so its weight is
$w+i$. This proves the last assertion.
