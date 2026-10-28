+++
kind  = "proof"
of    = "sk-prop-walg-determinant-weights"
+++
Apply [sk-p-central] to $V^{\mathrm{ss}}\oplus V'^{\mathrm{ss}}$, and let
$c_a$ and $c'_b$ be the scalars by which its central element of degree $N$
acts on the composition factors $A_a$ of $V$ and $A'_b$ of $V'$. By
[sk-p-readout], $\gamma_a=\lambda_\iota(c_a)/N$ and
$\dw_\iota(A'_b)=\lambda_\iota(c'_b)/N$. The finite geometric determinants
required there hold for every Weil representation by
[sk-d-real-detweights] ([lem-rp-determinant-weights-agree]).

(1) The central element acts by $c_ac'_b$ on $A_a\otimes A'_b$, and hence
on every simple factor of it, whose determinant weight is therefore
$\gamma_a+\dw_\iota(A'_b)$ by the same lemma. Each $A_a\otimes A'_b$ is
nonzero, and [sk-r-linear-library] identifies the simple factors of these
tensor products with those of $V\otimes V'$ ([prop-walg-tensor-determinant-weights],
[prop-ag-det-weight-two-factor-tensor]).

(2) The central element acts on $\bigotimes_a\bigwedge^{n_a}A_a$ by
$\prod_ac_a^{n_a}$, so each simple factor of this nonzero representation
has determinant weight $\sum_an_a\gamma_a$, and [sk-r-linear-library]
identifies these factors with those of $\bigwedge^rV$ ([prop-walg-exterior-determinant-weights],
[prop-ag-det-weight-exterior], [cor-mg-det-weight-exterior]).

In particular every simple factor of $V^{\otimes m}$ has determinant weight
at most $m\max\operatorname{DW}(V)$ ([cor-mg-det-weight-finite-tensor]).
