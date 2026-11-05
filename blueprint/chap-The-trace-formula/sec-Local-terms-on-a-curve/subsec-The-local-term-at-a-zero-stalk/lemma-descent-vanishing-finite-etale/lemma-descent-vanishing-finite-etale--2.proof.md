+++
kind = "proof"
of = "lemma-descent-vanishing-finite-etale--2"
order = 986004
+++
Multiplication by $n$ on every object of $D(A)$ is an isomorphism:
on each cohomology module its inverse is multiplication by the inverse
of $n$ in $A$, and cohomology detects isomorphisms. This is
`DerivedCategory.isIso_smul_id_of_isUnit`. Now

$$
(n\,\operatorname{id}_{M_2})\circ r
=t\circ p_2\circ r
=t\circ r'\circ p_1=0.
$$

Composing with the inverse of $n\,\operatorname{id}_{M_2}$ gives $r=0$.
