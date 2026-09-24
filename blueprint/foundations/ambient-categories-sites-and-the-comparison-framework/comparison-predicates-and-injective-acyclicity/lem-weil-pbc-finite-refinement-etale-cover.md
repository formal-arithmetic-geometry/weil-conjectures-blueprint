+++
id = "lem-weil-pbc-finite-refinement-etale-cover"
kind = "lemma"
title = "Finite refinement of a surjective etale morphism"
order = 1229
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions"]
+++
Let $u:U\to T$ be a surjective etale morphism
[def-weil-pbc-scheme-conventions] and assume that $T$ is quasi-compact and
quasi-separated. There exist a finite set $J$, a finite, finitely presented,
surjective morphism

$$
 r:T'\longrightarrow T,
$$

a finite open covering $T'=\bigcup_{a\in J}W_a$, and $T$-morphisms
$\phi_a:W_a\to U$ such that

$$
 u\circ\phi_a=r|_{W_a}:W_a\longrightarrow T
 \qquad(a\in J).
$$

Equivalently, $r$ factors through $u$ Zariski locally on $T'$.

## Proof

This is the input of the finite refinement of surjective etale morphisms: for
a surjective etale morphism $u:U\to T$ with $T$ quasi-compact and
quasi-separated, there are a finite, finitely presented, surjective morphism
$r:T'\to T$, a finite open covering $T'=\bigcup_{a\in J}W_a$, and
$T$-morphisms $\phi_a:W_a\to U$ with $u\circ\phi_a=r|_{W_a}$ for every $a\in
J$, i.e. $r$ factors through $u$ Zariski locally on $T'$ (Stacks Project,
Lemma 37.45.7, Tag [09Z0](https://stacks.math.columbia.edu/tag/09Z0)). The
blueprint records this single assertion in the displayed form and proves
separately all of its consequences (the degree-zero comparisons over
henselian pairs); the proof, which refines the affine Zariski covering of $T$
and uses the local structure of etale morphisms, is not decomposed here.
