+++
id = "lem-weil-pbc-five-lemma"
kind = "lemma"
title = "Five lemma in an abelian category"
uses = ["def-sp-abelian"]
lean = ["CategoryTheory.Abelian.isIso_of_epi_of_isIso_of_isIso_of_mono"]
order = 2115
tags = ["mathlib", "stacks-05QB"]
+++
Let $\mathcal A$ be an abelian category [def-sp-abelian] and consider a commutative diagram in $\mathcal A$

$$
\begin{array}{ccccccccc}
A_1&\to&A_2&\to&A_3&\to&A_4&\to&A_5\\
\downarrow{\scriptstyle\alpha_1}&&\downarrow{\scriptstyle\alpha_2}&&\downarrow{\scriptstyle\alpha_3}&&\downarrow{\scriptstyle\alpha_4}&&\downarrow{\scriptstyle\alpha_5}\\
B_1&\to&B_2&\to&B_3&\to&B_4&\to&B_5
\end{array}
$$

whose rows are exact at $A_2,A_3,A_4$ and at $B_2,B_3,B_4$. If $\alpha_1$ is an epimorphism, $\alpha_2$ and $\alpha_4$ are isomorphisms and $\alpha_5$ is a monomorphism, then $\alpha_3$ is an isomorphism. In particular $\alpha_3$ is an isomorphism when $\alpha_1,\alpha_2,\alpha_4,\alpha_5$ are.
