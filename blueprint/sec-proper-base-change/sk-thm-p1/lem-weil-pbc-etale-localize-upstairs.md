+++
id = "lem-weil-pbc-etale-localize-upstairs"
kind = "lemma"
title = "Etale near a closed subset gives an etale principal localization"
lean = ["AlgebraicGeometry.exists_etale_localization_of_prime_mem"]
source = "literature/stacks-project/more-algebra.tex, More on Algebra, Lemma Tag 07M0 (lemma-localize-upstairs, line 1821) and its proof (the non-etale locus is closed, V(J') with V(J') ∩ V(J) empty, Algebra Lemma 00E0 lemma-Zariski-topology, 1 = f + g with f in J, g in J')"
+++
Let $A\to B$ be a homomorphism of commutative rings and $\mathfrak b\subseteq B$ an ideal. Assume that for every prime ideal $\mathfrak q\subset B$ with $\mathfrak b\subseteq\mathfrak q$ there is $h\in B\setminus\mathfrak q$ such that $\operatorname{Spec}B_h\to\operatorname{Spec}A$ is etale `AlgebraicGeometry.Etale` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Etale.lean)). Then there is $g\in B$ whose image in $B/\mathfrak b$ is a unit such that $\operatorname{Spec}B_g\to\operatorname{Spec}A$ is etale.
