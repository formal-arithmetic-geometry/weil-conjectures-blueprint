+++
id = "lemma-nagata-rees-degree-zero"
kind = "lemma"
title = "The degree-zero piece"
order = 193
lean = ["AlgebraicGeometry.reesGradingZero"]
uses = ["def-nagata-rees-piece", "lemma-nagata-rees-piece-membership"]
+++
Taking the constant coefficient gives a ring equivalence

$$
\mathcal R_A(I)_0\cong A.
$$

## Proof

Since $I^0=A$, a degree-zero Rees element is exactly a constant polynomial.
The inverse sends $a$ to the constant monomial $at^0$. The two composites
are identities by coefficient extensionality.
