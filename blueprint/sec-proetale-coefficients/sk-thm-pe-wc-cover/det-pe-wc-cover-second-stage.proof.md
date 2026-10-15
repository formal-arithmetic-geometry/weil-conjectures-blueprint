+++
kind = "proof"
of = "det-pe-wc-cover-second-stage"
+++
*Preliminaries.* Clopen subsets of $\operatorname{Spec}C$ correspond to idempotents of $C$,
and preimages under $\pi$ of clopen subsets of $P$ are clopen, so $e_U$ exists. A closed
$Z$ in the profinite space $P$ is the intersection of its clopen neighbourhoods, so
$\operatorname{Spec}C_Z=\bigcap_U\pi^{-1}(U)=\pi^{-1}(Z)$, and localizing at idempotents
does not change local rings: $(C_Z)_x=C_x$ for $x\in\pi^{-1}(Z)$. Each $f(A)$ is compact,
hence closed. The partitions $\mathcal Q$ form a directed set under refinement (common
refinements by intersections), and $C_{f(A)}\to C_{f(A')}$ exists since $f(A')\subset f(A)$.

*1.* Each $C_{e_U}=C[1/e_U]$ is a principal localization, so $C_Z$ is a filtered colimit of
principal localizations, and $D_{\mathcal Q}$, a finite product of such colimits, is a
filtered colimit of finite products of principal localizations (finite products commute
with filtered colimits). Hence $D$ is a filtered colimit of finite products of principal
localizations of $C$, i.e. ind-Zariski [def-weil-pbc-ind-etale-algebra], so ind-étale and
flat ([lem-weil-pbc-ind-etale-stability]). Surjectivity on spectra follows from 2: for
$x\in\operatorname{Spec}C$ choose $s$ with $f(s)=\pi(x)$.

*2.* The spectrum of a filtered colimit of rings is the limit of the spectra. A prime of
$D_{\mathcal Q}$ is a part $A\in\mathcal Q$ together with a point
$x\in\pi^{-1}(f(A))$. A compatible family is therefore a point $x$ together with a
decreasing system of parts $A_{\mathcal Q}$ with $\pi(x)\in f(A_{\mathcal Q})$ for all
$\mathcal Q$. Since clopen partitions separate the points of the compact space $S$, the
$A_{\mathcal Q}$ have intersection a single point $s$, and every $s$ arises. Moreover
$\bigcap_{\mathcal Q}f(A_{\mathcal Q})=\{f(s)\}$: if $p$ lies in all $f(A_{\mathcal Q})$, the
nonempty compact sets $f^{-1}(p)\cap A_{\mathcal Q}$ are directed downwards, so their
intersection, contained in $\{s\}$, is nonempty and $f(s)=p$. Hence the points of
$\operatorname{Spec}D$ are the pairs $(x,s)$ with $\pi(x)=f(s)$. The map to $S$ is
continuous: the idempotents of $D_{\mathcal Q}$ indexed by the parts give continuous maps
$\operatorname{Spec}D\to\mathcal Q$, whose limit is the map to $S=\varprojlim\mathcal Q$.
The local ring at $(x,s)$ is $\varinjlim_{\mathcal Q}(C_{f(A_{\mathcal Q})})_x=C_x$.

*3.* If $x$ is closed in $\operatorname{Spec}C$, the closure of $(x,s)$ lies in the preimage
of $\{x\}$ and in the preimage of $\{s\}$ ($S$ is Hausdorff), so $(x,s)$ is closed. Let
$x$ be arbitrary with closed specialization $m$ (unique, as $C$ is w-local), so
$\pi(m)=\pi(x)=f(s)$ by [det-pe-wlocal-components]. The primes of the local ring
$D_{(m,s)}=C_m$ are generalizations of $(m,s)$; the one corresponding to $x$ lies over $x$
and over $s$ (a generalization of a point over $s$ lies over $s$, since points of $S$ are
closed), so by 2 it is $(x,s)$. Thus every point $(x,s)$ specializes to $(m,s)$, so the
closed points are exactly the $(m,s)$ with $m$ closed. Any closed specialization of
$(x,s)$ lies over $s$ and over a closed specialization of $x$, hence equals $(m,s)$. The
closed point set is the preimage of the closed set $(\operatorname{Spec}C)^c$, so it is
closed, and $\operatorname{Spec}D$ is w-local. The map $(\operatorname{Spec}D)^c\to S$,
$(m,s)\mapsto s$, is bijective (each component $\pi^{-1}(f(s))$ of $\operatorname{Spec}C$
has exactly one closed point) and continuous between compact Hausdorff spaces
([det-pe-wlocal-components]), hence a homeomorphism.

*4.* By 2 and 3, the local rings of $D$ at closed points are the rings $C_m$, $m$ maximal,
which are strictly henselian; so $D$ is w-strictly local. By 3 and
[det-pe-wlocal-components], $\pi_0(\operatorname{Spec}D)\cong(\operatorname{Spec}D)^c\cong S$,
which is extremally disconnected.
