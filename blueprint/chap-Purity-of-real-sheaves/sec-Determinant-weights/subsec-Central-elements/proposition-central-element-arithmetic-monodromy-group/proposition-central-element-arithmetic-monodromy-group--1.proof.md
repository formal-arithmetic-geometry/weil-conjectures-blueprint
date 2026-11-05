+++
kind = "proof"
of = "proposition-central-element-arithmetic-monodromy-group--1"
order = 1138003
uses = ["lemma-identity-component", "lemma-normality-geometric-monodromy", "lemma-connected-components-images-homomorphisms"]
+++
Put $\Gamma=G(k)$ and $G_0=G^\circ(k)$. The group $G_0$ has finite
index in $\Gamma$, by [lemma-connected-components-images-homomorphisms].
Lean uses the normal core $K$ of $G_0$ in $\Gamma$, which also has finite
index. Put $e=[\Gamma:K]>0$. Every $e$-th power in $\Gamma$ lies in $K$,
so $F^e\in G_0$.

By [lemma-identity-component], write $F^e=ct$, with
$c\in Z(G^\circ)^\circ(k)$ and $t\in H^\circ(k)$. Set $d=c^e$.
Then $d\in K$ and $d$ commutes with $K$. Conjugation by $\Gamma$
preserves the abelian group $Z(K)$, so the product

$$
z=\prod_{g\in\Gamma/K}g d g^{-1}
$$

is well defined, independently of the representatives. Conjugation
permutes its factors, hence $z\in Z(\Gamma)$.

In the abelianization of $\Gamma$, all the conjugates of $d$ have the
same image. Consequently $zF^{-e^3}t^{e^2}$ belongs to the commutator
subgroup. By [lemma-normality-geometric-monodromy] that subgroup is
contained in $H(k)$. Since $t\in H(k)$, we get
$zF^{-e^3}\in H(k)$. Taking $N=e^3$ proves the assertion.

This is the group argument of the private helper
`exists_pos_mem_center_mul_inv_mem` in the monodromy file. It uses no
assertion about determinants of elements of $H$.
