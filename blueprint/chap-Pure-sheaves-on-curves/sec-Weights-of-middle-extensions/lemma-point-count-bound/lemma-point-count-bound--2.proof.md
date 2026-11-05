+++
kind = "proof"
of = "lemma-point-count-bound--2"
order = 1177004
+++
A $K$-rational point mapping to $x$ induces a $k_0$-embedding
$\kappa(x)\to K$. The point is recovered by composing
$\Spec K\to\Spec\kappa(x)$ with the canonical map
$\Spec\kappa(x)\to X_0$, so this assignment is injective.
The field $\kappa(x)$ is finite-dimensional over $k_0$, and
`card_algHom_le_finrank` bounds the number of these embeddings by
$[\kappa(x):k_0]$.

For a finite scheme $Z_0$ over the finite field $k_0$, sum this bound
over its finitely many points. Their residue fields are finite, and
we obtain
$$
\#Z_0(k_n)\le\sum_{x\in Z_0}[\kappa(x):k_0],
$$
whose right-hand side is independent of $n$.
