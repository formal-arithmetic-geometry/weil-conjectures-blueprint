+++
kind = "proof"
of = "sk-prop-walg-determinant-weights"
+++
Apply Proposition [sk-p-central] to
$V^{\mathrm{ss}}\oplus V'^{\mathrm{ss}}$, and let $c_a$ and $c'_b$ be the
scalars by which its central element of degree $N$ acts on the
composition factors $A_a$ of $V$ and $A'_b$ of $V'$. By
Lemma [sk-p-readout],
$\gamma_a=\lambda_\iota(c_a)/N$ and
$\operatorname{dw}_\iota(A'_b)=\lambda_\iota(c'_b)/N$.

(1) The central element acts by $c_ac'_b$ on $A_a\otimes A'_b$, and hence
on every simple factor of it, whose determinant weight is therefore
$\gamma_a+\operatorname{dw}_\iota(A'_b)$ by the same lemma. Each
$A_a\otimes A'_b$ is nonzero, and Lemma [sk-r-linear-library]
identifies the simple factors of these tensor products with those of
$V\otimes V'$.

(2) The central element acts on $\bigotimes_a\bigwedge^{n_a}A_a$ by
$\prod_ac_a^{n_a}$, so each simple factor of this nonzero representation
has determinant weight $\sum_an_a\gamma_a$, and
Lemma [sk-r-linear-library] identifies these factors with those of
$\bigwedge^rV$.

(3) We have $\det(s\mid A^\vee)=\det(s\mid A)^{-1}$, and duality carries a
composition series of $V$ to one of $V^\vee$ whose factors are the duals
$A_a^\vee$.
