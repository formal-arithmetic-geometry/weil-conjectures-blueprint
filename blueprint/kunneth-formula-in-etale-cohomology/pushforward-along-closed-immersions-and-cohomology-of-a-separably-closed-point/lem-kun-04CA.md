+++
id = "lem-kun-04CA"
kind = "lemma"
title = "Pushforward along a closed immersion"
order = 6050
lean = ["AlgebraicGeometry.Etale.closedImmersion_pushforward_fullyFaithful"]
uses = ["def-kun-support"]
+++
Let $i:Z\to X$ be a closed immersion of schemes. The functor
$i_*:\Ab(Z_{\Et})\to\Ab(X_{\Et})$ is fully faithful, $i^{-1}$ is a left
inverse, and the essential image consists of those abelian sheaves on
$X_{\Et}$ whose support [def-kun-support] is contained in $Z$.

## Proof

For an étale $V\to X$ one has $(i_*F)(V)=F(V\times_XZ)$; for an étale
$V\to Z$ the composite $V\to Z\to X$ is étale and $V\times_XZ=V$, so the
restriction of $i_*F$ to $Z_{\Et}$ is $F$, i.e.
$i^{-1}i_*=\mathrm{id}$; in particular $i_*$ is fully faithful.

For the essential image, let $F$ be a sheaf on $X_{\Et}$ with
$\operatorname{Supp}F\subseteq Z$ and consider the canonical map
$F\to i_*i^{-1}F$. At a geometric point $\bar x$ of $X$ with $x\in Z$, the
pointed étale neighbourhoods $W\to X$ of $\bar x$ have $W\times_XZ$ cofinal
among the pointed étale neighbourhoods of $\bar x$ in $Z$ (an étale
neighbourhood of $\bar x$ in $Z$ extends to one in $X$ by composing with
$i$), so $(i_*i^{-1}F)_{\bar x}=F_{\bar x}$; at a geometric point with
$x\notin Z$, the open complement $X\setminus Z$ provides cofinal
neighbourhoods $W\subseteq X\setminus Z$ with $W\times_XZ=\emptyset$, so
both stalks vanish (for $F$ this is the support hypothesis).

Hence $F\to i_*i^{-1}F$ is an isomorphism on every geometric stalk, and
therefore an isomorphism.

Unresolved dependencies: def:weil-pbc-direct-image, def:weil-pbc-scheme-conventions, def:weil-pbc-geometric-stalks, def:weil-pbc-inverse-image, lem:weil-pbc-geometric-stalk-conservative
