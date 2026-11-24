+++
kind = "proof"
of = "proposition-purity-lisse-part-fourier-transform"
order = 1284
uses = ["lemma-integral-models", "proposition-proper-direct-image-constructible-complexes", "proposition-six-operations-dctf", "lemma-perfect-complexes-geometric-point", "theorem-grothendieck-lefschetz-trace-formula", "definition-trace-function", "lemma-subobjects-quotients-weil-sheaves", "proposition-weights-under-usual-operations", "definition-real-sheaves", "theorem-purity-real-sheaves-curves", "lemma-boundary-stalk", "corollary-unramified-boundary-point", "proposition-twisting-weight-zero-adding-dual", "proposition-base-change-fourier-inversion", "lemma-fourier-transform-boundary-sequence", "lemma-twisted-envelope", "lemma-finite-quasi-finite-direct-images"]
+++
We twist to weight zero and add the dual, as in
Proposition [proposition-twisting-weight-zero-adding-dual], before taking the transform, so
that a twist of $M'$ becomes a quotient of a [real](@definition-real-sheaves) sheaf, to which
Theorem [theorem-purity-real-sheaves-curves] applies.

Choose $b$ as in
Proposition [proposition-twisting-weight-zero-adding-dual], so that
$M^0=M\otimes\mathcal B_b$ is [pure](@definition-weights) of weight zero.

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
extensions have zero stalks. Hence $F$ is [real](@definition-real-sheaves), as in
Lemma [lemma-twisted-envelope]. Moreover, since
duality replaces $a$ by $-a$, the dual $(M^0)^\vee$ also has no
geometric constituent of the form $\mathcal L_{\psi(ax)}$, so the argument of
Lemma [lemma-fourier-transform-boundary-sequence] shows
that the [direct image with compact support](@proposition-construction-independence-rf-shriek) of $F$ along $p_2$ is
concentrated in degree one. We set $H=R^1p_{2!}F$.

Let $y$ be a point with values in a finite field. Since
$Rp_{2!}F=H[-1]$, the trace formula for [$Rp_{2!}$](@proposition-construction-independence-rf-shriek)
(Corollary [corollary-trace-functions-direct-image-compact]) gives
$-t_H(y)=\sum_x t_F(x,y)$. For each $x$ the traces of the two
summands of $F$ at $(x,y)$ are complex conjugate, so [$t_H(y)$](@definition-trace-function) is
real. Over the finite extensions of $\kappa(y)$ the same argument
shows that the trace of every power of the local
Frobenius is real. These traces are the power sums of the local
eigenvalues, and the Newton identities express the coefficients of
the characteristic polynomial through the power sums with rational
coefficients. Hence the local characteristic polynomials of $H$ have
real coefficients, that is, $H$ is [real](@definition-real-sheaves).

The first summand of $H$ is
$R^1p_{2!}(p_1^*j_!M\otimes\mathcal K_\psi)\otimes\mathcal B_b$ by the
projection formula for the constant twist, that is, $G\otimes\mathcal B_b$
with $G=\operatorname{FT}_\psi(j_!M)$ as in
Lemma [lemma-fourier-transform-boundary-sequence]. Tensoring the surjection
$G\to j'_*M'$ of that lemma with [$\mathcal B_b$](@proposition-weights-under-usual-operations), we see that
$M'\otimes\mathcal B_b$ is a quotient of a direct summand of $H$.
To apply the [purity theorem](@theorem-purity-real-sheaves-curves) we restrict to a dense open on which both $H$ and $M'$ are [lisse](@definition-lisse-sheaves).
There $M'\otimes\mathcal B_b$ is a [lisse](@definition-lisse-sheaves) quotient of the [real](@definition-real-sheaves) [lisse](@definition-lisse-sheaves)
sheaf $H$, and it is irreducible by Lemma [lemma-simple-objects],
so by Theorem [theorem-purity-real-sheaves-curves] it is
[pure](@definition-weights) of some real weight. Removing the
twist by [$\mathcal B_b$](@proposition-weights-under-usual-operations), we find that $M'$ is [pure](@definition-weights) of some weight $v$
on that open. Since the open where $M'$ is [lisse](@definition-lisse-sheaves) is a smooth
geometrically connected curve, the last assertion of
Corollary [corollary-unramified-boundary-point] extends the [purity](@definition-weights) to
all of it.
