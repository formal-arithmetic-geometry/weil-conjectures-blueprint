+++
kind  = "proof"
of    = "prop-weil-rationality-criterion"
+++
Write $R_j=(c_{j+s})_{s\geq0}$ and
$V=\operatorname{span}_K\{R_j:j\geq0\}$. We first identify the
matrix rank in [def-weil-hankel-matrix] with $\dim_K V$.
If $r$ rows are independent as infinite sequences,
[lem-weil-finite-coordinate-detection] applied to their span
shows that finitely many columns still detect their independence.
A further selection of $r$ columns gives a nonzero $r$-minor.
Conversely a nonzero finite minor makes its rows independent.
Thus bounded finite matrix ranks are equivalent to finite $\dim_K V$.

Suppose (2) holds. If $R_0=0$, all $c_n$ vanish and (3) holds
with $m=0,d=1,a_0=0$. Otherwise choose the least $d\geq1$
for which $R_0,\ldots,R_d$ are dependent. The preceding rows are
independent, so the last row has coefficient nonzero in any nontrivial relation.
Dividing by that coefficient gives
$R_d+a_{d-1}R_{d-1}+\cdots+a_0R_0=0$.
Its $n$-th coordinate is (3) with $m=0$.

Suppose (3) holds. Put
$Q(T)=1+a_{d-1}T+\cdots+a_0T^d$.
For $N\geq m+d$, the coefficient of $T^N$ in $QC$ is
zero by the recurrence with $n=N-d$. Hence $QC=P$ is a
polynomial, proving (1). For later use, (3) also directly implies
(2): for every $j\geq m$ the same recurrence in every coordinate
expresses $R_{j+d}$ in the span of $R_j,\ldots,R_{j+d-1}$.
All rows therefore lie in the span of $R_0,\ldots,R_{m+d-1}$.

Finally suppose (1) holds. Write
$Q=1+b_1T+\cdots+b_dT^d$, first taking $d\geq1$.
The coefficient identity $QC=P$, in degrees $N>\deg P$
and $N\geq d$, gives (3) with $a_{d-j}=b_j$ and sufficiently
large $m$. If $Q=1$, the coefficients of $C=P$ eventually
vanish, so take $d=1,a_0=0$ and $m$ sufficiently large.
This proves all implications.
