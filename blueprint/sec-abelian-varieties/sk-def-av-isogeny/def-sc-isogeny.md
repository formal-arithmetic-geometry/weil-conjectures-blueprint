+++
id = "def-sc-isogeny"
kind = "definition"
title = "Isogenies"
lean = ["AlgebraicGeometry.IsIsogeny", "AlgebraicGeometry.isogenyDegree"]
order = 441
uses = ["def-sc-abelian-variety", "def-sc-group-scheme"]
+++
Let $A,B$ be group schemes
over $k$. An *isogeny* $f:A\to B$ is a homomorphism of group
schemes which is surjective and whose kernel is finite over $k$; the
*degree* of an isogeny is the order of its kernel.

When $A$ and $B$ are abelian varieties ([def-sc-abelian-variety]), an
isogeny $f:A\to B$ is finite and flat, and the degree of the finite flat
morphism $f$ equals the order of its kernel.
