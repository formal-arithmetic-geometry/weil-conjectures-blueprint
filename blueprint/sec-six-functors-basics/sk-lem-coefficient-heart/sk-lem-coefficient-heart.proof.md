+++
kind  = "proof"
of    = "sk-lem-coefficient-heart"
uses = ["sk-lem-lattice-atlas", "sk-prop-sfb-qlbar-colimit-x", "sk-lem-lisse-finite-descent"]
+++
(1) Given finitely many constructible sheaves, we refine their stratifications to a common
one. Then all three closure properties can be checked on a single stratum $S$. Details:
[det-lem-coefficient-heart-common-stratification].

*Extensions.* Let $0\to F'\to F\to F''\to0$ be exact with $F'$ and $F''$ lisse on $S$. After
passing to a cover, $F'$ and $F''$ are free. Since $F\to F''$ is surjective, after a further
cover a basis of $F''$ lifts to sections of $F$. Hence the sequence splits locally, and $F$ is
locally free of finite rank.

*Kernels and cokernels.* A morphism of lisse sheaves is, locally, a matrix of continuous
functions to $E$, and its kernel need not be locally free. Once we choose lattices, however,
the morphism becomes a constant matrix on a suitable pro-étale cover, because its reductions
are maps of finite locally constant sheaves. The kernel and cokernel of a constant matrix
over $E$ are constant of finite rank, and since being lisse is a local property for the
pro-étale topology, this suffices.

First let $\Lambda=E$ and let $f\colon L\to L'$ be a morphism of lisse sheaves on $S$. By
[sk-lem-lattice-atlas] we may replace $S$ by a connected quasi-compact affine étale
neighbourhood $V$ on which $L$ and $L'$ contain lattices $M$ and $N$. On a finite
quasi-compact pro-étale covering trivializing both lattices, the matrix entries of $f$ have a
common denominator, so $h=\pi_E^mf$ maps $M$ into $N$ for some $m\ge0$.

The reductions $M_n=M/\pi_E^nM$ and $N_n=N/\pi_E^nN$ are finite locally constant étale
sheaves, and $M=\varprojlim M_n$, $N=\varprojlim N_n$ by [sk-prop-sfb-qlbar-colimit-x], checked
where $M$ and $N$ are free. Fix a geometric point $\bar v$ of $V$. The completed fibres
$M_{\bar v}=\varprojlim(M_n)_{\bar v}$ and $N_{\bar v}=\varprojlim(N_n)_{\bar v}$ are finite free
$\cO_E$-modules with continuous $\pi_1(V,\bar v)$-actions, and the reductions of $h$ give an
equivariant map $h_{\bar v}$ between them. Each $M_n$ and $N_n$ becomes constant on a connected
finite étale cover of the connected scheme $V$, and we may choose these covers to form a
tower. Their inverse limit $V'\to V$ is a connected pro-étale covering, so that maps between
constant sheaves on $V'$ are constant. On $V'$ the lattices $M$ and $N$ are identified with
the constant sheaves attached to $M_{\bar v}$ and $N_{\bar v}$, and $h$ with the constant
matrix $h_{\bar v}$. Hence on $V'$ the kernel and the cokernel of $f=\pi_E^{-m}h$ are the
constant sheaves attached to the kernel and the cokernel of $h_{\bar v}\otimes_{\cO_E}E$, and
they are lisse.

For $\Lambda=\Qlb$, [sk-lem-lisse-finite-descent] descends $L$, $L'$ and $f$ to a finite
extension $E/\mathbf Q_\ell$, and the exact functor $\QbarX\otimes_{E_X}-$ carries the kernel
and cokernel over $E$ to those of $f$. Finally, restriction to strata is exact, so the kernel
and cokernel of a morphism of constructible sheaves on $X$ are constructible. A second route,
through the Bhatt–Scholze result that kernels and cokernels of maps of lisse sheaves on a
topologically Noetherian scheme are lisse, is [det-lem-coefficient-heart-closure].

(2) We choose the sites in a fixed universe. Up to isomorphism, a constructible sheaf is
determined by a finite stratification and, on each stratum, descent data of finite rank on a
covering. These data form a set. Details: [det-lem-coefficient-heart-small].

(3) By Noetherian induction we refine the stratification of $F$ so that there is an open
stratum $j\colon U\hookrightarrow X$ with closed complement $i\colon Z\hookrightarrow X$ that is
again a union of strata. The exact sequence $0\to j_!j^*F\to F\to i_*i^*F\to0$ separates the
stratum $U$ from the rest, and $j^*F$ is lisse. Applying the same step to $i^*F$ on $Z$ and
iterating, we obtain a finite filtration of $F$ whose subquotients are $a_!(F|_S)$ for the
strata $a\colon S\hookrightarrow X$, and each $F|_S$ is lisse. Details:
[det-lem-coefficient-heart-filtration].
