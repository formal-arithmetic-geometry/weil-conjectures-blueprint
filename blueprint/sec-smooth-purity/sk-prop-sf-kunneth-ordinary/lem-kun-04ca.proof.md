+++
kind  = "proof"
of    = "lem-kun-04ca"
+++
For an etale $V\to X$ one has $(i_*F)(V)=F(V\times_XZ)$ by
[def-weil-pbc-direct-image]; for an etale $V\to Z$ the composite
$V\to Z\to X$ is etale and $V\times_XZ=V$, so the restriction of
$i_*F$ to $Z_{\Et}$ is $F$, i.e. $i^{-1}i_*=\mathrm{id}$ by [def-weil-pbc-inverse-image]; in
particular $i_*$ is fully faithful ([prop-openclosed-lowerstar-fully-faithful]).
For the essential image, let $F$ be a sheaf on $X_{\Et}$ with
$\kunsupp F\subseteq Z$ and consider the canonical map
$F\to i_*i^{-1}F$. At a geometric point $\bar x$ of $X$ with
$x\in Z$, the pointed etale neighbourhoods $W\to X$ of $\bar x$
have $W\times_XZ$ cofinal among the pointed etale neighbourhoods of
$\bar x$ in $Z$ by [lemma-openclosed-stalk-lowerstar] (an etale neighbourhood of $\bar x$ in $Z$
extends to one in $X$ by composing with $i$), so
$(i_*i^{-1}F)_{\bar x}=F_{\bar x}$ by
[def-weil-pbc-geometric-stalks]; at a geometric point with
$x\notin Z$, the open complement $X\setminus Z$ provides cofinal
neighbourhoods $W\subseteq X\setminus Z$ with $W\times_XZ=\emptyset$,
so both stalks vanish (for $F$ this is the support hypothesis).
Hence $F\to i_*i^{-1}F$ is an isomorphism on every geometric stalk,
and therefore an isomorphism by
lem:weil-pbc-geometric-stalk-conservative.
