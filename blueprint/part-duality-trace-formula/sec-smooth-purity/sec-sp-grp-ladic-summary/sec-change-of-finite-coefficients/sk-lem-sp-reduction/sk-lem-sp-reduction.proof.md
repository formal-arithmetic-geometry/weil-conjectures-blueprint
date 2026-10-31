+++
kind = "proof"
of = "sk-lem-sp-reduction"
uses = ["sk-lem-sf-flat-model", "sk-prop-scalar-six", "sk-lem-sp-finite-existence", "sk-prop-geo-p1-adjunction", "sk-prop-cohsm"]
+++
The map $b$ is the change of coefficients for $Rf_!$ (Proposition [sk-prop-scalar-six]):
extension by zero commutes with $-\otimes^{\mathbf L}_AB$, and for $R\bar f_*$ we resolve
$B$ by finite free $A$-modules and use the flat models of Lemma [sk-lem-sf-flat-model].
The comparison holds on each free term, and since $R\bar f_*$ has finite cohomological
dimension only finitely many terms contribute in each degree, so it holds for every $B$.
We define $c_{A,B}(K)$ as the transpose of the right-hand side of (10.15).
Whether it is an isomorphism is a local question, so we may restrict to a chart
$f|_U=p_d\circ e$ of Proposition [sk-prop-cohsm](1). There the counit is built from
the trace of the projective line and sums over the fibres of $e$, which commute with
extension of coefficients (Proposition [sk-prop-geo-p1-adjunction]). Hence $c_{A,B}(K)$
is the transpose of $(e^*p_d^*K(d)[2d])_B\simeq e^*p_d^*(K_B)(d)[2d]$. Transitivity holds
because both sides have the same transpose.
