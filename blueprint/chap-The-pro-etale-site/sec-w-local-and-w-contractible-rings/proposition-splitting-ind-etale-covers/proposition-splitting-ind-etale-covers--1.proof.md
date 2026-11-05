+++
kind = "proof"
of = "proposition-splitting-ind-etale-covers--1"
title = "Proof outline"
order = 56002
uses = ["proposition-etale-implications", "proposition-w-local-components", "proposition-gleason-s-theorem"]
+++
The map $R\to B$ is weakly étale by
[proposition-etale-implications]. Every prime $\mathfrak q\subset B$
is contained in a maximal ideal $\mathfrak n$. The equalities defining
$V(I)$ and $V(IB)$ imply that $\mathfrak m=\mathfrak n\cap R$ is
maximal. Thus $R_{\mathfrak m}$ is strictly henselian, and the weakly
étale local homomorphism $R_{\mathfrak m}\to B_{\mathfrak n}$ is an
isomorphism. Localizing further shows that
$R_{\mathfrak q\cap R}\to B_{\mathfrak q}$ is an isomorphism for
every $\mathfrak q$.

Faithful flatness gives a surjection
$\pi_0(\operatorname{Spec}(B))\to\pi_0(\operatorname{Spec}(R))$.
Its target is extremally disconnected, so [proposition-gleason-s-theorem]
gives a continuous section. Let $T$ be its image. Then $T$ is closed
and maps bijectively onto $\pi_0(\operatorname{Spec}(R))$.

Restrict $B$ to the components in $T$: take the filtered colimit $C$
of the localizations at idempotents corresponding to the clopen subsets
of $\operatorname{Spec}(B)$ containing those components. The map
$B\to C$ is surjective and ind-Zariski, and its map on spectra is a
closed embedding with image the union of the components in $T$.
Consequently $C$ is w-local, $R\to C$ identifies local rings, and
closed points of $\operatorname{Spec}(C)$ map to closed points of
$\operatorname{Spec}(R)$. By [proposition-w-local-components], the
choice of $T$ makes the map on connected components bijective. A
map between w-local rings preserving closed points and identifying
local rings is an isomorphism when its map on connected components is
bijective. Inverting $R\to C$ and composing with $B\to C$ gives the
required retraction.
