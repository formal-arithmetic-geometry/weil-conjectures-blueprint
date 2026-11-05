+++
kind = "proof"
of = "theorem-purity-real-sheaves-curves--2"
order = 1166002
uses = ["theorem-purity-real-sheaves-curves--1", "definition-weights"]
+++
Let $\mathcal G$ be the given sheaf. Choose a finite filtration

$$
0=\mathcal H_0\subseteq\mathcal H_1\subseteq\cdots
\subseteq\mathcal H_n\simeq\mathcal G
$$

by lisse Weil subsheaves with irreducible lisse quotients, using
`AlgebraicGeometry.WeilSheaf.IsLisse.exists_filtration_isIrreducibleLisse`.
Composing the inclusions identifies every $\mathcal H_i$ with a
subsheaf of $\mathcal G$, as in
`AlgebraicGeometry.WeilSheaf.exists_mono_of_chain`.
Thus each quotient $\mathcal H_{i+1}/\mathcal H_i$ is an irreducible
constituent of $\mathcal G$ and is punctually pure of some real weight
$w_i$, by [theorem-purity-real-sheaves-curves--1]. Lean uses the weaker
wrapper `AlgebraicGeometry.WeilSheaf.IsReal.exists_isPunctuallyPureOfWeight_cokernel`
at this step, forgetting the determinant identity.

The finite number $w=\sum_i|w_i|$ bounds all these weights from above.
The chosen filtration therefore witnesses that $\mathcal G$ is mixed
of weights at most $w$, and hence mixed, by [definition-weights].
