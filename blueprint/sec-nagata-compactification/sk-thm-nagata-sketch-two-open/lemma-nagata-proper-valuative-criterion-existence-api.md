+++
id = "lemma-nagata-proper-valuative-criterion-existence-api"
kind = "lemma"
title = "Existence part of the proper valuative criterion"
order = 295
lean = ["AlgebraicGeometry.UniversallyClosed.eq_valuativeCriterion"]
uses = ["lemma-nagata-local-domain-valuation-dominates", "lemma-nagata-valuation-intersection"]
+++
A morphism $f\colon Y\to S$ is universally closed if and only if it is
quasi-compact and, for every valuation ring $A$ with fraction field $K$,
every $S$-morphism $\operatorname{Spec}(K)\to Y$ lying over a morphism
$\operatorname{Spec}(A)\to S$ extends to an $S$-morphism
$\operatorname{Spec}(A)\to Y$.

## Proof

**Universally closed implies the two conditions.** A universally closed
morphism is quasi-compact. For the lifts, let
$\operatorname{Spec}(K)\to Y$ lie over $\operatorname{Spec}(A)\to S$ and
put $Y_A=Y\times_S\operatorname{Spec}(A)$. The given maps induce a
morphism $\operatorname{Spec}(K)\to Y_A$ over
$\operatorname{Spec}(A)$; let $\xi\in Y_A$ be the image of its point and
$G=\overline{\{\xi\}}$ with the reduced induced structure. Then $G$ is
integral with generic point $\xi$, and $\kappa(\xi)\subseteq K$. Since
$f$ is universally closed, $Y_A\to\operatorname{Spec}(A)$ is closed, so
the image of $G$ is a closed subset containing the generic point of
$\operatorname{Spec}(A)$, i.e. all of $\operatorname{Spec}(A)$. Choose
$x\in G$ over the closed point. The local ring $B=\mathcal O_{G,x}$ is a
local domain with fraction field $\kappa(\xi)\subseteq K$, and
$A\to B$ is a local homomorphism. By
[lemma-nagata-local-domain-valuation-dominates], choose a valuation
ring $C$ of $K$ dominating $B$. Then $A\subseteq C\subseteq K$ and $C$
dominates $A$, so the intersection identity
[lemma-nagata-valuation-intersection] (with $L=K$) gives
$C=K\cap C=A$. The composite
$\operatorname{Spec}(A)=\operatorname{Spec}(C)\to\operatorname{Spec}(B)
\to G\to Y_A\to Y$ restricts on $\operatorname{Spec}(K)$ to the given
map, and its composite to $\operatorname{Spec}(A)$ is the identity, so it
is an $S$-morphism extending the generic map.

**The two conditions imply universally closed.** Both conditions are
stable under base change: quasi-compactness is, and if $f'\colon
Y'=Y\times_SS'\to S'$ is a base change, a square for $f'$ composes to a
square for $f$, whose lift, paired with the given
$\operatorname{Spec}(A)\to S'$, is a lift for $f'$. It therefore suffices
to show that a quasi-compact $f$ with the lifting property is closed. Let
$Z\subseteq Y$ be closed. Since $f$ is quasi-compact, $f(Z)$ is closed as
soon as it is stable under specialization, because the closure of
the image of a quasi-compact morphism consists of the specializations of
image points. Let
$s'=f(y')$ with $y'\in Z$ and let $s'\rightsquigarrow s$. Let $T$ be the
closure of $s'$ with its reduced structure; $\mathcal O_{T,s}$ is a local
domain with fraction field $\kappa(s')\subseteq\kappa(y')=:K$. By
[lemma-nagata-local-domain-valuation-dominates] there is a valuation ring
$A$ of $K$ dominating $\mathcal O_{T,s}$. The point $y'$ gives
$\operatorname{Spec}(K)\to Y$ over
$\operatorname{Spec}(A)\to T\to S$, and a lift
$h\colon\operatorname{Spec}(A)\to Y$ sends the generic point to $y'$, so
the closed point to a specialization of $y'$, which lies in $Z$, and it
lies over $s$. Hence $s\in f(Z)$.
