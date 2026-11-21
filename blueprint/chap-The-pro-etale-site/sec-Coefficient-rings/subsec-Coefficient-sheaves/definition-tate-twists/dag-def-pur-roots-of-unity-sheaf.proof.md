+++
kind = "proof"
of = "dag-def-pur-roots-of-unity-sheaf"
tags = ["sheaf-dag"]
uses = ["dag-lem-pur-torsion-sheaf-constant-module"]
+++
1. Apply preservation of kernels by the inclusion of abelian sheaves into presheaves and evaluation. Mathlib PreservesKernel.iso and AddCommGrpCat.kernelIsoKer identify sections with the concrete kernel of N times identity on the lifted additive units. Remove ULift and additive notation to identify this kernel with rootsOfUnity. Compatibility with the inclusion is kernelComparison_comp_ι; equality after the subgroup inclusion proves uniqueness. This works also for N=0.
2. Evaluate kernel.condition and use injectivity of the kernel inclusion on sections to prove N annihilates every section. If N divides N prime, write N prime=N*k and use mul_nsmul to deduce annihilation by N prime.
3. Compose the N prime/N multiple of the identity with N times the identity. Bilinearity of composition and Nat.div_mul_cancel identify the resulting exponent with N prime. The kernel equation proves the transition condition, so kernel.lift defines the transition.
4. Apply torsionSheaf_hom_linear with the canonical actions, whose normalization and semilinearity are torsionSheafModuleStructure_spec, using the two annihilation results. This gives the linearity needed for the module morphism. (uses [dag-lem-pur-torsion-sheaf-constant-module])
5. For a prime ell, pow_succ and cancellation by the positive ell^(r+1) give ell^(r+2)/ell^(r+1)=ell. Evaluate kernel.lift_ι on sections and substitute this equality. Functor.ofOpSequence supplies all remaining inverse-system transitions.
