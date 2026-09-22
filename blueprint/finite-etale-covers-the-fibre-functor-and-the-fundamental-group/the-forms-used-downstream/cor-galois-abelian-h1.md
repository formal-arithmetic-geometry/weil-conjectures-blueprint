+++
id = "cor-galois-abelian-h1"
kind = "theorem"
title = "Abelian case: torsors, characters and H^1"
order = 3035
lean = ["AlgebraicGeometry.Etale.h1EquivContinuousHom"]
tags = ["latex:corollary"]
uses = ["thm-galois-fundamental", "thm-galois-torsor-h1", "def-galois-fibre-functor", "lem-galois-axioms", "lem-galois-action-continuous"]
+++
Let $Y$ be connected with geometric point $\bar y$ and let $M$ be a finite
abelian group. Then there is a canonical bijection
$$
 H^1(Y_{\Et},\underline M)\xrightarrow{\ \sim\ }
 \operatorname{Hom}_{\mathrm{cont}}\bigl(\pi_1(Y,\bar y),M\bigr),
$$
given on torsors by choosing $p\in P_{\bar y}$ — a simply transitive
$M$-set — and sending $P$ to the continuous homomorphism $f_P$ with
$$
 g\cdot p=p+f_P(g)\qquad(g\in\pi_1(Y,\bar y));
$$
the class of $P$ is independent of the choice of $p$ because $M$ is
abelian. (This is the identification used, without citation, in the proof
of the additive-character lemma of the monodromy chapter.)

## Proof

By [thm-galois-fundamental] an $M$-torsor $P$ is a finite $\pi_1$-set with
a simply transitive $M$-action commuting with the $\pi_1$-action; choosing
$p\in P_{\bar y}$, simple transitivity gives a unique $f_P(g)\in M$ with
$g\cdot p=p+f_P(g)$. The two actions commute, so
$f_P(gh)=f_P(g)+f_P(h)$, and $f_P$ is continuous: by
[lem-galois-action-continuous] the action map is continuous, so for
$m\in M$ the set of $g$ with $f_P(g)=m$, which is the preimage of the point
$p+m$ of the finite discrete $\pi_1(Y,\bar y)$-set $P_{\bar y}$ under the
continuous map $g\mapsto g\cdot p$, is open.

Conversely a continuous homomorphism $f$ makes $M$ into a finite continuous
$\pi_1$-set by $g\cdot a=f(g)+a$, commuting with translations, hence
corresponds to an $M$-torsor. The constructions are inverse, and replacing
$p$ by $p+a$ does not change $f_P$ since $M$ is abelian. The identification
with $H^1$ is [thm-galois-torsor-h1].

Unresolved dependencies: def:weil-pbc-finite-torsors
