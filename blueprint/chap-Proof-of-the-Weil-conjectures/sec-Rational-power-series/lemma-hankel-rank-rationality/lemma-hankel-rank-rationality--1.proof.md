+++
kind = "proof"
of = "lemma-hankel-rank-rationality--1"
order = 1376003
uses = []
+++
Suppose that $CQ=P$ with $Q(0)=1$, and write $Q(T)=\sum_i q_iT^i$.
Set $d=\max(\deg Q,1)$. Comparing coefficients gives, for all
sufficiently large $n$,

$$
c_n=-\sum_{i=1}^d q_i c_{n-i}.
$$

For every sufficiently large $j$, this identity holds at $n=j+s$
for all $s\geq0$, and hence
$R_j=-\sum_{i=1}^d q_iR_{j-i}$. Strong induction on $j$ puts every
row in the span of a fixed finite list of initial rows.

Conversely, let $V$ be the finite-dimensional row span. The shift
$S(v)_n=v_{n+1}$ preserves $V$, since $S(R_j)=R_{j+1}$.
Let $p(U)=\sum_{j=0}^e p_jU^j$ be its characteristic polynomial.
By Cayley--Hamilton, $p(S)R_0=0$, and evaluation at coordinate $n$
gives

$$
\sum_{j=0}^e p_jc_{n+j}=0\qquad(n\geq0).
$$

Put $Q(T)=\sum_{i=0}^e p_{e-i}T^i$, the reversed characteristic
polynomial. Since $p$ is monic, $Q(0)=1$. The recurrence shows that
every coefficient of $CQ$ in degree at least $e$ vanishes. Taking
$P$ to be the truncation of $CQ$ to degrees below $e$ gives $CQ=P$.
