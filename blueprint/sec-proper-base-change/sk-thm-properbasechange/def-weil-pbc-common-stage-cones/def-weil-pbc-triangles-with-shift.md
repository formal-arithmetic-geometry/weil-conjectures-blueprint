+++
id = "def-weil-pbc-triangles-with-shift"
kind = "definition"
title = "Triangles, morphisms and isomorphisms of triangles in a category with shift"
refines = "def-weil-pbc-common-stage-cones"
lean = ["CategoryTheory.Pretriangulated.Triangle"]
tags = ["sheaf-dag", "mathlib", "stacks-0144"]
+++
Let $\mathcal D$ be an additive category and $[1 ]:\mathcal D\to\mathcal D$, $X\mapsto X[1 ]$, an additive functor which is an auto-equivalence. A *triangle* in $\mathcal D$ is a sextuple $(X,Y,Z,f,g,h)$ of objects $X,Y,Z$ and morphisms $f:X\to Y$, $g:Y\to Z$, $h:Z\to X[1 ]$. A *morphism of triangles* $(X,Y,Z,f,g,h)\to(X',Y',Z',f',g',h')$ is a triple of morphisms $a:X\to X'$, $b:Y\to Y'$, $c:Z\to Z'$ with $b\circ f=f'\circ a$, $c\circ g=g'\circ b$ and $a[1 ]\circ h=h'\circ c$. Triangles and their morphisms, composed componentwise, form a category; an *isomorphism of triangles* is an isomorphism in this category, equivalently a morphism of triangles $(a,b,c)$ whose three components are isomorphisms of $\mathcal D$. Two triangles are *isomorphic* when there is an isomorphism of triangles between them.
