+++
kind = "proof"
of = "proposition-bound-largest-determinant-weight"
order = 1166
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "lemma-additivity-open-subscheme-complement", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-function-sheaf-dictionary", "proposition-lattices-representations-normal-scheme", "theorem-rank-one-sheaves-have-finite", "corollary-rank-one-weights", "corollary-determinant-weights", "lemma-tensor-exterior-powers-filtered-representations", "lemma-normality-geometric-monodromy", "lemma-identity-component", "lemma-determinant-weight-from-central-scalar", "lemma-degree-zero-top-cohomology", "lemma-finite-quasi-finite-direct-images", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
We bound the poles of $L(U_0,\mathcal G^{\otimes2m},t)$ by determinant
weights through $H^2_c$, and positivity then passes the bound to each local
factor.

We may assume that $\mathcal G$ is semisimple. Indeed, by
Lemma [lemma-filtrations-spectra], replacing $\mathcal G$ by its
semisimplification changes neither its local characteristic polynomials
nor the determinant weights of its constituents.

*The top cohomology.* Fix $m\ge1$ and put
$\mathcal T=\mathcal G^{\otimes2m}$. We show that every eigenvalue $\mu$ of
$F$ on $H_c^2(U,\mathcal T)$ satisfies $|\iota(\mu)|\le q^{m\beta+1}$; these
eigenvalues determine the possible poles of the $L$-function. First, every
constituent of $\mathcal T$ has determinant weight at most $2m\beta$, by
Proposition [proposition-determinant-weights-tensor-operations](1).
Next, Lemma [lemma-degree-zero-top-cohomology] identifies
$H_c^2(U,\mathcal T)$ with $T_{\pi_1(U)}(-1)$, where
$T$ is the generic fibre of $\mathcal T$. The geometric fundamental group
acts trivially on $T_{\pi_1(U)}$, so its simple Weil factors are
one-dimensional, as one sees by triangularizing the operator induced by a
degree-one lift. Let $b$ be the eigenvalue on such a factor. Since
$T_{\pi_1(U)}$ is a Weil quotient of $T$, the factor is a constituent of
$\mathcal T$, and its determinant weight is $\lambda_\iota(b)$. From
$\lambda_\iota(b)=2\log_q|\iota(b)|\le2m\beta$ we get
$|\iota(b)|\le q^{m\beta}$. The twist $(-1)$ multiplies eigenvalues by $q$,
and the claim follows.

*The local factors.* The bound on $H^2_c$ makes the $L$-function
holomorphic on a disc, and positivity passes this to each local
factor. As $H_c^0=0$ by Lemma [lemma-degree-zero-top-cohomology],
Theorem [theorem-trace-formula-euler-product] gives

$$
L(U_0,\mathcal T,t)
=\prod_{x\in|U_0|}\det(1-\operatorname{Frob}_x t^{\deg(x)}\mid\mathcal T_{\bar x})^{-1}
=\frac{\det(1-Ft\mid H_c^1(U,\mathcal T))}
{\det(1-Ft\mid H_c^2(U,\mathcal T))}.
$$

This is an identity of formal power series, and the product is
coefficientwise locally finite because there are only finitely many
closed points of bounded degree. Now put $R_m=q^{-m\beta-1}$. By the bound on
$H_c^2$, the denominator has no zero on the disc $|t|<R_m$ after applying
$\iota$, so the rational function, and with it its Taylor series, is
holomorphic on this disc.

Each local factor
$\det(1-\operatorname{Frob}_x t^{\deg(x)}\mid\mathcal T_{\bar x})$ has no zero
on the same disc. Indeed, after applying $\iota$ the local factors of
$L(U_0,\mathcal T,t)$ are power series with nonnegative coefficients and
constant coefficient one by Lemma [lemma-positivity-euler-factors], so
that Lemma [lemma-positivity-convergence] applies.

Now let $\alpha$ be a local eigenvalue of $\mathcal G$. Then $\alpha^{2m}$ is
an eigenvalue on $\mathcal T$ by Lemma [lemma-filtrations-spectra], and
$1-\iota(\alpha)^{2m}t^{\deg(x)}$ divides the local factor. Its roots
have absolute value $|\iota(\alpha)|^{-2m/\deg(x)}$, so by the previous paragraph this number must be at
least $R_m$, that is,

$$
|\iota(\alpha)|^2\le q_x^{\beta+1/m}.
$$

Letting $m$ tend to infinity proves the bound.
