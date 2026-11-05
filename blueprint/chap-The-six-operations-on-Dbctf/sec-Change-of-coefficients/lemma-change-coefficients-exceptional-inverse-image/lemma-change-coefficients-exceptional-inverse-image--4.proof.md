+++
kind = "proof"
of = "lemma-change-coefficients-exceptional-inverse-image--4"
order = 640009
uses = ["lemma-change-coefficients-direct-image", "definition-sp-scalar-extension"]
+++
Choose an $E$-basis $b_1,\ldots,b_d$ of $F$. After restriction of scalars,
the maps from $K$ to $T_ZK$ given by the unit and multiplication by the
$b_i$ identify $\operatorname{Res}_Z T_ZK$ with the direct sum of $d$
copies of $K$. The same basis works on $X$ and $Y$; this is
`exists_isIso_biproductDesc_unit_smul`.

Restriction of scalars commutes with $Rf_*$, and the pushforward over $F$
commutes with multiplication by each $b_i$. Consequently these direct-sum
identifications are compatible with the pushforward comparison and the
scalar-extension adjunctions. The right adjoint of $Rf_{*,E}$ is additive,
so it preserves these finite direct sums. Applying
`CategoryTheory.Adjunction.isIso_mateEquiv_inv_of_isIso_biproductDesc_unit`
shows that the transpose of the inverse pushforward comparison is an
isomorphism.
