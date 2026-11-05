+++
id = "proposition-exceptional-inverse-image-smooth-morphism--8"
kind = "proposition"
title = "Compatibility with the tensor description"
order = 561009
aliases = ["bp-r169-8"]
lean = ["CategoryTheory.Adjunction.projectionTensorMap_mateEquiv"]
uses = ["definition-exceptional-base-change-map", "theorem-existence-exceptional-inverse-image"]
+++
Let $A$ be any finite commutative ring. Let $g'^*f^!\to f'^!g^*$ be the canonical base change map of a cartesian
square, with $f$ and $f'$ compactifiable and $f'$ quasi-compact. Smoothness
is not needed for the following compatibility. For $M,N\in D(S_{\acute{e}t},A)$,
write
$$
\tau_f(M,N):f^!M\otimes_A^{\mathbf L}f^*N
\longrightarrow f^!(M\otimes_A^{\mathbf L}N)
$$
for the tensor map obtained from the projection formula by adjunction.
Under the canonical pullback and tensor identifications,
$$
\beta_{M\otimes_A^{\mathbf L}N}\circ g'^*\tau_f(M,N)
=
\tau_{f'}(g^*M,g^*N)\circ(\beta_M\otimes 1).
$$
Taking $M=A_S$ gives compatibility of $\theta_{f,N}$ with base change;
using symmetry gives the compatibility for $\mu_N$ in (6.11).
