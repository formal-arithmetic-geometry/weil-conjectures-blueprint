+++
id = "def-weil-pbc-ringed-space-algebra-module"
kind = "definition"
title = "Underlying-module functor of commutative algebra sheaves on a ringed space"
lean = ["CategoryTheory.commAlgebraSheafModuleFunctor", "CategoryTheory.commAlgebraSheafModule"]
order = 1638
+++
Let $X$ be a topological space, and let $\mathcal O$ be a sheaf of commutative rings on $X$. Sheaves of commutative $\mathcal O$-algebras form the under category of $\mathcal O$ in commutative ring sheaves: an object is a ring sheaf $\mathcal A$ with a ring-sheaf map $\sigma:\mathcal O\to\mathcal A$, and a morphism is a ring-sheaf map commuting with the structure maps. The underlying-module functor to sheaves of $\mathcal O$-modules sends $(\mathcal A,\sigma)$ to the unit module over $\mathcal A$, restricted along $\sigma$, so $r\cdot a=\sigma(r)a$ on each open; it sends a morphism to its same additive section maps, now $\mathcal O$-linear.
