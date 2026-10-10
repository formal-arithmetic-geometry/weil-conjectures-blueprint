+++
kind  = "proof"
of    = "thm-weil-final-functional-equation"
+++
Use the determinant definitions in [def-weil-determinant-constants].
The reciprocity calculation [prop-duality-reciprocity], whose duality
input is [prop-poincare-pairing], gives

$$
P_{2d-i}(q^{-d}T^{-1})
=(-1)^{b_i}T^{-b_i}D_i^{-1}P_i(T),
\qquad D_iD_{2d-i}=q^{db_i}.
$$

Pairing $i$ with $2d-i$, and using the middle-degree alternating-form
case in [prop-duality-reciprocity], shows that $d\chi$ is even. Thus
the sign is defined by [def-weil-functional-equation-sign]. Finally,
substitution into the rational factorization of the
[def-weil-point-counts-zeta] zeta series and reindexing gives exactly
the functional-equation identity in [prop-functional-equation],
with $\chi$ and $b_i$ as in [def-weil-betti-numbers].
