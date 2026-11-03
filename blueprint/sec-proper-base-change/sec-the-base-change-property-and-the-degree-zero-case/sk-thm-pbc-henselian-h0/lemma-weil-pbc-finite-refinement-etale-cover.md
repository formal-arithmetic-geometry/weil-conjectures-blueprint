+++
id = "lemma-weil-pbc-finite-refinement-etale-cover"
kind = "lemma"
title = "Finite refinement of a surjective etale morphism"
lean = ["AlgebraicGeometry.Scheme.exists_finite_surjective_refinement_of_etale"]
order = 1646
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
