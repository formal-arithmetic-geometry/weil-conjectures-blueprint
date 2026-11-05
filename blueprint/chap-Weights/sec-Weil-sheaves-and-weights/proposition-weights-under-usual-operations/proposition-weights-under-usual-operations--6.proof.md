+++
kind = "proof"
of = "proposition-weights-under-usual-operations--6"
order = 1073013
+++
Let $(G_i)$ be a mixed filtration of the mixed lisse sheaf $G$. If the graded pieces $G_i/G_{i-1}$ are lisse, dualizing is exact on lisse sheaves, so the annihilator filtration $G_i^\perp=\ker(G^\vee\to G_i^\vee)$ has graded pieces $(G_i/G_{i-1})^\vee$. Clause [proposition-weights-under-usual-operations--4] makes them pure of the negated weights. This proves the second assertion, and the first one in this case.

In general the graded pieces need not be lisse, and we argue by Noetherian induction on $X$. Let $j:U\to X$ be a dense open, stable under Frobenius, on which all graded pieces are lisse, and let $i:Z\to X$ be its closed complement. On $U$ the first case applies to $j^*G$. Since $G$ is lisse, $i^*(G^\vee)\simeq(i^*G)^\vee$ with $i^*G$ mixed lisse on $Z$, so $i^*(G^\vee)$ is mixed of the negated weights by induction. Extension by zero and direct image along a closed immersion do not change stalks, so they carry mixed filtrations to mixed filtrations of the same weights. Clause [proposition-weights-under-usual-operations--1], applied to $0\to j_!j^*(G^\vee)\to G^\vee\to i_*i^*(G^\vee)\to0$, shows that $G^\vee$ is mixed of the negated weights.

*Source:* the proof of Proposition [proposition-weights-under-usual-operations].
