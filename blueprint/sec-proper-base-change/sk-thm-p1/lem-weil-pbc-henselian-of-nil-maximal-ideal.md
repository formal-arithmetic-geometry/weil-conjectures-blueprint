+++
id = "lem-weil-pbc-henselian-of-nil-maximal-ideal"
kind = "lemma"
title = "A local ring with nil maximal ideal is henselian"
uses = ["def-weil-pbc-henselian-terminology"]
lean = ["henselianLocalRing_of_maximalIdeal_le_nilradical"]
source = "Mathlib/Dynamics/Newton.lean; literature/stacks-project/algebra.tex, Polynomial.existsUnique_nilpotent_sub_and_aeval_eq_zero, lines 100-127; Tag 06RS"
+++
Let $R$ be a commutative local ring with maximal ideal $\mathfrak m$. If every element of $\mathfrak m$ is nilpotent, then $R$ is a henselian local ring [def-weil-pbc-henselian-terminology].
