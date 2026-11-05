+++
kind = "proof"
of = "lemma-bounds-squared-traces--5"
order = 1202011
uses = ["definition-trace-function", "definition-growth-squared-traces", "proposition-weights-under-usual-operations"]
+++
For the general rescaling assertion, the normalized ratio for $F'$
at $\beta$ is the normalized ratio for $F$ at $\beta+w$:

$$
\frac{S_n(F')}{q^{n(\beta+1)}}
=\frac{S_n(F)}{q^{n(\beta+w+1)}}.
$$

Translate the real parameter in the supremum defining $\nu$ to get
$\nu(F')=\nu(F)-w$.

The identity
`AlgebraicGeometry.WeilSheaf.traceFunction_constantTwist` gives
$t_{F\otimes\mathcal B_b,n}=b^nt_{F,n}$. Taking squared absolute
values and summing proves the energy identity, since
$|\iota(b)|^{2n}=q^{-nw}$. Apply the rescaling assertion and use
$\lambda_\iota(b)=2\log_q|\iota(b)|=-w$.
