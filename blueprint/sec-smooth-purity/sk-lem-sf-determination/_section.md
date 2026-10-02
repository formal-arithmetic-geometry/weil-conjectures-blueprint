+++
id = "sk-lem-sf-determination"
kind = "section"
title = "Determination on a generating class"
order = 1862
uses = ["sk-def-sf-operations"]
lean = ["CategoryTheory.Pretriangulated.isIso₃_of_isIso₁₂"]
+++
*Lemma (sketch).*

Let $\Phi,\Psi$ be exact functors of triangulated categories and let
$\alpha:\Phi\to\Psi$ be natural. If $\alpha$ is an isomorphism on two terms of
a distinguished triangle, it is an isomorphism on the third; hence a natural
transformation that is an isomorphism on a generating class, natural in the
same variables, is determined by its values there.

## Proof

Apply $H^q$ to the map of triangles: two columns of the ladder are
isomorphisms, so the third is, by the five lemma; a morphism whose cone has
vanishing cohomology is zero. For the second clause, two such transformations
differ by one vanishing on generators, and the first clause descends from
generators to shifts, cones and summands.

Uses: `\Cref{sk-def-sf-operations}`
