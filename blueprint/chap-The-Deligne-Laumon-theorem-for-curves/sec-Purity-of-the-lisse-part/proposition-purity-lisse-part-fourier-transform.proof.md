+++
kind = "proof"
of = "proposition-purity-lisse-part-fourier-transform"
order = 1284
uses = ["proposition-etale-implications", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-dctf-x-qbar-2-colimit", "lemma-change-coefficients", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "lemma-filtrations-spectra", "proposition-lattices-representations-normal-scheme", "theorem-rank-one-sheaves-have-finite", "corollary-rank-one-weights", "corollary-determinant-weights", "definition-weil-representation", "lemma-normality-geometric-monodromy", "lemma-identity-component", "lemma-determinant-weight-from-central-scalar", "lemma-degree-zero-top-cohomology", "proposition-bound-largest-determinant-weight", "proposition-weights-j-boundary-points", "lemma-fourier-transform-boundary-sequence", "lemma-finite-quasi-finite-direct-images", "remark-non-noetherian-compactifications", "remark-base-change-compactification", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
We twist to weight zero and add the dual, as in
Proposition [proposition-twisting-weight-zero-adding-dual], before taking the transform, so
that a twist of $M'$ becomes a quotient of a real sheaf, to which
Theorem [theorem-purity-real-sheaves-curves] applies.

Choose $b$ as in
Proposition [proposition-twisting-weight-zero-adding-dual], so that
$M^0=M\otimes\mathcal B_b$ is pure of weight zero.

On the product of the line and the dual line, consider the sheaf

$$
F=
(p_1^*j_!M^0\otimes\mathcal K_\psi)
\ \oplus\
(p_1^*j_!(M^0)^\vee\otimes\mathcal K_{\psi^{-1}}).
$$

At each closed point, the Frobenius eigenvalues of the second summand
are the complex conjugates of those of the first, because the
eigenvalues of $M^0$ have absolute value one and those of the
character sheaves are roots of unity, while at the boundary both zero
extensions have zero stalks. Hence $F$ is real, as in
Lemma [lemma-twisted-envelope]. Moreover, since
duality replaces $a$ by $-a$, the dual $(M^0)^\vee$ also has no
geometric constituent of the form $\mathcal L_{\psi(ax)}$, so the argument of
Lemma [lemma-fourier-transform-boundary-sequence] shows
that the direct image with compact support of $F$ along $p_2$ is
concentrated in degree one. We set $H=R^1p_{2!}F$.

Let $y$ be a point with values in a finite field. Since
$Rp_{2!}F=H[-1]$, the trace formula for $Rp_{2!}$
(Corollary [corollary-trace-functions-direct-image-compact]) gives
$-t_H(y)=\sum_x t_F(x,y)$. For each $x$ the traces of the two
summands of $F$ at $(x,y)$ are complex conjugate, so $t_H(y)$ is
real. Over the finite extensions of $\kappa(y)$ the same argument
shows that the trace of every power of the local
Frobenius is real. These traces are the power sums of the local
eigenvalues, and the Newton identities express the coefficients of
the characteristic polynomial through the power sums with rational
coefficients. Hence the local characteristic polynomials of $H$ have
real coefficients, that is, $H$ is real.

The first summand of $H$ is
$R^1p_{2!}(p_1^*j_!M\otimes\mathcal K_\psi)\otimes\mathcal B_b$ by the
projection formula for the constant twist, that is, $G\otimes\mathcal B_b$
with $G=\operatorname{FT}_\psi(j_!M)$ as in
Lemma [lemma-fourier-transform-boundary-sequence]. Tensoring the surjection
$G\to j'_*M'$ of that lemma with $\mathcal B_b$, we see that
$M'\otimes\mathcal B_b$ is a quotient of a direct summand of $H$.
To apply the purity theorem we restrict to a dense open on which both $H$ and $M'$ are lisse.
There $M'\otimes\mathcal B_b$ is a lisse quotient of the real lisse
sheaf $H$, and it is irreducible by Lemma [lemma-simple-objects],
so by Theorem [theorem-purity-real-sheaves-curves] it is
pure of some real weight. Removing the
twist by $\mathcal B_b$, we find that $M'$ is pure of some weight $v$
on that open. Since the open where $M'$ is lisse is a smooth
geometrically connected curve, the last assertion of
Corollary [corollary-unramified-boundary-point] extends the purity to
all of it.
