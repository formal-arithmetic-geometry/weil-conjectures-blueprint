+++
id = "sbc-lem-slicing"
kind = "lemma"
title = "Slicing a smooth morphism"
order = 5136
lean = ["AlgebraicGeometry.IsSmooth.exists_etale_cover_slicing"]
uses = ["def-sbc-smooth-morphisms", "def-sbc-normal-dominant-galois"]
+++
Let $f:X\to S$ be a smooth [def-sbc-smooth-morphisms] morphism of schemes.
Then there exists an étale covering $\{U_i\to X\}_{i\in I}$ such that
$U_i\to S$ factors as $U_i\to V_i\to S$ where $V_i\to S$ is étale and
$U_i\to V_i$ is a smooth morphism of affine schemes, which has a section,
and has geometrically connected [def-sbc-normal-dominant-galois] fibres.

(*Stacks Project, More on Morphisms, [Tag
0EY4](https://stacks.math.columbia.edu/tag/0EY4) = Lemma 37.38.8.*)

## Proof

This is the recorded classical input named in the statement, Stacks Project,
More on Morphisms, Lemma 37.38.8 ([Tag
0EY4](https://stacks.math.columbia.edu/tag/0EY4)): a smooth morphism
becomes, after an étale cover of its source, a smooth morphism of affine
schemes with a section and geometrically connected fibres over an étale
base. No separate proof is given.
