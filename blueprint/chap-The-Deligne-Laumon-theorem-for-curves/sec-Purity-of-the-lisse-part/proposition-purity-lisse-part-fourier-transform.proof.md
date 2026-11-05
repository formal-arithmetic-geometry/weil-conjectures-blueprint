+++
kind = "proof"
of = "proposition-purity-lisse-part-fourier-transform"
order = 1281
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "proposition-weights-under-usual-operations", "definition-real-sheaves", "theorem-purity-real-sheaves-curves", "lemma-boundary-stalk", "corollary-unramified-boundary-point", "lemma-fourier-transform-boundary-sequence", "lemma-finite-quasi-finite-direct-images", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
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
