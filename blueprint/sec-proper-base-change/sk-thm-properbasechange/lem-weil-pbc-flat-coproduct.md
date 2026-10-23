+++
id = "lem-weil-pbc-flat-coproduct"
kind = "lemma"
title = "A coproduct of flat objects of a Grothendieck abelian braided closed monoidal category is flat"
lean = ["CategoryTheory.ObjectProperty.flat_coproduct", "CategoryTheory.ObjectProperty.flat_iff_preservesFiniteLimits"]
order = 2013
tags = ["stacks-03EU"]
+++
Let $\mathcal B$ be a Grothendieck abelian category with a braided monoidal closed structure $\otimes$, and call an object $P$ of $\mathcal B$ flat if the functor $P\otimes-:\mathcal B\to\mathcal B$ preserves finite limits. If $(P_i)_{i\in I}$ is a family of flat objects indexed by a set $I$ (of the size of the Hom-sets of $\mathcal B$), then $\coprod_{i\in I}P_i$ is flat.
