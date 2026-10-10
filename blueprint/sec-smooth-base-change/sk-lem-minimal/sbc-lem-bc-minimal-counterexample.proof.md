+++
kind  = "proof"
of    = "sbc-lem-bc-minimal-counterexample"
+++
Consider the set $\mathfrak T$ of closed subschemes $T'\subset T$ such
that $P(T')$; ordered by inclusion ($T''\subset T'$ means the closed
immersion), a chain has a lower bound by (2) applied to the inverse
system of its members (their transition morphisms are closed
immersions, hence affine), so by Zorn's lemma $\mathfrak T$ has a
minimal element $T'$, and $T'\neq\emptyset$ by (4). If $T'$ is not reduced, then the reduction
$T'_{\mathrm{red}}\to T'$ is a thickening, and (1) gives
$P(T'_{\mathrm{red}})$, contradicting the minimality of $T'$ as
$T'_{\mathrm{red}}$ is a strictly smaller closed subscheme; hence $T'$
is reduced. Let $\eta\in T'$ be the generic point of an irreducible
component of $T'$; then $\eta=\operatorname{Spec}K$ for a field $K$
and $\eta=\varprojlim V$ over the affine open subschemes $V\subset T'$
containing $\eta$. For such a $V$, the complement $Z=T'\setminus V$ is
closed with quasi-compact complement $V$, and if $P(V)$ failed then by
(3) $P(Z)$ would hold, contradicting the minimality of $T'$ ($Z$ is
strictly smaller than $T'$ since $\eta\in V$); hence
$P(V)$ holds for all these $V$, and (2) applied to the limit gives
$P(\eta)=P(\operatorname{Spec}K)$.
