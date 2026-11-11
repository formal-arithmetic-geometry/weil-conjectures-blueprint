+++
kind = "proof"
of = "proposition-determinant-weights-tensor-operations--1"
order = 1148003
uses = ["corollary-determinant-weights--2", "lemma-tensor-exterior-powers-filtered-representations--3", "definition-monodromy-groups--1", "definition-monodromy-groups--2", "lemma-normality-geometric-monodromy--1", "proposition-central-element-arithmetic-monodromy-group--1", "proposition-central-element-arithmetic-monodromy-group--2", "lemma-determinant-weight-from-central-scalar--1"]
+++
We use one central element for $V$ and $V'$ simultaneously, so that
its scalars on the factors of $V\otimes V'$ are products of its scalars
on the factors of $V$ and of $V'$. Since
Proposition [proposition-central-element-arithmetic-monodromy-group] requires
semisimple representations, we apply it to
$V^{\mathrm{ss}}\oplus V'^{\mathrm{ss}}$. This changes nothing,
because by Lemma [lemma-tensor-exterior-powers-filtered-representations] the simple factors of
$V\otimes V'$ and $\bigwedge^rV$ depend only on the composition factors
of $V$ and $V'$. Let $c_a$ and $c'_b$ be the
scalars by which its central element of degree $N$ acts on the
composition factors $A_a$ of $V$ and $A'_b$ of $V'$. By
Lemma [lemma-determinant-weight-from-central-scalar],
$\gamma_a=\lambda_\iota(c_a)/N$ and
$\operatorname{dw}_\iota(A'_b)=\lambda_\iota(c'_b)/N$.

(1) The central element acts by $c_ac'_b$ on $A_a\otimes A'_b$, and hence
on every simple factor of it. By the same lemma, each such factor has
determinant weight $\gamma_a+\operatorname{dw}_\iota(A'_b)$. Each
$A_a\otimes A'_b$ is nonzero, and Lemma [lemma-tensor-exterior-powers-filtered-representations]
identifies the simple factors of these tensor products with those of
$V\otimes V'$.

*Source:* the proof of Proposition [proposition-determinant-weights-tensor-operations].
