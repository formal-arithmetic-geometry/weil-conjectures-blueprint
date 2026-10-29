+++
id = "sk-prop-wrp-real-envelope"
kind = "proposition"
title = "The real envelope"
order = 4122
uses = ["sk-d-real-weights", "sk-def-wrp-real-definition", "sk-r-real-linear"]
tags = ["sketch"]
+++
Let $\mathcal F\ne0$ be lisse and pure of weight $w$ on a nonempty
finite-type scheme over $k_0$. There is $b\in\overline{\mathbf Q}_\ell^\times$
with $|\iota(b)|=q^{-w/2}$. Put

$$
 \mathcal F^0=\mathcal F\otimes\mathcal B_b,
 \qquad \mathcal E=\mathcal F^0\oplus(\mathcal F^0)^\vee.
$$

Then $\mathcal E$ is real ([sk-def-wrp-real-definition]) and pure of weight
zero, contains $\mathcal F^0$ as a direct summand, and at points over $k_n$
its trace is twice the real part of the trace of $\mathcal F^0$. We call
$\mathcal E$ the *real envelope* of $\mathcal F$.

The same argument applies to twists by the exponential kernel used in the
Fourier argument. Namely, if $\mathcal A$ is pure of weight zero and
$\mathcal L$ has rank one with local eigenvalues of finite order, then

$$
 (\mathcal A\otimes\mathcal L)
   \oplus(\mathcal A^\vee\otimes\mathcal L^{-1})
$$

is real and pure of weight zero. After extension by zero along an open
immersion, the two summands still have complex conjugate local traces;
at the missing points both stalks are zero. Since by Newton's
identities the characteristic polynomials are determined by the traces
of powers, the extension is real as well.

*Complement.* The envelope with a chosen $b$ is
[def-wf-normalized-real-envelope]; its reality is [lem-wf-envelope-real].
