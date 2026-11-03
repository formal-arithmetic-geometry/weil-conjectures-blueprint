+++
kind  = "proof"
of    = "cor-nagata-conrad-proper-target-extension"
uses = ["lem-weil-pbc-closed-immersion-from-composite", "thm-nagata-conrad-elimination"]
+++
Put $P=Y\times_SX$ and let $p\colon P\to X$ be the second projection. As a
base change of the proper morphism $y$, the morphism $p$ is proper; in
particular it is separated, of finite type and quasi-compact. Since $X$ is
quasi-compact and quasi-separated and $p$ is quasi-compact and
quasi-separated, $P$ is quasi-compact and quasi-separated as well.

The pair $(f,U\hookrightarrow X)$ defines a morphism $s\colon U\to P$ with
$p\circ s$ the inclusion of $U$, i.e. a section of $p$ over $U$. It factors
through the open $p^{-1}(U)$, and there it is a section of the separated
morphism $p^{-1}(U)\to U$; by
[lem-weil-pbc-closed-immersion-from-composite] (applied with $p\circ s$
the identity of $U$, a closed immersion) it is a closed immersion, so its
image is closed in $p^{-1}(U)$.

Apply [thm-nagata-conrad-elimination] with $V=U$ to the section $s$ of $p$.
It gives a $U$-admissible blow-up $\pi\colon\widetilde X\to X$, an open
$W\subseteq\widetilde X$ containing $\pi^{-1}(U)$ and a morphism
$g\colon W\to P$ with $p\circ g=\pi|_W$, extending $s\circ\pi$ on
$\pi^{-1}(U)$, whose graph is closed in $P\times_X\widetilde X$.

The open $W$ is dense in $\widetilde X$. Indeed, let $\mathcal I$ be the
center, so $U\subseteq X\setminus V(\mathcal I)$. The blow-up is an
isomorphism over $X\setminus V(\mathcal I)$, and $U$ is dense there, so
$\pi^{-1}(U)$ is dense in $\pi^{-1}(X\setminus V(\mathcal I))$. The latter
contains the complement of the exceptional divisor
$V(\mathcal I\mathcal O_{\widetilde X})$, an effective Cartier divisor
(locally cut out by a nonzerodivisor), whose complement is dense. Hence
$\pi^{-1}(U)\subseteq W$ is dense.

Thus $(W,g)$ is a quasi-domination of $\widetilde X$ over $P$, both viewed
as schemes over $X$. Since $P\to X$ is proper,
[lemma-nagata-conrad-quasi-domination-proper-target] (with base $X$) gives
$W=\widetilde X$. Put $\widetilde f=\mathrm{pr}_Y\circ g\colon\widetilde X\to Y$.
Then $y\circ\widetilde f=x\circ p\circ g=x\circ\pi$, and on $\pi^{-1}(U)$
we get $\widetilde f=\mathrm{pr}_Y\circ s\circ\pi=f\circ\pi$.
