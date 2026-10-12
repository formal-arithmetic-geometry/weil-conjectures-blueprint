+++
kind = "proof"
of = "lem-weil-pbc-dense-open-component-modifications-empty"
+++
For a point x of X, Mathlib irreducibleComponent_mem_irreducibleComponents x supplies an irreducible component. The cover hypothesis supplies i : Fin 0 for that component, contradicting Fin.elim0. Thus the underlying type of X is empty.

Choose the bottom open U. Density is vacuous because X has no points. The open subscheme U is empty; Mathlib AlgebraicGeometry.isIso_of_isEmpty makes every scheme morphism into it an isomorphism, in particular the restriction of the coproduct morphism. No componentwise gluing is needed.
