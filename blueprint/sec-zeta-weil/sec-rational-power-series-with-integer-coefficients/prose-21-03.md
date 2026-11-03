+++
id = "prose-21-03"
kind = "hidden"
title = "Rational power series with integer coefficients"
order = 794
+++
To compare, for different primes $\ell$, the characteristic
polynomials of Frobenius on $\ell$-adic cohomology, we need a description of the zeta function that does not mention $\ell$.
The following two elementary lemmas show that a rational power series
with integer coefficients is a quotient of integral polynomials in a
unique reduced form.

The zeta function has integer coefficients by its definition, but the
trace formula proves its rationality only over $\Ql$, as an alternating
product of $\ell$-adic characteristic polynomials. Rationality is a
linear-algebra condition on the coefficients, the finiteness of the
rank of the Hankel matrix $(c_{r+s})$, and so it descends from $\Ql$ to
$\mathbf Q$ (Lemma [sk-prop-criterion]). Integrality of the reduced fraction is a further
step: the row span of the Hankel matrix contains a lattice stable
under the shift, and the characteristic polynomial of an integral
matrix is integral (Lemma [sk-lem-wweil-integer-rationality]). For
example, the coefficients $c_n=2^{n+1}-1$ of
$1/((1-2T)(1-T))$ satisfy $c_{n+2}=3c_{n+1}-2c_n$, and the shift
matrix $S$ on the row span has $\det(1-TS)=(1-2T)(1-T)$, which is the
reduced denominator. The reduced fraction
$A/B$ is the object to which the $\ell$-adic factorizations are
compared in the next subsection.
