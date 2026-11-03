+++
kind  = "proof"
of    = "lem-fin-projective-flat-coherent-ranks"
+++
By [lem-pc-projective-noetherian-rf-perfect], locally on a
finite affine cover of $S$, the coherent derived direct image is
represented by a bounded complex $C^\bullet$ of finite projective
modules. A further finite open cover makes its finitely many terms
free, by [def-pc-perfect-complex].
By [cor-pc-projective-noetherian-rf-perfect-base-change],
$C^\bullet\otimes\kappa(\bar s)$ computes the displayed fibre
cohomology. If $c_r$ is the rank of $C^r$ on this open, then

$$
h^r(\bar s)=c_r-\operatorname{rank}(d^{r-1}_{\bar s})
-\operatorname{rank}(d^r_{\bar s}).
$$

A matrix has rank exactly $t$ where all its $(t+1)$-minors
vanish and at least one $t$-minor is nonzero; rank zero is defined
by vanishing of all entries. These are finite unions of locally
closed subsets, and there are only finitely many possible ranks.
Intersect the partitions for the two matrices to obtain a finite
locally closed partition on which $h^r$ is constant. Refine the
finitely many base-open partitions to a partition of $S$.
Thus constructibility has been obtained from explicit matrices.
It does not use etale direct-image finiteness.
