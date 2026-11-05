+++
kind = "proof"
of = "proposition-bound-largest-determinant-weight--1"
order = 1162002
uses = ["lemma-degree-zero-top-cohomology", "theorem-trace-formula-euler-product", "lemma-positivity-convergence", "lemma-positivity-euler-factors", "lemma-filtrations-spectra", "proposition-determinant-weights-tensor-operations", "corollary-determinant-weights", "proposition-lattices-representations-normal-scheme"]
+++
For (1), write $V$ for the representation attached to $\mathcal H$.
On the geometric coinvariants, let $T$ be $q$ times the operator induced
by a degree-one lift. This is the Frobenius on $H_c^2(U,\mathcal H)$ of
Lemma [lemma-degree-zero-top-cohomology], represented in Lean by
`AlgebraicGeometry.WeilGroup.compactTopFrobenius`.
If $\mu\ne0$ is an eigenvalue of $T$, the generalized eigenspace for $\mu/q$
on the coinvariants is stable under the Weil group. An irreducible
subquotient of it is a constituent of $V$ with determinant weight
$2\log|\iota(\mu/q)|/\log q$.
This is `AlgebraicGeometry.WeilGroup.exists_isConstituent_hasDetWeight_of_hasEigenvalue`.
The hypothesis therefore gives

$$
|\iota(\mu)|\le q^{D/2+1}.
$$

The same bound is immediate if $\mu=0$.

Theorem [theorem-trace-formula-euler-product] and the vanishing of $H_c^0$
give a polynomial $P_1$ such that

$$
L(U_0,\mathcal H,t)
=\frac{P_1(t)}{\iota\det(1-Tt)}.
$$

Lean uses this identity in the form
`AlgebraicGeometry.WeilGroup.exists_eulerSeries_mul_eq_coe`.
The denominator has no zero on the disc of radius $R=q^{-D/2-1}$, so
the Euler series has radius of convergence at least $R$.
By Lemma [lemma-positivity-convergence], every inverse local factor has
at least this radius. If $\alpha$ is a local eigenvalue at a point of
degree $e$, choose $z$ with $z^e=\iota(\alpha)^{-1}$.
The local denominator vanishes at $z$, so $|z|\ge R$.
Since $|z|^e=|\iota(\alpha)|^{-1}$ and $q_x=q^e$, taking logarithms gives
$\lambda_{\iota,x}(\alpha)\le D+2$.

For (2), apply (1) to $\mathcal G\otimes\mathcal G$.
Its inverse local factors have nonnegative coefficients by
Lemma [lemma-positivity-euler-factors], and its constituent determinant
weights are at most $2d$ by
Proposition [proposition-determinant-weights-tensor-operations] and
Corollary [corollary-determinant-weights]. Lean combines the latter facts in
`AlgebraicGeometry.WeilGroup.le_add_of_isConstituent_tprod_of_hasDetWeight`.
By Lemma [lemma-filtrations-spectra], $\alpha^2$ is a local eigenvalue of
the tensor square. Since
$\lambda_{\iota,x}(\alpha^2)=2\lambda_{\iota,x}(\alpha)$, (1) gives
$\lambda_{\iota,x}(\alpha)\le d+1$, the case $j=0$.

The tensor square is again lisse and $\iota$-real: its matrices have
continuous coefficients on the geometric group, and its complex
eigenvalues form a conjugation-stable multiset of pairwise products.
These are `AlgebraicGeometry.WeilGroup.IsLisse.tprod` and
`AlgebraicGeometry.WeilGroup.IsReal.tprod`.
Applying the induction hypothesis to this square gives

$$
2\lambda_{\iota,x}(\alpha)\le 2d+\frac1{2^j},
$$

which is the assertion for $j+1$ after division by two.
Finally, the main bound follows by letting $j$ tend to infinity and
taking $d=\beta$; Lean expresses the limit by choosing $2^{-j}<\varepsilon$
for each $\varepsilon>0$.
