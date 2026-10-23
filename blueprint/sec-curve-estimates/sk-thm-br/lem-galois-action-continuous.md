+++
id = "lem-galois-action-continuous"
kind = "lemma"
title = "Continuity of the action of $\\operatorname{Aut}(F)$"
order = 1402
lean = ["CategoryTheory.PreGaloisCategory.continuousSMul_aut_fiber"]
uses = ["def-galois-category"]
+++
Let $\mathcal C$ be a category and $F:\mathcal C\to\mathbf{Sets}$ a
functor with all $F(X)$ finite, and let
$\operatorname{Aut}(F)\subseteq\prod_X\operatorname{Aut}(F(X))$ carry
the topology induced from the product of the discrete topologies, as in
[def-galois-category]. Then for every object $X$ the action map

$$
\operatorname{Aut}(F)\times F(X)\longrightarrow F(X),\qquad
(\gamma,x)\longmapsto\gamma_X(x),
$$

is continuous for the discrete topology on $F(X)$.
