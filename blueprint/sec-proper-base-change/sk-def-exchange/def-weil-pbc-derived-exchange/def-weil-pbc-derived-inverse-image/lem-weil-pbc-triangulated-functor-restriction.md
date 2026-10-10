+++
id = "lem-weil-pbc-triangulated-functor-restriction"
kind = "lemma"
title = "Restriction of a triangulated functor to full triangulated subcategories"
uses = ["def-weil-triangulated-category"]
refines = "sk-def-exchange"
lean = ["CategoryTheory.ObjectProperty.isTriangulated_lift"]
tags = ["sheaf-dag", "mathlib", "stacks-05QM"]
+++
Let $\mathcal T,\mathcal T'$ be triangulated categories and $(F,\sigma):\mathcal T\to\mathcal T'$ a triangulated functor, $\sigma_X:F(X[1 ])\xrightarrow{\sim}F(X)[1 ]$ its shift isomorphism [def-weil-triangulated-category]. Let $\mathcal S\subset\mathcal T$ and $\mathcal S'\subset\mathcal T'$ be full triangulated subcategories (strictly full, containing $0$, stable under $[1 ]$ and $[-1 ]$, and containing the third vertex of every distinguished triangle whose two other vertices they contain), each with the triangulated structure in which a triangle is distinguished iff it is distinguished in the ambient category, so that the inclusions $\iota:\mathcal S\to\mathcal T$, $\iota':\mathcal S'\to\mathcal T'$ are triangulated functors with identity shift isomorphisms. Suppose $F(X)\in\mathcal S'$ for every $X\in\mathcal S$. Then the restriction $F|:\mathcal S\to\mathcal S'$, $X\mapsto F(X)$, $f\mapsto F(f)$, with the shift isomorphisms $\sigma_X$ ($X\in\mathcal S$), is a triangulated functor, and $\iota'\circ F|=F\circ\iota$ as functors with shift isomorphisms.
