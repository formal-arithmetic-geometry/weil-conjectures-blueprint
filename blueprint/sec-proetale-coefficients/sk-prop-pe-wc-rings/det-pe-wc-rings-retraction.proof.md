+++
kind = "proof"
of = "det-pe-wc-rings-retraction"
+++
*1. Local rings.* Every prime $\mathfrak q$ of $S$ lies in a maximal ideal $\mathfrak n$,
which is a closed point and so contains $IS$; then $\mathfrak n\cap R\supset I$ is maximal,
and $R_{\mathfrak n\cap R}$ is strictly henselian since $R$ is w-strictly local. The map
$R\to S$ is weakly étale ([lem-weil-pbc-ind-etale-stability]), so
$R_{\mathfrak n\cap R}\to S_{\mathfrak n}$ is an isomorphism by [det-pe-wc-rings-local-iso],
and $R_{\mathfrak q\cap R}\to S_{\mathfrak q}$ is an isomorphism as a localization of it. In
particular closed points of $\operatorname{Spec}S$ lie over closed points of
$\operatorname{Spec}R$.

*1. Choice of components.* By [det-pe-wlocal-components] the closed point sets of
$\operatorname{Spec}S$ and $\operatorname{Spec}R$ are profinite and homeomorphic to the
component spaces $\pi_0(\operatorname{Spec}S)$ and $\pi_0(\operatorname{Spec}R)$; the latter is
extremally disconnected because $R$ is w-contractible. The induced map
$\pi_0(\operatorname{Spec}S)\to\pi_0(\operatorname{Spec}R)$ is continuous and surjective: a
maximal ideal $\mathfrak m$ of $R$ is the image of a prime of $S$ by faithful flatness, whose
closed specialization lies over $\mathfrak m$. By [det-pe-stonean-projective]
(1 $\Rightarrow$ 3) it has a continuous section $\sigma$. Its image $T=\sigma(\pi_0(
\operatorname{Spec}R))$ is compact, hence closed, and maps bijectively onto
$\pi_0(\operatorname{Spec}R)$.

*1. Restriction to $T$.* Let $S_T=\varinjlim_e S_e$, the colimit over the idempotents $e$ of $S$
whose clopen subset contains the preimage of $T$ in $\operatorname{Spec}S$. Localizing at an
idempotent is a quotient, so $S\to S_T$ is surjective, $\operatorname{Spec}S_T$ is the
preimage of $T$ (an intersection of clopen subsets, as $T$ is closed in the profinite space
$\pi_0(\operatorname{Spec}S)$), and local rings do not change. Thus $R\to S_T$ identifies
local rings, $\operatorname{Spec}S_T$ is w-local (a closed union of components of a w-local
space), closed points of $\operatorname{Spec}S_T$ lie over closed points of
$\operatorname{Spec}R$, and $\pi_0(\operatorname{Spec}S_T)=T\to\pi_0(\operatorname{Spec}R)$ is
bijective.

*1. $R\to S_T$ is an isomorphism.* Each component of $\operatorname{Spec}S_T$ consists of the
generalizations of its closed point $t$, i.e. is the spectrum of $(S_T)_t\cong R_{\mathfrak m}$
with $\mathfrak m$ the image of $t$, and maps bijectively onto the component of $\mathfrak m$
([det-pe-wlocal-components]). As components correspond bijectively,
$\operatorname{Spec}S_T\to\operatorname{Spec}R$ is bijective, with isomorphisms on local
rings. It suffices that $R_{\mathfrak p}\to S_T\otimes_RR_{\mathfrak p}$ is an isomorphism for
every prime $\mathfrak p$ of $R$. Let $\mathfrak q$ be the unique prime of $S_T$ over
$\mathfrak p$. The primes of $S_T\otimes_RR_{\mathfrak p}$ are the primes $\mathfrak q'$ of
$S_T$ with $\mathfrak q'\cap R\subset\mathfrak p$; going down for the flat map $R\to S$
restricted to the union of components $\operatorname{Spec}S_T$ (which is stable under
generalization) gives a prime $\mathfrak q''\subset\mathfrak q$ of $S_T$ with
$\mathfrak q''\cap R=\mathfrak q'\cap R$, and by injectivity $\mathfrak q''=\mathfrak q'$. Hence
$S_T\otimes_RR_{\mathfrak p}$ is local with maximal ideal $\mathfrak q$, equals
$(S_T)_{\mathfrak q}$, and $R_{\mathfrak p}\to(S_T)_{\mathfrak q}$ is an isomorphism. The
composite $S\to S_T\xrightarrow{\ \sim\ }R$ is the required retraction.

*2.* By [det-pe-wc-rings-w-local-refinement], $S=B'$ satisfies the hypotheses of 1, so it has
an $R$-algebra retraction $B'\to R$; precomposing with $B\to B'$ gives the retraction of
$R\to B$.
