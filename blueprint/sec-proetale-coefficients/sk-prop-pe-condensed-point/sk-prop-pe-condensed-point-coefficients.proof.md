+++
kind = "proof"
of = "det-pe-condensed-point-coefficients"
+++
*Sheaf property.* A pro-étale covering ([def-weil-pbc-proetale-site]) is in
particular an fpqc covering, and for an fpqc covering $\{U_a\to U\}$ the map
$\coprod_a|U_a|\to|U|$ is a quotient map on underlying spaces (after refining to a
quasi-compact covering of each affine open). Hence a family of continuous functions
on the $U_a$ which agree on the overlaps descends uniquely to a continuous function
on $U$, which is the sheaf condition for $\underline M_X$.

*Discrete coefficients.* The canonical map from the constant sheaf sends $m$ to the
constant function with value $m$. If $M$ is discrete, a continuous function
$f\colon|U|\to M$ is locally constant: its fibres form a covering of $U$ by
disjoint open and closed subschemes, which is a pro-étale covering, and on each
member $f$ is constant. So the map is locally surjective. It is locally injective,
since a section of the constant sheaf vanishing as a function vanishes on a
covering. Hence it is an isomorphism of sheaves.

*Étale origin.* The constant pro-étale sheaf is the sheafified constant presheaf,
and $\nu_X^*$ ([def-weil-pbc-site-comparison-morphism]) sends the sheafified constant
étale presheaf to the sheafified constant pro-étale presheaf, both being left
adjoint to global sections on the terminal object. Combining,
$\nu_X^*M_{X,\Et}\cong\underline M_X$ for discrete $M$.
