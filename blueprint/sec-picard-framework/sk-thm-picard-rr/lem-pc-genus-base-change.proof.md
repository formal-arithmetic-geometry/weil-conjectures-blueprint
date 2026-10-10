+++
kind  = "proof"
of    = "lem-pc-genus-base-change"
+++
The base change $X_K=X\times_{\operatorname{Spec} k}\operatorname{Spec} K$ is proper over $K$
(base change of proper [lem-pc-proper-base-change]), and the
structure morphism $X\to\operatorname{Spec} k$ is proper, so by
[lem-sc-flat-base-change-coherent] (the affine/flat base change
case, applied with the flat $k$-algebra
$K$):

$$
H^1(X_K,\mathcal{O}_{X_K})\cong H^1(X,\mathcal{O}_X)\otimes_kK,
$$

whence $\dim_KH^1(X_K,\mathcal{O}_{X_K})=\dim_kH^1(X,\mathcal{O}_X)=g(X)$.
