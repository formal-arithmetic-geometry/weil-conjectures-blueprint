+++
kind = "proof"
of = "proposition-jacobian-over-ground-field--4"
order = 1562010
uses = ["proposition-jacobian-over-ground-field--1", "lemma-rigidification-along-section", "corollary-degree-jacobian"]
+++
Send a degree-zero invertible sheaf on $C$ to its class in
$F(\operatorname{Spec}\bar k)$. Its fibrewise degree is zero by
invariance of degree under field extension.

This map is injective: equality of Picard-sheaf classes identifies the
invertible sheaves up to tensoring with a sheaf pulled back from the
base, as in [lemma-rigidification-along-section], and
$\operatorname{Pic}(\bar k)=0$. For surjectivity, a section is represented
by an invertible sheaf on an fppf cover of $\operatorname{Spec}\bar k$.
A nonempty member of that cover has a $\bar k$-point, so pulling back
along this point produces a representative on $C$. Its degree is zero
because the original section lies in $F$.

This is the bijection of
`AlgebraicGeometry.exists_picardZero_equiv_picardFunctorDegree`.
Compose it with the inverse of the representing bijection $r$.
Since pullback respects tensor products and $r$ respects the group
laws, `AlgebraicGeometry.exists_mulEquiv_of_isPicardZeroMul` makes the
composite a group isomorphism.
