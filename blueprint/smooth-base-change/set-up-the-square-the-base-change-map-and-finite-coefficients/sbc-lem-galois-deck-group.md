+++
id = "sbc-lem-galois-deck-group"
kind = "lemma"
title = "The deck group of a connected Galois cover"
order = 5108
lean = ["AlgebraicGeometry.IsGaloisCover.aut_eq_of_isConnected"]
uses = ["def-sbc-normal-dominant-galois"]
+++
Let $\pi:Z\to C$ be a Galois cover with group $G$ in the sense of
[def-sbc-normal-dominant-galois], and assume that $Z$ is connected. Then the
deck group of $\pi$ is $G$.

## Proof

By [def-sbc-normal-dominant-galois] every element of $G$ is an automorphism
of $Z$ over $C$, so $G\subseteq\operatorname{Aut}_C(Z)$.

Conversely, since $Z\to C$ is a $G$-torsor, the action identifies
$G\times_CZ$ with $Z\times_CZ$ by $(g,z)\mapsto(g\cdot z,z)$; the graph of an
automorphism $\sigma\in\operatorname{Aut}_C(Z)$, read through the inverse of
this identification, is a morphism $Z\to G\times_CZ$ over $Z$, and its
projection to $G$ is a morphism $Z\to G$. As $G$ is a finite disjoint union
of copies of $C$ and $Z$ is connected, this morphism is constant, with value
some $g\in G$; then $\sigma(z)=g\cdot z$ for all $z\in Z$, so $\sigma=g\in G$
and $\operatorname{Aut}_C(Z)=G$.
