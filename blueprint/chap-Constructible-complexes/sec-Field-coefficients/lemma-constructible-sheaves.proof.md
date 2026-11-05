+++
kind = "proof"
of = "lemma-constructible-sheaves"
order = 270
uses = ["proposition-pro-etale-coverings", "proposition-ctf-equals-bc", "lemma-lattices-lisse-e-sheaves", "lemma-comparison-completed-coefficients", "lemma-descent-lisse-qbar-sheaves-finite", "proposition-topos-functoriality", "proposition-extension-zero-restriction-closed-subscheme", "lemma-constructible-sheaves--1", "lemma-constructible-sheaves--2", "lemma-constructible-sheaves--3", "lemma-constructible-sheaves--4", "lemma-constructible-sheaves--5", "lemma-constructible-sheaves--6", "lemma-constructible-sheaves--7"]
+++
Part (1) is the substantial one. All three closure properties are local on a common
stratification, so it suffices to treat lisse sheaves on a single stratum,
and there the only difficulty is the kernel of a morphism. Parts (2) and
(3), by contrast, are formal.

(1) Given finitely many constructible sheaves, we refine their
stratifications to a common one. Then all three closure properties can
be checked on a single stratum $S$.

*Extensions.* Let $0\to F'\to F\to F''\to0$ be exact with $F'$ and
$F''$ lisse on $S$. After passing to a cover, $F'$ and $F''$ are free.
Since $F\to F''$ is surjective, after a further cover a basis of $F''$
lifts to sections of $F$. Hence the sequence splits locally, and
$F$ is locally free of finite rank.

*Kernels and cokernels.*
Locally, a morphism of lisse sheaves is a matrix of continuous
functions to $E$, and a priori its kernel need not be locally free. Once
we choose lattices, however, the morphism becomes a constant matrix on
a suitable pro-étale cover, because its reductions are maps of finite
locally constant sheaves. The kernel and cokernel of a constant matrix
over $E$ are constant of finite rank, and since being lisse is a local
property for the pro-étale topology, this suffices.

First let $\Lambda=E$ and let $f:L\to L'$ be a morphism of lisse
sheaves on $S$. By Lemma [lemma-lattices-lisse-e-sheaves] we may replace $S$
by a connected quasi-compact affine étale neighbourhood $V$ on which
$L$ and $L'$ contain lattices $M$ and $N$. On a finite
quasi-compact pro-étale covering trivializing both lattices, the matrix
entries of $f$ have a common denominator, so $h=\pi_E^mf$ maps $M$ into
$N$ for some $m\ge0$.

The reductions $M_n=M/\pi_E^nM$ and $N_n=N/\pi_E^nN$ are finite locally
constant étale sheaves, and $M=\varprojlim M_n$, $N=\varprojlim N_n$ by
Lemma [lemma-comparison-completed-coefficients], checked where $M$ and $N$ are
free. Fix a geometric point $\bar v$ of $V$. Then the completed fibres
$M_{\bar v}=\varprojlim(M_n)_{\bar v}$ and
$N_{\bar v}=\varprojlim(N_n)_{\bar v}$ are finite free
$\mathcal O_E$-modules with continuous $\pi_1(V,\bar v)$-actions, and
the reductions of $h$ give an equivariant map $h_{\bar v}$ between them.
To make $h$ constant, note that each $M_n$ and $N_n$ becomes constant on a connected finite étale
cover of the connected scheme $V$, and we may choose these covers to form
a tower. Their inverse limit $V'\to V$ is a connected pro-étale
covering, so maps between constant sheaves on $V'$ are constant.
On $V'$ the lattices $M$ and $N$ are identified
with the constant sheaves attached to $M_{\bar v}$ and $N_{\bar v}$, and
$h$ with the constant matrix $h_{\bar v}$. Hence on $V'$ the kernel and
the cokernel of $f=\pi_E^{-m}h$ are the constant sheaves attached to the
kernel and the cokernel of $h_{\bar v}\otimes_{\mathcal O_E}E$. In particular
they are lisse.

For $\Lambda=\overline{\mathbf Q}_\ell$, we descend $L$, $L'$ and $f$ to a finite extension
$E/\mathbf Q_\ell$ by Lemma [lemma-descent-lisse-qbar-sheaves-finite]. Since the
functor $\QbarX\otimes_{E_X}-$ is exact, it takes the kernel and cokernel
over $E$ to those of $f$. Finally, restriction to strata is exact, so the
kernel and cokernel of a morphism of constructible sheaves on $X$ are
constructible.

(2) We choose the sites in a fixed universe. Up to isomorphism, a
constructible sheaf is then determined by a finite stratification and, on
each stratum, descent data of finite rank on a covering, and these data form a
set.

(3) By Noetherian induction we refine the stratification of $F$ so that
there is an open stratum $j:U\hookrightarrow X$ with closed complement
$i:Z\hookrightarrow X$ that is again a union of strata. The exact sequence
$0\to j_!j^*F\to F\to i_*i^*F\to0$ separates the stratum $U$ from the rest,
and here $j^*F$ is lisse. Applying the same step to $i^*F$ on $Z$ and iterating,
we obtain a finite filtration of $F$ whose subquotients are $a_!(F|_S)$ for
the strata $a:S\hookrightarrow X$, and each $F|_S$ is lisse.
