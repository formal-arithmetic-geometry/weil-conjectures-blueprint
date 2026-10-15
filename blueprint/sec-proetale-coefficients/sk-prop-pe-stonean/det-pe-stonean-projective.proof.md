+++
kind = "proof"
of = "det-pe-stonean-projective"
+++
*2 $\Rightarrow$ 3.* Apply 2 to $p=q$ and $f=\mathrm{id}_S$.

*3 $\Rightarrow$ 2.* Given $p$ and $f$, the fibre product
$P=S\times_YX=\{(s,x):f(s)=p(x)\}$ is closed in $S\times X$, hence compact Hausdorff, and
its projection $q\colon P\to S$ is surjective because $p$ is. A section $\sigma$ of $q$
gives $g=\mathrm{pr}_X\circ\sigma$ with $p\circ g=f\circ q\circ\sigma=f$.

*3 $\Rightarrow$ 1.* Let $U\subset S$ be open. The space
$P=\overline U\sqcup(S\setminus U)$ (disjoint union of two closed subspaces) is compact
Hausdorff and maps onto $S$ by the inclusions. Let $\sigma$ be a section. A point of $U$
has its only preimage in the first summand, so $\sigma(U)$ lies in the closed first summand,
and by continuity so does $\sigma(\overline U)$. A point outside $\overline U$ has its only
preimage in the second summand. Hence $\sigma^{-1}(\text{first summand})=\overline U$, which
is open since the summand is clopen in $P$.

*1 $\Rightarrow$ 3.* Let $q\colon P\to S$ be a continuous surjection with $P$ compact
Hausdorff. Order the closed subsets $P'\subset P$ with $q(P')=S$ by inclusion. A chain
$(P_i)$ has lower bound $\bigcap_iP_i$: for $s\in S$ the sets $q^{-1}(s)\cap P_i$ are
nonempty, compact and totally ordered by inclusion, so their intersection is nonempty. By
Zorn's lemma there is a minimal such $P_0$; put $q_0=q|_{P_0}$. Minimality means that no
proper closed subset of $P_0$ surjects onto $S$.

For open $V\subset P_0$ put $V^*=S\setminus q_0(P_0\setminus V)$. It is open ($q_0$ is a
closed map, compact to Hausdorff), contained in $q_0(V)$ (every point of $S$ has a preimage
in $P_0$, and points of $V^*$ have none outside $V$), and nonempty if $V\neq\emptyset$
(otherwise the proper closed subset $P_0\setminus V$ would surject).

We show $q_0$ is injective. Suppose $a\neq b$ in $P_0$ with $q_0(a)=q_0(b)=s$. Choose
disjoint open neighbourhoods $A\ni a$, $B\ni b$ in $P_0$. Then $A^*\cap B^*=\emptyset$: a
point of both would have its whole (nonempty) fibre inside $A\cap B=\emptyset$. Moreover
$s\in\overline{A^*}$: for an open neighbourhood $N$ of $s$, the set $V=q_0^{-1}(N)\cap A$ is
a nonempty open set (it contains $a$), and $\emptyset\neq V^*\subset q_0(V)\cap A^*\subset
N\cap A^*$. Similarly $s\in\overline{B^*}$. By 1, $\overline{A^*}$ is open; it contains
$s\in\overline{B^*}$, hence meets $B^*$. But $B^*$ is open and disjoint from $A^*$, so it is
disjoint from $\overline{A^*}$, a contradiction.

So $q_0$ is a continuous bijection from a compact space to a Hausdorff space, hence a
homeomorphism, and $q_0^{-1}$ followed by the inclusion $P_0\subset P$ is a section of $q$.

*Total disconnectedness.* Let $S$ satisfy 1 and $x\neq y$. Choose disjoint open $U\ni x$,
$V\ni y$. Then $\overline U$ is clopen, contains $x$, and misses $y$ because the open set
$V$ is disjoint from $U$, hence from $\overline U$. So points are separated by clopen sets,
and a compact Hausdorff space with this property is profinite.
