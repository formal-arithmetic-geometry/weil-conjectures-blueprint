+++
id = "def-sp-kinjective-bridge"
kind = "definition"
title = "The K-injective bridge"
order = 1730
lean = ["CategoryTheory.IsKInjective", "CategoryTheory.KInjectiveResolution"]
uses = ["def-sp-grothendieck-abelian"]
+++
A *K-injective resolution* of a complex $K$ is a quasi-isomorphism $K\to I$
with $I$ K-injective: for every acyclic complex $A$ the complex
$\operatorname{Hom}(A,I)$ is acyclic. In a Grothendieck abelian category
[def-sp-grothendieck-abelian] every bounded-below complex admits a
K-injective resolution.
