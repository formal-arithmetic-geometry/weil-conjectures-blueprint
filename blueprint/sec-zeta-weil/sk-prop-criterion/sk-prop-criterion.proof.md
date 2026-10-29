+++
kind  = "proof"
of    = "sk-prop-criterion"
+++
We first show that (2) and (3) are equivalent. For
(3)$\Rightarrow$(2), a nonzero $k\times k$ minor of a finite submatrix
gives $k$ linearly independent rows, so every finite submatrix has
rank at most the dimension of the row span. For (2)$\Rightarrow$(3),
let $R_{j_1},\ldots,R_{j_m}$ be linearly independent. On their span
the coordinate functionals have common kernel zero, so they span its
dual, and $m$ of them already do. The corresponding $m\times m$ minor
is then nonzero, and hence $m$ is at most the bound in (2).

Suppose that $QC=P$ with $Q(0)=1$. Comparing coefficients, we obtain a
fixed linear recurrence for all sufficiently large indices, and the
same recurrence expresses every sufficiently late row in terms of a
fixed finite list of earlier rows. This proves (3).
Conversely, assume (3). The left shift $S(v)_n=v_{n+1}$ preserves the
finite-dimensional row span $V$, since $S(R_j)=R_{j+1}$. Let $e$ be
evaluation at coordinate zero and $v=R_0$. In any basis of $V$, with
$M$ the matrix of the shift, we have

$$
 C(T)=e(I-TM)^{-1}v
     =\frac{e\operatorname{adj}(I-TM)v}{\det(I-TM)}.
$$

Here the denominator has constant coefficient one, and the identity
follows coefficient by coefficient from the geometric series of the
matrix $TM$. This proves (1).

Finally, condition (2) involves only the coefficients $c_n\in K$, and
the rank of a matrix with entries in $K$ does not change when we pass
to $K'$. Hence (2) holds over $K$ if and only if it holds over $K'$.
Applying (1)$\Rightarrow$(2) over $K'$ and (2)$\Rightarrow$(1) over
$K$, we obtain the descent of rationality.
