+++
id = "proposition-exceptional-inverse-image-smooth-morphism--5"
kind = "proposition"
title = "Tensor description of exceptional inverse image"
order = 561006
aliases = ["bp-r169-5"]
lean = ["AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor"]
uses = ["definition-relative-dualizing-complex", "theorem-existence-exceptional-inverse-image"]
+++
For every $N\in D(S_{\acute{e}t},A)$, the canonical map
$$
\theta_{f,N}:\omega_f\otimes_A^{\mathbf L}f^*N\longrightarrow f^!N
$$
is an isomorphism. It is the adjoint transpose of the inverse projection
formula followed by the counit and the unit identification:
$$
Rf_!(\omega_f\otimes_A^{\mathbf L}f^*N)
\simeq Rf_!\omega_f\otimes_A^{\mathbf L}N
\longrightarrow A_S\otimes_A^{\mathbf L}N\simeq N.
$$
Composing $\theta_{f,N}$ with the symmetry of the derived tensor product
gives the isomorphism
$$
\mu_N:f^*N\otimes_A^{\mathbf L}\omega_f\longrightarrow f^!N
\tag{6.11}
$$
with the factors in the order used in the human statement.
