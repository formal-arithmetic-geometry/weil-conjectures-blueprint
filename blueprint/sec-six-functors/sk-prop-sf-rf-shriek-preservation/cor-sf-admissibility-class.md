+++
id = "cor-sf-admissibility-class"
kind = "theorem"
title = "The dualizing object and finite-coefficient dual preservation"
order = 2184
tags = ["latex:corollary"]
uses = ["cor-exc-base-change-open-immersion-general", "def-pod-conventions", "def-trf-admissibility", "def-weil-exceptional-adjoint-admissibility", "lem-weil-finite-duality-site-comparison", "lem-weil-verdier-preservation-strata", "thm-sf-preservation-class"]
+++
Let $X$ be separated of finite type over $\Fbar$, let
$A=A_{E,n}$, and let $D_{a_X}$ be the chart bound of
[thm-sf-preservation-class]. Then:

1. $\omega_{X,A}=Ra_X^!A$ belongs to $D^b_{ctf}(X,A)$, with
Tor amplitude in $[-2D_{a_X},1]$, uniformly in $n$. The geometric
duality construction also gives the bound $[-2\dim X,0]$.
1. For every $K\in D^b_{ctf}(X,A)$ of Tor amplitude $[a,b]$,
$D_XK=R\mathcal Hom(K,\omega_{X,A})$ has Tor amplitude in
$[-b-2\dim X,-a]$. No site-perfect hypothesis on $X$ is required
for this geometric bound.
1. Clauses (2) and (3) of exceptional-adjoint admissibility follow
from [thm-sf-preservation-class]. The additional composition,
exchange and exceptional coefficient comparisons in
[def-trf-admissibility], [def-pod-conventions] retain their stated
hypotheses except where a specific theorem supplies them, such as
[cor-exc-base-change-open-immersion-general].

## Proof

Apply [thm-sf-preservation-class] to $a_X$ and the constant input
of Tor amplitude zero; this gives the chart bound in (1) and the
exceptional-preservation assertion in (3). For (2), use the geometric
stratification bound of [lem-weil-verdier-preservation-strata] on the
small étale site and transport duality by
[lem-weil-finite-duality-site-comparison]. Applied to $K=A_X$,
this also gives the bound $[-2\dim X,0]$ in (1).
The remaining qualifications are those of
[def-weil-exceptional-adjoint-admissibility] and
[def-trf-admissibility], [def-pod-conventions]; the indicated open-base
exchange is [cor-exc-base-change-open-immersion-general].
