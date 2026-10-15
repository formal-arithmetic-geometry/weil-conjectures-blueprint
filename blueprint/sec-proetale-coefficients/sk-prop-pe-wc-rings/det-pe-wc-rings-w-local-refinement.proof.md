+++
kind = "proof"
of = "det-pe-wc-rings-w-local-refinement"
+++
Let $B^w$ be the w-localization of $B$ ([def-weil-pbc-w-localization]). By
[lem-weil-pbc-w-localization-points] its points are pairs $(x,y)$ of primes of $B$ with
$y\subset x$, with local ring $B_y$ and with contraction $y$ to $B$; its closed points are
the pairs $(x,x)$, and they form a closed subset.

Since $R$ is w-local, its set of maximal ideals is closed, say $V(I)$ with $I$ radical. Let
$T\subset\operatorname{Spec}B^w$ be the set of closed points $(x,x)$ lying in
$V(IB^w)$. A closed point $(x,x)$ contracts to $x$ in $B$, so it lies in $V(IB^w)$ iff
$I\subset x\cap R$, i.e. iff $x\cap R$ is maximal. Thus $T$ is closed (an intersection of
two closed sets), consists of closed points, and corresponds to the primes of $B$ lying
over maximal ideals of $R$.

Put $B'=(B^w)_{[T]}$ ([def-weil-pbc-retained-localization]). By
[lem-weil-pbc-retained-localization], $B^w\to B'$ is ind-Zariski, its points are the points
of $\operatorname{Spec}B^w$ generalizing a point of $T$, with unchanged local rings, and,
since all points of $T$ are closed, $\operatorname{Spec}B'$ is w-local with closed point set
$T$. This gives 2 and 4, and the first half of 3. The map $B\to B^w$ is ind-Zariski, so
$B\to B'$ is ind-Zariski and $R\to B'$ is ind-étale by
[lem-weil-pbc-ind-etale-stability]; this is 1. For surjectivity in 3: a maximal ideal
$\mathfrak m$ of $R$ is the image of some prime $x$ of $B$ because $R\to B$ is faithfully
flat, and then $(x,x)\in T$ maps to $\mathfrak m$.
