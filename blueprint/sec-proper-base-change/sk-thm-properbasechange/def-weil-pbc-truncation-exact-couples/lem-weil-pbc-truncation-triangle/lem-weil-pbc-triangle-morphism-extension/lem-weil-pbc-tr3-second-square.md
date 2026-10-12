+++
id = "lem-weil-pbc-tr3-second-square"
kind = "lemma"
title = "TR3 from the second square: a commutative square on the second arrows extends to a morphism of distinguished triangles"
uses = ["def-weil-triangulated-category"]
refines = "proof/lem-weil-pbc-triangle-morphism-extension"
lean = ["CategoryTheory.Pretriangulated.complete_distinguished_triangle_morphism₁"]
tags = ["sheaf-dag", "mathlib", "stacks-0145"]
+++
Let $\mathcal T$ be a pre-triangulated category [def-weil-triangulated-category], $X\xrightarrow{u}Y\xrightarrow{v}Z\xrightarrow{d}X[1 ]$ and $X'\xrightarrow{u'}Y'\xrightarrow{v'}Z'\xrightarrow{d'}X'[1 ]$ distinguished triangles, and $b:Y\to Y'$, $c:Z\to Z'$ morphisms with $c\circ v=v'\circ b$. Then there is $a:X\to X'$ with $b\circ u=u'\circ a$ and $a[1 ]\circ d=d'\circ c$, i.e. $(a,b,c)$ is a morphism of triangles.
