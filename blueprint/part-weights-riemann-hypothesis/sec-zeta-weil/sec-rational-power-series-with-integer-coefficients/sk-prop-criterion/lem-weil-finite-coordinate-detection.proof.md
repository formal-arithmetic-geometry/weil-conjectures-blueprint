+++
kind  = "proof"
of    = "lem-weil-finite-coordinate-detection"
+++
The finite-dimensionality in
[def-weil-finite-dimensional-subspace] permits induction on
the nonnegative integer $\dim_K V$.
Start with $W=V$ and $J=\varnothing$. If $W\neq0$, choose
$v\in W\setminus\{0\}$ and an index $j$ with $v_j\neq0$.
Replace $W$ by the kernel of the nonzero coordinate functional
$w\mapsto w_j$ on $W$, and add $j$ to $J$.
The dimension strictly decreases. After at most $\dim_K V$ steps,
the intersection of the selected coordinate kernels is zero.
This is exactly the injectivity asserted.
