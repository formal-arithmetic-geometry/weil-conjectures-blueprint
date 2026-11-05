+++
kind = "proof"
of = "theorem-purity-higher-direct-images-under"
order = 1373
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "lemma-global-lattice-normal-scheme", "lemma-finite-quasi-finite-direct-images", "theorem-pure-lisse-sheaves-over-relative", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
