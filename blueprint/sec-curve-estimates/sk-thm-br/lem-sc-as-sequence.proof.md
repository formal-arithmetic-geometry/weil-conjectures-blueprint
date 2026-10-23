+++
kind  = "proof"
of    = "lem-sc-as-sequence"
+++
The map $\wp$ is additive since $p=0$ on every etale $X$-scheme. The
constant sheaf $\mathbf F_p$ maps into $\ker\wp$ since $c^p=c$ for
$c\in\mathbf F_p$. Conversely, let $V\to X$ be etale and $y\in\mathcal O(V)$
with $y^p=y$. Since $y^p-y=\prod_{c\in\mathbf F_p}(y-c)$ and the elements
$y-c$ are pairwise comaximal (their differences are units of $\mathbf F_p$),
the Chinese remainder theorem decomposes $V$ into the disjoint union of the
open and closed pieces $\{y=c\}$; so $y$ is a locally constant
$\mathbf F_p$-valued function, i.e. a section of $\mathbf F_p$. This
identifies $\mathbf F_p$ with $\ker\wp$.

For surjectivity, let $U\to X$ be etale and $f\in\mathbf G_a(U)=\mathcal
O_U(U)$. The $\mathcal O_U(U)$-algebra $\mathcal O_U(U)[y]/(y^p-y-f)$ is free
of rank $p$, hence faithfully flat, and etale because the derivative of
$y^p-y-f$ is $-1$, a unit. Its base change along
$U\to\operatorname{Spec}\mathcal O_U(U)$ is a surjective etale
$V\to U$ on which $\wp(y)=f$; therefore $\wp$ is surjective as a morphism
of etale sheaves.
