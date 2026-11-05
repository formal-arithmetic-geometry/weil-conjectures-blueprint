+++
kind = "proof"
of = "definition-real-sheaves--2"
order = 1153003
uses = ["definition-real-sheaves--1", "lemma-logarithm-determinant"]
+++
Put $P_x(T)=\det(1-T\operatorname{Frob}_x\mid\mathcal G_{\bar x})$.
By [definition-real-sheaves--1], its images under $\iota$ and
$\operatorname{conj}\circ\iota$ agree coefficient by coefficient.
These images determine the images of all positive-power traces: the
logarithmic derivative identity of [lemma-logarithm-determinant] gives

$$
-T\frac{(\iota P_x)'(T)}{\iota P_x(T)}
=\sum_{n\ge1}\iota\operatorname{Tr}
(\operatorname{Frob}_x^n\mid\mathcal G_{\bar x})T^n.
$$

Apply this identity to the two embeddings and compare coefficients.
For $n=0$, the trace is the dimension of the stalk, which is the degree
of $P_x$, since local Frobenius is invertible. This is the comparison used in
`FrobeniusModule.map_trace_frobeniusEnd_pow_eq_of_map_localPolynomial_eq`.

For the representation formulation, [definition-real-sheaves--1] gives
$\overline{M_x}=M_x$. Complex conjugation commutes with finite sums and
natural powers, so conjugating the power sum leaves it unchanged. These
power sums are the traces of the corresponding powers of local Frobenius.
