+++
kind = "proof"
of = "proposition-determinant-weights-tensor-operations--2"
order = 1148005
uses = ["definition-monodromy-groups--1", "definition-monodromy-groups--2", "proposition-central-element-arithmetic-monodromy-group--1", "proposition-central-element-arithmetic-monodromy-group--2", "lemma-determinant-weight-from-central-scalar--1"]
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

(2) The central element acts on $\bigotimes_a\bigwedge^{n_a}A_a$ by
$\prod_ac_a^{n_a}$. So each simple factor of this nonzero representation
has determinant weight $\sum_an_a\gamma_a$.
Lemma [lemma-tensor-exterior-powers-filtered-representations] identifies these factors with those of
$\bigwedge^rV$.

*Source:* the proof of Proposition [proposition-determinant-weights-tensor-operations].
