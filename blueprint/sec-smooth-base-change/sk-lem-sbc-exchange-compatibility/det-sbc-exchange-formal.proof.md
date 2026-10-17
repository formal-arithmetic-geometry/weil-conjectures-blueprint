+++
kind = "proof"
of = "det-sbc-exchange-formal"
+++
(1) The composition isomorphism $f'^*g^*\simeq u^*f^*$ and the counit $\epsilon_f$ are natural
transformations, so the composite $f'^*g^*Rf_*\to u^*$ is natural in $K$, and adjoint
transposition along $f'^*\dashv Rf'_*$ preserves naturality.

(2) For the identity square the composition isomorphism is the identity, and the adjoint
transpose of $\epsilon_f:f^*Rf_*\to\mathrm{id}$ along $f^*\dashv Rf_*$ is the identity of $Rf_*$
by the triangular identities.

(3) The base change $gh$ has the composite adjunction $(f'')^*\dashv Rf''_*$ on the outer
rectangle, and the counit of a composite adjunction is the composite of the two counits.
Equivalently, the adjoint transpose of the outer composite
$f''^*h^*g^*Rf_*K\simeq u'^*f'^*g^*Rf_*K\simeq u'^*u^*f^*Rf_*K\to u'^*u^*K$ factors
through $u'^*$ applied to the transpose defining $\operatorname{Ex}_{g,f}(K)$ followed by the
counit $\epsilon_{f'}$, which is the defining composite of $\operatorname{Ex}_{h,f'}(u^*K)$.
Transposing gives the asserted factorization. The composition isomorphisms for inverse
images are associative, so the order in which the two directions of a rectangle are
composed does not matter. The same computation with the composite adjunction
$(ef)^*\dashv R(ef)_*$ proves the second pasting formula.
