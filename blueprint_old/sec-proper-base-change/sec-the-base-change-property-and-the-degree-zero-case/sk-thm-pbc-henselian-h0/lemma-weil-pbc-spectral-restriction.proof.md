+++
kind  = "proof"
of    = "lemma-weil-pbc-spectral-restriction"
+++
*Step 1: specialization to $T_0$.* For $y\in T$ the closure
$\overline{\{y\}}$ is irreducible and closed, so it meets $T_0$: every point of
$T$ specializes to a point of $T_0$. If $y\rightsquigarrow z$, every open
containing $z$ contains $y$.

*Step 2: injectivity.* The stalk of $F|_{T_0}$ at $z\in T_0$ is $F_z$. If
$s\in\Gamma(T,F)$ restricts to $0$ on $T_0$, its germ at every $z\in T_0$ vanishes,
so $s$ vanishes on an open neighbourhood of each such $z$; by Step 1 that
neighbourhood contains every generization of $z$, and every point of $T$ is such a
generization. Hence all germs of $s$ vanish and $s=0$.

*Step 3: shrinking.* Let $U_j$, $A_{jk}$ be as in the statement, and put
$K_j=U_j\cap T_0$, a quasi-compact set. First, if $y\in T$ specializes to points
$w_k\in K_k$ and $w_l\in K_l$, then $y\in A_{kl}$. Otherwise the connected set
$\overline{\{y\}}\cap T_0$ would be covered by the two opens
$\bigcup_{m:\,y\in A_{km}}U_m$ and $\bigcup_{m:\,y\notin A_{km}}U_m$, both meeting
it (at $w_k$ and at $w_l$), so they would meet in a point $w$ of
$\overline{\{y\}}\cap T_0$ lying in some $U_{m_1}$ with $y\in A_{km_1}$ and some
$U_{m_2}$ with $y\notin A_{km_2}$; but $w\in U_{m_1}\cap U_{m_2}\cap T_0\subseteq
A_{m_1m_2}$, an open set, contains its generization $y$, and transitivity gives
$y\in A_{km_2}$, a contradiction.

Now let $B_j$ be the set of points of $U_j$ which are generizations of a point of
some $K_k$ but do not lie in $A_{jk}$, and put
$W_j=U_j\setminus\overline{B_j}$. The set $B_j$ is closed in the constructible
topology, and in a spectral space every point of the closure of such a set is a
specialization of one of its points. Hence, if $y$ specializes to a point of $K_j$,
then $y\notin\overline{B_j}$: otherwise some $y'\in B_j$ with $y'\rightsquigarrow y$
would specialize both into $K_j$ and into some $K_k$ with $y'\notin A_{jk}$,
contradicting the first observation. In particular $K_j\subseteq W_j$, and the
$W_j$ cover $T$, since by Step 1 every $y$ specializes to a point of some $K_j$
and then lies in $U_j$. Finally, if $y\in W_j\cap W_k$, choose $l$ with $y$
specializing into $K_l$; then $y\notin B_j\cup B_k$ gives $y\in A_{jl}\cap A_{kl}$,
and symmetry and transitivity give $y\in A_{jk}$.

*Step 4: surjectivity.* Let $t\in\Gamma(T_0,F|_{T_0})$. Since $T_0$ is closed in
the spectral space $T$, it is quasi-compact, so by the definition of the inverse
image there are finitely many quasi-compact opens $U_j$ of $T$ covering $T_0$
and sections $s_j\in F(U_j)$ whose germs at the points of $U_j\cap T_0$ are those
of $t$. Let $A_{jk}\subseteq U_j\cap U_k$ be the open set of points where $s_j$
and $s_k$ have the same germ. These sets satisfy the hypotheses of Step 3, which
gives opens $W_j$. The sections $s_j|_{W_j}$ agree on overlaps and glue to
$s\in\Gamma(T,F)$, whose germs along $T_0$ are those of $t$; so $s|_{T_0}=t$.
