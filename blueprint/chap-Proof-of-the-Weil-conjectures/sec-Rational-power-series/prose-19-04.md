+++
id = "prose-19-04"
kind = "hidden"
title = "Rational power series (1)"
order = 1378
+++
The zeta function has integer coefficients by its definition, but the
trace formula proves its rationality only over $\mathbf Q_\ell$, as an alternating
product of $\ell$-adic characteristic polynomials. To compare these
polynomials for different primes $\ell$, we need a form of the zeta
function that does not mention $\ell$. We show that a rational power
series with integer coefficients is a quotient of integral polynomials
in a unique reduced form.

Lemma [lemma-hankel-rank-rationality] shows that rationality is a
condition of linear algebra on the coefficients, namely that the Hankel
matrix $(c_{r+s})$ has finite rank. Such a condition descends from
$\mathbf Q_\ell$ to $\mathbf Q$. For integrality of the reduced fraction,
Lemma [lemma-reduced-fractions-integer-coefficients] uses a lattice
in the row span of the Hankel matrix that is stable under the shift.
The characteristic polynomial of the shift on this lattice is then
integral. For example, the coefficients $c_n=2^{n+1}-1$ of
$1/((1-2T)(1-T))$ satisfy $c_{n+2}=3c_{n+1}-2c_n$. The shift matrix $S$
on the row span has $\det(1-TS)=(1-2T)(1-T)$, which is the reduced
denominator. In the next section we compare the $\ell$-adic
factorizations with the reduced fraction $A/B$.
