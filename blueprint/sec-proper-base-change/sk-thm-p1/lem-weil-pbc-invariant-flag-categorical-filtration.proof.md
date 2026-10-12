+++
kind = "proof"
of = "lem-weil-pbc-invariant-flag-categorical-filtration"
+++
Set n=dim M and B_i=F_min(i,n), and equip each B_i with its restricted representation W_i. For i<n use the given inclusions and thereafter the identity on F_n. They are equivariant and injective, hence monic by Rep.mono_iff_injective. W_0 is zero by Rep.isZero_iff since F_0=0. The subtype map W_n→M is injective and surjective since F_n=M, so is an isomorphism in the abelian category Rep.

For stable A⊆B put K=A.comap(B.subtype). The inclusion A→B followed by B→B/K is exact after forgetting to modules: an element mapped to zero lies in K and therefore comes from A. The second map is surjective. The faithful exact forgetful functor reflects exactness by ShortComplex.exact_map_iff_of_faithful. Exact.gIsCokernel gives the quotient cokernel, which is isomorphic to the chosen categorical cokernel. This is the proved private helper cokernel_inclusion_iso_quotient.

For i<n the ranks satisfy dim B_i=i (use F_0=0 at zero and the preceding step otherwise), and dim B_(i+1)=i+1. Submodule.comapSubtypeEquivOfLe identifies K with B_i; Submodule.finrank_quotient_add_finrank gives dimension one for B_(i+1)/K. For any g, the condition g*x-x∈F_i makes the quotient action trivial. A linear equivalence to ULift(ZMod ℓ) exists by FiniteDimensional.nonempty_linearEquiv_of_finrank_eq and finrank_ulift. Its trivial action makes the equivalence equivariant; Rep.mkIso and the quotient/cokernel isomorphism give the required cokernel identification. Every step is proved in Lean from Mathlib, without sorry.
