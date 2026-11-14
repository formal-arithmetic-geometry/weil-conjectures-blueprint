+++
kind = "proof"
of = "dag-def-pur-proetale-structure-sheaf"
tags = ["sheaf-dag"]
+++
1. Restrict the global-sections functor Scheme.Γ along the opposite of the forgetful functor from the small pro-etale site [dag-def-weil-pbc-small-proetale-site] to schemes `def-pc-scheme`. This is exactly proEtaleStructurePresheaf, so the values and restriction maps are unchanged.
2. For every commutative ring R, the affine-target adjunction `lem-weil-pbc-morphism-into-affine-scheme` identifies the presheaf U ↦ Hom(R, Γ(U, O_U)) naturally with Hom(U, Spec R). The source library packages this as ΓSpec.representableBy. The big pro-etale topology is subcanonical: it is coarser than the fpqc topology, whose representable descent is `lem-weil-pbc-fpqc-representable-descent`. Hence each of these Hom presheaves is a sheaf. By the definition of the sheaf condition for a category-valued presheaf, Scheme.Γ is therefore a ring-valued sheaf. This is precisely the proved source-library theorem Scheme.isSheaf_Γ applied to proetaleTopology. (uses `lem-weil-pbc-morphism-into-affine-scheme`, `lem-weil-pbc-fpqc-representable-descent`)
3. The forgetful functor ProEt.forget S ⋙ Over.forget S is continuous from the small pro-etale topology [dag-def-weil-pbc-small-proetale-site] to the big pro-etale topology, as proved in Mathlib.AlgebraicGeometry.Sites.Proetale. Apply Functor.op_comp_isSheaf_of_isSheaf to the ring-valued sheaf of the previous step. Its conclusion is definitionally the sheaf condition of proEtaleStructurePresheaf S. Bundle that presheaf with this proof to obtain proEtaleStructureSheaf S.

Proof dependencies not drawn: `lem-weil-pbc-morphism-into-affine-scheme`, `lem-weil-pbc-fpqc-representable-descent`.
