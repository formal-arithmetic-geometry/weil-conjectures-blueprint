+++
kind = "proof"
of = "lemma-hankel-rank-rationality"
order = 1377
+++
The equivalence of (2) and (3) is linear algebra. For the equivalence
of (1) and (3), note that a denominator $Q$ gives a linear recurrence
among the rows. Conversely, the characteristic polynomial of the
shift on a finite-dimensional row span is a denominator. The descent
statement holds because (2) does not change when we extend the field.

For example, $C=1/(1-T)$ has all $c_n=1$, every row is $(1,1,\ldots)$,
and the row span is a line. For $C=1/(1-T)^2$ we have $c_n=n+1$, and
$R_j=R_0+j(R_1-R_0)$, so the row span is a plane.

For (3)$\Rightarrow$(2), a nonzero $k\times k$ minor of a finite submatrix
gives $k$ linearly independent rows. So every finite submatrix has
rank at most the dimension of the row span. For (2)$\Rightarrow$(3),
let $R_{j_1},\ldots,R_{j_m}$ be linearly independent. On their span
the coordinate functionals have common kernel zero. They therefore span
its dual, and $m$ of them already do. The corresponding $m\times m$
minor is nonzero, and so $m$ is at most the bound in (2).

For (1)$\Rightarrow$(3), suppose that $QC=P$ with $Q(0)=1$. Comparing
coefficients gives a fixed linear recurrence for all sufficiently
large indices, and the same recurrence expresses every sufficiently
late row in terms of a fixed finite list of earlier rows.

For (3)$\Rightarrow$(1), the left shift $S(v)_n=v_{n+1}$ preserves the
finite-dimensional row span $V$, since $S(R_j)=R_{j+1}$. Let $e$ be
evaluation at coordinate zero and $v=R_0$. In any basis of $V$, with
$M$ the matrix of the shift, we have

$$
C(T)=e(I-TM)^{-1}v
=\frac{e\operatorname{adj}(I-TM)v}{\det(I-TM)}.
$$

The first equality holds coefficient by coefficient. Indeed,
$(I-TM)^{-1}=\sum_nT^nM^n$, and $eM^nv$ is the coordinate zero of
$S^n(R_0)=R_n$, that is, $c_n$. As the denominator has constant
coefficient one, this proves (1).

For the descent, note that condition (2) involves only the
coefficients $c_n\in K$, and the rank of a matrix with entries in $K$
does not change when we pass to $K'$. So (2) holds over $K$ if and
only if it holds over $K'$. Applying (1)$\Rightarrow$(2) over $K'$
and (2)$\Rightarrow$(1) over $K$ gives the descent of rationality.
