+++
kind = "proof"
of = "sk-lem-sp-reduction"
uses = ["sk-lem-sf-flat-model", "sk-def-sfb-coefficient-comparisons", "sk-lem-sp-finite-existence", "sk-prop-geo-p1-adjunction"]
+++
For $b$, use one compactification $f=\bar f\circ j$ for both rings. Extension
by zero commutes with $-\otimes^{\mathbf L}_AB$. For $R\bar f_*$, take a
bounded-above resolution of $B$ whose terms are finite free $A$-modules; it
may be infinite to the left. Represent $M$ by the bounded flat constructible
model of [sk-lem-sf-flat-model]. The comparison is an isomorphism on each
free term, and the cohomological bound $\operatorname{cd}_\ell(\bar f)$ gives a
finite window in every total degree. As in the scalar projection argument of
[sk-def-sfb-coefficient-comparisons], this applies to every $B$, whatever its
projective dimension over $A$. Associativity gives compatibility with a second
map $B\to C$.

Define $c_{A,B}(K)$ as the transpose of the right side of the counit identity.
Whether it is an isomorphism is local, so we may check it on the coordinate
charts $f|_U=p_d\circ e$ of [sk-lem-sp-finite-existence]. There the counit is
built from summation over the geometric fibres of $e$, the Kummer class of
$\mathcal O_{\mathbf P^1}(1)$, the diagonal class and the splitting of
$Rq_*$ of the constant sheaf on $\mathbf P^1$ into two free summands of rank
one, each of which commutes with extension of coefficients (for the projective
line this is the coefficient compatibility in [sk-prop-geo-p1-adjunction]).
Hence on a chart $c_{A,B}(K)$ is the transpose of the canonical isomorphism
$(e^*p_d^*K(d)[2d])_B\simeq e^*p_d^*(K_B)(d)[2d]$.

