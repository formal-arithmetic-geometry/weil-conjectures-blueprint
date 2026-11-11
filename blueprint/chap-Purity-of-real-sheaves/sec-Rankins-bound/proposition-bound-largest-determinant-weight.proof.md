+++
kind = "proof"
of = "proposition-bound-largest-determinant-weight"
order = 1166
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "lemma-logarithm-determinant", "theorem-trace-formula-euler-product", "lemma-filtrations-spectra", "proposition-lattices-representations-normal-scheme", "corollary-determinant-weights", "proposition-determinant-weights-tensor-operations", "lemma-degree-zero-top-cohomology", "lemma-positivity-convergence", "lemma-cohomological-range-curve", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
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
