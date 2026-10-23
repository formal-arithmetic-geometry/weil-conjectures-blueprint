+++
kind  = "proof"
of    = "sk-prop-criterion"
+++
A finite-dimensional space of sequences is detected by finitely many
coordinates. Indeed, the coordinate functionals have common kernel
zero and therefore span its dual, and a finite subset of them already
spans it. Thus independent rows have a nonzero minor on finitely many
columns, and conversely a nonzero minor gives independent rows. This
proves the equivalence of (2) and (3).

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

Finally, each finite minor has its entries in $K$, so if all minors of
some size vanish in $K'$, they already vanish in $K$. Applying
(2)$\Rightarrow$(1) over $K$, we obtain the descent of rationality.
