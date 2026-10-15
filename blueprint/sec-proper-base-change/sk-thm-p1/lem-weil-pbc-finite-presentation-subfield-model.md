+++
id = "lem-weil-pbc-finite-presentation-subfield-model"
kind = "lemma"
title = "A finitely presented algebra has a model over one subfield"
lean = ["Algebra.exists_subfield_model"]
+++
Let $k$ be a field, let $(K_i)_{i\in I}$ be a nonempty directed family of subfields of $k$ whose union is $k$, and let $E$ be a finitely presented commutative $k$-algebra `Algebra.FinitePresentation` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/FinitePresentation.lean)). Then for some $i\in I$ there is a commutative $K_i$-algebra $B$ and a $k$-algebra isomorphism $k\otimes_{K_i}B\cong E$. If $k:\mathrm{Type}\ u$ and $E:\mathrm{Type}\ w$, the carrier of $B$ can be chosen in $\mathrm{Type}(\max(u,w))$.
