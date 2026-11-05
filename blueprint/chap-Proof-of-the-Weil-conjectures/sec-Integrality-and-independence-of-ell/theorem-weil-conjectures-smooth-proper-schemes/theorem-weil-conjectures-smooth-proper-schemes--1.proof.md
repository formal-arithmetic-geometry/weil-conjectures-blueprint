+++
kind = "proof"
of = "theorem-weil-conjectures-smooth-proper-schemes--1"
order = 1388002
uses = ["corollary-point-counting-zeta-function", "corollary-cup-product-pairing", "lemma-hankel-rank-rationality", "lemma-reduced-fractions-integer-coefficients", "theorem-weil-conjectures-smooth-proper-schemes--2", "theorem-weil-conjectures-smooth-proper-schemes--5", "theorem-weil-conjectures-smooth-proper-schemes--10", "theorem-weil-conjectures-smooth-proper-schemes--11", "theorem-weil-conjectures-smooth-proper-schemes--16"]
+++
Fix a prime $\ell\nmid q$. The spaces $\overline H^i_\ell$, their Frobenius endomorphisms and the point counts form a trace datum by [corollary-point-counting-zeta-function]. Poincaré duality supplies perfect pairings in complementary degrees with Frobenius multiplier $q^d$.

Embed $\overline{\mathbf Q}_\ell$ in $\mathbf C$. The purity in [theorem-weil-conjectures-smooth-proper-schemes--5] holds for every such embedding. Hankel descent and the integrality of the zeta series give a reduced normalized integral fraction $A/B$. Its roots are algebraic; extension of embeddings of their number fields shows that each determinant factor is pure under every embedding of these number fields. This is `TraceDatum.isUniversallyPureOfWeight_map_P`.

The distinct weights separate the factors of $A$ and $B$. Taking their weight factors and descending normalized divisors of integer polynomials gives the integer family (`Polynomial.exists_int_norm_eq_of_isUniversallyPure`). The endpoint identities [theorem-weil-conjectures-smooth-proper-schemes--10] and [theorem-weil-conjectures-smooth-proper-schemes--11], and the pairings of [theorem-weil-conjectures-smooth-proper-schemes--16], give the factorization, purity and root reciprocity. Injectivity of the chosen embedding gives the comparison in $\overline{\mathbf Q}_\ell[T]$. These are the steps of `AlgebraicGeometry.Scheme.exists_isWeilFactorization_of_prime`.

Choose one prime $\ell_0\nmid q$ and its integer family. For any other $\ell$, repeat the construction and apply [theorem-weil-conjectures-smooth-proper-schemes--2] to identify the two integer families. Thus the first family realizes all the determinant factors.
