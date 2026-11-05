+++
kind = "proof"
of = "proposition-determinant-weights-tensor-operations"
order = 1146
uses = ["theorem-rank-one-sheaves-have-finite", "corollary-determinant-weights", "lemma-tensor-exterior-powers-filtered-representations", "definition-monodromy-groups", "lemma-normality-geometric-monodromy", "proposition-central-element-arithmetic-monodromy-group", "lemma-determinant-weight-from-central-scalar", "proposition-determinant-weights-tensor-operations--1", "proposition-determinant-weights-tensor-operations--2"]
+++
We use one central element for $V$ and $V'$ simultaneously, so that
its scalars on the factors of $V\otimes V'$ are products of its scalars
on the factors of $V$ and of $V'$. Since
Proposition [proposition-central-element-arithmetic-monodromy-group] requires
semisimple representations, we apply it to
$V^{\mathrm{ss}}\oplus V'^{\mathrm{ss}}$. This changes nothing,
because by Lemma [lemma-tensor-exterior-powers-filtered-representations] the simple factors of
$V\otimes V'$ and $\bigwedge^rV$ depend only on the composition factors
of $V$ and $V'$. Now let $c_a$ and $c'_b$ be the
scalars by which its central element of degree $N$ acts on the
composition factors $A_a$ of $V$ and $A'_b$ of $V'$. By
Lemma [lemma-determinant-weight-from-central-scalar],
$\gamma_a=\lambda_\iota(c_a)/N$ and
$\operatorname{dw}_\iota(A'_b)=\lambda_\iota(c'_b)/N$.

(1) The central element acts by $c_ac'_b$ on $A_a\otimes A'_b$, and hence
on every simple factor of it. By the same lemma, each such factor has
determinant weight $\gamma_a+\operatorname{dw}_\iota(A'_b)$. Moreover, each
$A_a\otimes A'_b$ is nonzero, and Lemma [lemma-tensor-exterior-powers-filtered-representations]
identifies the simple factors of these tensor products with those of
$V\otimes V'$.

(2) The central element acts on $\bigotimes_a\bigwedge^{n_a}A_a$ by
$\prod_ac_a^{n_a}$. So each simple factor of this nonzero representation
has determinant weight $\sum_an_a\gamma_a$, and
Lemma [lemma-tensor-exterior-powers-filtered-representations] identifies these factors with those of
$\bigwedge^rV$.

(3) We have $\det(s\mid A^\vee)=\det(s\mid A)^{-1}$, and duality carries a
composition series of $V$ to one of $V^\vee$ whose factors are the duals
$A_a^\vee$.
