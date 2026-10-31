+++
kind = "proof"
of = "lem-weil-pbc-constant-module-dual"
+++
A finite module over the noetherian coefficient ring has a finite presentation Λᵐ → Λⁿ → M → 0. Apply the exact constant sheaf functor to obtain a presentation of M_X by finite free coefficient sheaves. This includes the zero module by taking a zero presentation.

Internal Hom into the unit turns this cokernel presentation into a kernel: maps from any sheaf T into the internal Hom are maps M_X ⊗ T → Λ_X, and tensoring preserves the presentation cokernel. Duals of the finite free coefficient sheaves are finite free, by the tensor-Hom adjunction, and the resulting map is the transpose of the presenting matrix.

Constant sheafification preserves kernels. The module kernel of the transposed matrix is Hom_Λ(M,Λ), since a map Λⁿ → Λ vanishes on the relations exactly when it factors uniquely through M. Uniqueness of the kernel isomorphism gives the asserted constant sheaf comparison. This does not use projectivity of M.
