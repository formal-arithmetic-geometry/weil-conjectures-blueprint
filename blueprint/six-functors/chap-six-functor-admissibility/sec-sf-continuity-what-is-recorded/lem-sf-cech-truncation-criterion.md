+++
id = "lem-sf-cech-truncation-criterion"
kind = "lemma"
title = "Truncating the Čech complex of a single weakly contractible covering needs the vanishing as input"
order = 3492
uses = ["def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site"]
+++
Let $T$ be a scheme, let $U\to T$ be a nonempty object of the
small pro-étale site $T_{\Proet}$ of
[def-weil-pbc-proetale-site], let $\mathcal F$ be a sheaf of
$A$-modules on $T_{\Proet}$, that is, an object of
[def-weil-pbc-proetale-modules], let $W\to U$ be a pro-étale covering
whose source and all of whose fibre products
$W^{n+1}=W\times_U\dots\times_UW$, $n\geq0$, are weakly contractible objects
of $T_{\Proet}$, and let $K$ be the Čech hypercover of that covering,
$K_n=\{W^{n+1}\to U\}$, the hypercovering of Stacks Project, Example 25.3.6,
[Tag 0GMA](https://stacks.math.columbia.edu/tag/0GMA). Put
$C=s(\mathcal F(K))$, the complex with $C^n=\mathcal F(W^{n+1})$ and
differentials the alternating sums of the maps induced by the face maps of
$K$. Then

$$
R\Gamma(U,\mathcal F)\cong C,
$$

and for every integer $N$ the truncation $\tau_{\leq N}C\to C$ is a
quasi-isomorphism if and only if $H^q(U,\mathcal F)=0$ for every $q>N$.
Consequently no truncation of $C$ computes $R\Gamma(U,\mathcal F)$ unless
the vanishing it is meant to establish already holds.

## Proof

The identification $R\Gamma(U,\mathcal F)\cong s(\mathcal F(K))$ is Stacks
Project, Pro-étale Cohomology, Lemma 61.14.2,
[Tag 09A2](https://stacks.math.columbia.edu/tag/09A2), applied to
$\mathcal F$ placed in degree $0$, a sheaf of $A$-modules on the small
pro-étale site $T_{\Proet}$ of [def-weil-pbc-proetale-site] being an
object of [def-weil-pbc-proetale-modules] and its terms
$W^{n+1}$ being weakly contractible by hypothesis; hence
$H^q(C)=H^q(U,\mathcal F)$ for every $q$. The complex $C$ is
concentrated in degrees $\geq0$, and its smart truncation $\tau_{\leq N}C$
agrees with $C$ in degrees $<N$, has $\ker(C^N\to C^{N+1})$ in degree
$N$ and vanishes above, so that $H^q(\tau_{\leq N}C)=H^q(C)$ for $q\leq N$
and $H^q(\tau_{\leq N}C)=0$ for $q>N$. In the long exact cohomology sequence
of the triangle $\tau_{\leq N}C\to C\to M\to$, the two outer terms therefore
vanish in degrees $>N$, and the connecting maps show
$H^q(M)\cong H^q(C)$ for every $q>N$; so $M$ is acyclic, that is, the
truncation is a quasi-isomorphism, if and only if $H^q(C)=0$ for every
$q>N$, which by the identification above is the stated vanishing. The
converse of the last sentence is immediate: a truncation concentrated in degrees
$\leq N$ has no cohomology above $N$.
