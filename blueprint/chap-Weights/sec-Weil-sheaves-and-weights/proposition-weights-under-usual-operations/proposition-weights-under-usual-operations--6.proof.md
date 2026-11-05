+++
kind = "proof"
of = "proposition-weights-under-usual-operations--6"
order = 1073013
+++
Let $G$ be a mixed lisse sheaf with mixed filtration $(G_i)$. Suppose first
that the graded pieces $G_i/G_{i-1}$ are lisse. Dualizing is exact on lisse
sheaves, so the annihilator filtration $G_i^\perp=\ker(G^\vee\to G_i^\vee)$
has graded pieces $(G_i/G_{i-1})^\vee$, which are pure of the negated
weights by clause [proposition-weights-under-usual-operations--4]. This proves the second assertion, and
the first in this case.

In general the graded pieces need not be lisse: on a curve, a pure lisse
$G$ has the filtration $j_!j^*G\subseteq G$, whose quotient $i_*i^*G$ is a
skyscraper with dual zero. We then argue by Noetherian induction on $X$. Let
$U\subseteq X$ be a dense open, stable under Frobenius, on which all graded
pieces are lisse, and let $i:Z\to X$ be its closed complement. On $U$ the
first case applies to $j^*G$. Since $G$ is lisse,
$i^*(G^\vee)\simeq(i^*G)^\vee$, and $i^*G$ is a mixed lisse sheaf on $Z$, so
$i^*(G^\vee)$ is mixed by induction, of the negated weights. Extension by
zero and direct image along a closed immersion are exact and do not change
stalks, so they carry mixed filtrations to mixed filtrations of the same
weights, and the exact sequence

$$
0\to j_!j^*(G^\vee)\to G^\vee\to i_*i^*(G^\vee)\to 0
$$

shows that $G^\vee$ is mixed, of the negated weights.

*Source:* the proof of Proposition [proposition-weights-under-usual-operations].
