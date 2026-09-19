+++
id = "prop-zla-reciprocal-eigenvalue-pairing"
kind = "theorem"
title = "Reciprocal eigenvalue pairing"
order = 1032
tags = ["latex:proposition"]
uses = ["def-zla-similitude-pairing", "lem-zla-adjoint-conjugacy"]
+++
Let $B:V\times W\to E$ be a perfect similitude pairing of multiplier $\mu$ for
the automorphisms $F_V,F_W$, let $\Omega$ be an algebraic closure of $E$, and
put $b=\dim_EV=\dim_EW$. If $\alpha_1,\ldots,\alpha_b\in\Omega$ are the
eigenvalues of $F_V\otimes_E\Omega$, counted with algebraic multiplicity, then
the eigenvalues of $F_W\otimes_E\Omega$, counted with algebraic multiplicity,
are

$$
\frac{\mu}{\alpha_1},\ldots,\frac{\mu}{\alpha_b}.
$$

No semisimplicity assumption is required.

## Proof

By [lem-zla-adjoint-conjugacy] the endomorphism $F_W$ is conjugate to
$\mu\,(F_V^{-1})^\vee$, and conjugate endomorphisms have the same
characteristic polynomial. Dualizing does not change the characteristic
polynomial, inverting an automorphism replaces its eigenvalue multiset by the
multiset of inverses, and multiplying by the scalar $\mu$ scales every
eigenvalue by $\mu$; all three operations are computed on characteristic
polynomials, so no semisimplicity is needed.
