+++
kind = "proof"
of = "theorem-purity-real-sheaves-curves--1"
order = 1166001
uses = ["lemma-filtrations-spectra", "proposition-lattices-representations-normal-scheme", "corollary-determinant-weights", "proposition-determinant-weights-tensor-operations", "proposition-bound-largest-determinant-weight"]
+++
First work with an $\iota$-real lisse Weil representation $\rho$ on an affine curve.
Choose a composition series with factors $Q_a$, and put
$r_a=\dim Q_a$ and $\gamma_a=\operatorname{dw}_\iota(Q_a)$.
By Lemma [lemma-filtrations-spectra], the semisimplification
$S=\bigoplus_a Q_a$ has the same local characteristic polynomials as
$\rho$. Hence $S$ is real, and so are its exterior powers: complex
conjugation permutes their eigenvalues, which are products with distinct
indices of the eigenvalues of $S$.

Fix a factor $Q_b$ of determinant weight $\gamma$, and put

$$
A=\{a:\gamma_a>\gamma\},\qquad
N=\sum_{a\in A}r_a,\qquad B=\sum_{a\in A}r_a\gamma_a.
$$

By Proposition [proposition-determinant-weights-tensor-operations],
the determinant weight of every constituent of $\bigwedge^{N+1}S$
is a sum of $N+1$ entries of the list in which $\gamma_a$ occurs
$r_a$ times. Such a sum is at most $B+\gamma$.
The description as a sum is supplied by
`Representation.exists_multiset_le_and_detWeight_eq_sum_of_exteriorPower`.

At a closed point $x$, let $\beta$ be an eigenvalue on $Q_b$.
Multiplying $\beta$ by all the eigenvalues on the factors $Q_a$ with
$a\in A$ gives an eigenvalue of $\bigwedge^{N+1}S$, by
Lemma [lemma-filtrations-spectra]. Corollary [corollary-determinant-weights]
shows that the product of those other eigenvalues has weight $B$.
Proposition [proposition-bound-largest-determinant-weight] therefore gives
$\operatorname{wt}_{\iota,q_x}(\beta)+B\le B+\gamma$.
Every eigenvalue on $Q_b$ has weight at most $\gamma$, while the sum of
their weights, counted with multiplicity, is the weight of the determinant,
namely $r_b\gamma$. Thus every one of their weights equals $\gamma$.
This is the argument of
`AlgebraicGeometry.WeilGroup.isPunctuallyPure_subquotient_of_isReal`;
the last step is `Multiset.eq_of_le_of_sum_eq`.

An arbitrary irreducible constituent occurs as a factor of a composition
series. The affine assertion follows by transporting along this
isomorphism and using uniqueness of the determinant weight.
For a general curve and a closed point $x$, choose an affine open
neighbourhood $U_0$ as in
`AlgebraicGeometry.WeilGroup.exists_restriction_isAffine`.
The restriction $W(U_0)\to W(C_0)$ is continuous, surjective, preserves
degrees and carries local Frobenius elements into the corresponding
conjugacy classes. Consequently restriction preserves lissity, reality,
irreducible constituents and determinant weights. The affine assertion
gives purity at $x$, since the residue cardinality and local eigenvalues
are unchanged.

Finally pass from sheaves to representations through the lisse
sheaf–representation equivalence
`AlgebraicGeometry.WeilGroup.exists_equivalence_isLisse`, built from
Proposition [proposition-lattices-representations-normal-scheme].
Kernels and cokernels of maps of lisse sheaves are lisse. Under the
equivalence, the images of $\mathcal G_1$ and $\mathcal G_2$ in the
representation of $\mathcal G$ therefore exhibit the representation of
$\mathcal V$ as a subquotient. Irreducibility makes it a constituent.
The equivalence identifies the stalk Frobenius operators with the local
Frobenius actions, so it preserves characteristic polynomials and
determinants. Apply the representation assertion and
Corollary [corollary-determinant-weights], and transport the resulting
purity and determinant identity back to the stalks of $\mathcal V$.
