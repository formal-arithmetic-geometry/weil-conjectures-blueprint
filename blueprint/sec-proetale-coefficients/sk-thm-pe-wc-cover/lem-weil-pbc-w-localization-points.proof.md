+++
kind  = "proof"
of    = "lem-weil-pbc-w-localization-points"
+++
Each $A_{Z(E',E'')}$ is a localization of $A$, so each $P_E$ is a finite
product of localizations and $A\to P_E$ is ind-Zariski; hence so is the
filtered colimit $A\to A^w$, by [lem-weil-pbc-ind-etale-stability]. Each
prime of $A$ lies in exactly one stratum $Z(E',E'')$ and survives in the
corresponding factor, so $A\to P_E$ is flat and surjective on spectra, i.e.
faithfully flat; a filtered colimit of faithfully flat algebras is faithfully
flat. Ind-Zariski maps identify local rings, because local isomorphisms do and
local rings commute with filtered colimits.

A prime $\mathfrak q$ of $A^w$ chooses, at every stage $E$, one stratum and a
prime of the corresponding localization. It contains $I_A$ if and only if at
every stage its image lies in the stratum itself, i.e. contains the kernel of
$A_{Z(E',E'')}\to(A/(E''))_{\prod E'}$. A prime $\mathfrak p$ of $A$ lies in
exactly one stratum for each $E$, and these choices are compatible, so there
is exactly one prime of $V(I_A)$ over $\mathfrak p$: the map
$V(I_A)\to\operatorname{Spec}A$ is bijective. Every prime $\mathfrak q$
satisfies $\mathfrak q+I_A\neq A^w$, since at each stage a prime of the
localization at a stratum specializes to a point of the stratum; so it
specializes to a point of $V(I_A)$. If $\mathfrak q$ specializes to two
points $c,c'$ of $V(I_A)$, then for each $f\in A$ the stage $E=\{f\}$ shows
that $c,c'$ lie over the same part $D(f)$ or $V(f)$, as comparable primes of a
finite product lie over the same factor; hence the images of $c$ and $c'$ in
$\operatorname{Spec}A$ contain the same elements, and $c=c'$ by the
bijection. Points of $V(I_A)$ are maximal: a prime containing one of them also
contains $I_A$, and the stagewise description shows it lies over the same
prime of $A$. Conversely a closed point specializes to a point of $V(I_A)$,
so equals it. Thus the closed points form the closed set $V(I_A)$, every
point has a unique closed specialization, and $\operatorname{Spec}A^w$ is
w-local.

If $V(J)$ consists of closed points, every prime of $A^w$ containing $JA^w$
lies over a maximal ideal of $A$ and, by the stagewise description, lies in
$V(I_A)$; the bijection $V(I_A)\to\operatorname{Spec}A$ therefore restricts
to a bijection $V(JA^w)\to V(J)$. The map $A/J\to A^w/JA^w$ is ind-Zariski
with bijective map on spectra between zero-dimensional spectra and identifies
local rings, hence is an isomorphism.
