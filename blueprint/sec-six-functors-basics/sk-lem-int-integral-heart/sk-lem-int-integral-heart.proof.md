+++
kind = "proof"
of = "sk-lem-int-integral-heart"
uses = ["sk-lem-integral-models", "sk-def-sfb-constructible"]
+++
By [sk-lem-integral-models](1),(2), restriction of scalars to the constant
sheaf $\underline{\mathcal O_E}$, which is flat, identifies
$\Dbc(X,\mathcal O_E)$ with the category $\Dc(X,\mathcal O_E)$ of the Stacks
Project (Stacks, Tags 099I, 099L). The two conditions of the definition of
constructibility ([sk-def-sfb-constructible]), derived completeness and
constructibility of the reduction modulo $\pi_E$, are stable under cones and
shifts, so $\Dbc(X,\mathcal O_E)$ is triangulated, and its objects are bounded
because our schemes are quasi-compact (Stacks, Tag 09C2).

The local structure is the key point, and it is Stacks, Tag 09C7, whose
Noetherian hypothesis holds for our schemes (since $\mathcal O_E$ is already
complete, the completed coefficient ring of Stacks, Tag 09C4 is
$\mathcal O_E$ itself). The statement is: *for $K\in\Dbc(X,\mathcal O_E)$ there
is a finite stratification of $X$ such that on each stratum $K$ is pro-étale
locally the completion of a bounded complex $M^\bullet$ of finite free
$\mathcal O_E$-modules, with differentials given by matrices over
$\mathcal O_E$.* The idea of the proof is that the reduction $K/\pi_E$ is a
classical constructible complex, hence on a stratum is locally a perfect
complex of $\mathcal O_E/\pi_E$-modules; on a weakly contractible cover, where
cohomology vanishes in positive degrees, such a perfect complex and its
successive deformations to $\mathcal O_E/\pi_E^n$ can be lifted compatibly,
and the derived limit of the lifts is $K$ by completeness. As
$\underline{\mathcal O_E}\to\mathcal O_{E,X}$ is flat, $H^q(K)$ is then locally
the completion of the finitely generated $\mathcal O_E$-module
$H^q(M^\bullet)$; this is (2) once we know that $H^q(K)$ lies in
$\Cons(X,\mathcal O_E)$.

First, $H^q(K)$ is derived complete: the pro-étale site has enough weakly
contractible affines (Stacks, Tag 0990), and Stacks, Tag 099Q(5) then shows
that cohomology sheaves of derived complete complexes are derived complete.
Second, a finitely generated $\mathcal O_E$-module has a free resolution of
length one, in degrees $-1,0$. The reduction of $H^q(K)$ modulo $\pi_E$
therefore has cohomology only in degrees $-1$ and $0$, and on the chosen
strata these cohomology sheaves are locally constant with finite stalks,
hence come from constructible sheaves on the étale site (Stacks, Tags 099Y,
09AK). Thus $H^q(K)\in\Dbc(X,\mathcal O_E)$. Every truncation of $K$ is a
finite extension of shifts of the $H^q(K)$, so it also lies in
$\Dbc(X,\mathcal O_E)$.

Stability under truncation gives (1) for the heart: the kernel and cokernel
of a map of constructible sheaves are cohomology sheaves of its cone, and an
extension of two constructible sheaves is the middle term of a triangle with
constructible ends. Essential smallness holds because the data describing a
constructible sheaf (a finite stratification, finite presentations of
$\mathcal O_E$-modules, sheaves on a fixed small site, and gluing morphisms)
form a set. For (3), the length one free resolution of the local model gives
the derived dual and the evaluation and coevaluation maps locally, and the
Tor amplitudes can be read off from it.

For the local model $\mathcal O_E/\pi_E$ the amplitudes in (3) can be seen
directly. The resolution
$0\to\mathcal O_E\xrightarrow{\pi_E}\mathcal O_E\to\mathcal O_E/\pi_E\to0$
shows that $M\otimes^{\mathbf L}\mathcal O_E/\pi_E$ is the cone of $\pi_E$ on
$M$, which lives in degrees $[-1,0]$ for a module $M$. Applying
$R\operatorname{Hom}(-,\mathcal O_E)$ to the same resolution gives the dual
$\mathcal O_E/\pi_E[-1]$, whose Tor amplitude is $[0,1]$.
