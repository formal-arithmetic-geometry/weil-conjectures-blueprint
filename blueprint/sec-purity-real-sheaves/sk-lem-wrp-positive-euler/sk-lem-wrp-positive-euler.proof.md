+++
kind  = "proof"
of    = "sk-lem-wrp-positive-euler"
+++
For a square matrix $A$, triangularization and the geometric series
give the formal identity

$$
 \det(1-tA)^{-1}
   =\exp\left(\sum_{n\ge1}\operatorname{Tr}(A^n)\frac{t^n}{n}\right).
$$

On an even tensor power, the trace of the $n$th power of Frobenius is
$\operatorname{Tr}(F_x^n\mid\mathcal G)^{2k}$, which is nonnegative
after applying $\iota$. Every coefficient of the exponential is then
a finite sum of products of nonnegative numbers, and this remains true
after replacing $t$ by $t^{d(x)}$ ([lem-rp-even-tensor-positivity]).

For the second assertion, write $f_j=\sum_na_{j,n}t^n$ and
$L=\sum_nA_nt^n$. Since all coefficients are nonnegative and all
constant coefficients are one, we have $0\le a_{j,n}\le A_n$. For
every $0<r<R$, Cauchy's estimate gives $|A_n|\le C_rr^{-n}$. Hence the
radius of convergence of $f_j$ is at least $r$ for every such $r$, and
so at least $R$ ([lem-rp-positive-product-radius]). Finally, a zero of $P_j$
in the disc would be a pole of $f_j=1/P_j$, which is impossible.
