+++
kind  = "proof"
of    = "sk-p-exterior"
+++
Choose the central element of degree $N$ of [sk-p-central] for
$V^{\mathrm{ss}}=\bigoplus_aA_a$, and let $c_a$ be its scalar on $A_a$. It
acts on $\bigotimes_a\bigwedge^{n_a}A_a$ by $\prod_ac_a^{n_a}$. Hence each
simple factor $Q$ of this nonzero tensor construction satisfies

$$
\dw_\iota(Q)=\frac{\lambda_\iota(\prod_ac_a^{n_a})}{N}=\sum_an_a\gamma_a
$$

by [sk-p-readout]. By the filtration of [sk-r-linear-library], these are
exactly the weights occurring in $\bigwedge^rV$. Grouping the indices with
equal $\gamma_a$ gives the equivalent formulation, since every tuple
$(n_\gamma)$ with $0\le n_\gamma\le m(\gamma)$ can be distributed among the
corresponding indices $a$ with $n_a\le d_a$.

For the complement, the reduction to a surjective degree map with
$\deg(\gamma)=1$ is the one in the proof of [sk-p-tensor]; the
rank-counted list is a reindexing of the sums $\sum_an_a\gamma_a$.
