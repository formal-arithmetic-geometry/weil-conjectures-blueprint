+++
kind = "proof"
of = "corollary-functional-equation"
order = 1046
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "proposition-exceptional-inverse-image-smooth-morphism", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-relative-dualizing-complex", "theorem-trace-isomorphism-top-degree", "corollary-cup-product-pairing", "lemma-additivity-open-subscheme-complement", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-function-sheaf-dictionary", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "lemma-finite-quasi-finite-direct-images", "theorem-pure-lisse-sheaves-over-relative", "lemma-hankel-rank-rationality", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Duality gives the relations $b_{2d-i}=b_i$ and $D^2=q^{d\chi}$. If we substitute
$1/(q^dT)$ into each factor of the cohomological expression for
$Z(X_0,T)$, duality turns the factor in degree $i$ into
the factor in degree $2d-i$ times an explicit scalar.

We apply Theorem [theorem-poincare-duality-frobenius] with $K=\mathbf Q_\ell$ and $X$ proper.
It gives $b_{2d-i}=b_i$, and it shows that the eigenvalues of $F_{2d-i}$ are the $q^d/\alpha$ for
the eigenvalues $\alpha$ of $F_i$, with multiplicities. Hence
$\det F_i\cdot\det F_{2d-i}=q^{db_i}$. Since $(-1)^i=(-1)^{2d-i}$, we get

$$
D^2=\prod_i\bigl(\det F_i\cdot\det F_{2d-i}\bigr)^{(-1)^i}
=q^{d\chi}.
$$

Since $b_{2d-i}=b_i$, the terms of $\chi$ for $i$ and $2d-i$ are equal
and cancel modulo $2$, so $\chi\equiv b_d\pmod 2$. If $d$ is even,
$d\chi$ is even anyway. If $d$ is odd,
the pairing on $H^d$ of each connected component of $X$ is perfect and
alternating (Corollary [corollary-cup-product-pairing]), so $b_d$ is even. In
both cases $d\chi$ is even. Then $\varepsilon^2=1$ because $D^2=q^{d\chi}$.

Now consider a single factor. Since $F_i$ is invertible, its
eigenvalues $\alpha$ are nonzero. Pulling $-\alpha/(q^dT)$ out of
each linear factor gives

$$
\det\bigl(1-q^{-d}T^{-1}F_i\bigr)
=\prod_\alpha\Bigl(-\frac{\alpha}{q^dT}\Bigr)\Bigl(1-\frac{q^d}{\alpha}T\Bigr)
=(-1)^{b_i}\frac{\det F_i}{(q^dT)^{b_i}}\det\bigl(1-TF_{2d-i}\bigr).
$$

By Corollary [corollary-point-counting-zeta-function], and since $H^i_c=H^i$ as $X_0$ is
proper, $Z(X_0,T)$ is the product of the
$\det(1-TF_i)^{(-1)^{i+1}}$. We substitute $1/(q^dT)$ for $T$ and apply
the last display to each factor. Since $(-1)^i=(-1)^{2d-i}$, the factors
$\det(1-TF_{2d-i})^{(-1)^{i+1}}$ multiply to $Z(X_0,T)$, and the scalar
factors multiply to

$$
(-1)^{\chi}D^{-1}(q^dT)^{\chi}=(-1)^{\chi}D\,T^{\chi},
$$

by $D^2=q^{d\chi}$. The second form of the equation is the definition
of $\varepsilon$.
