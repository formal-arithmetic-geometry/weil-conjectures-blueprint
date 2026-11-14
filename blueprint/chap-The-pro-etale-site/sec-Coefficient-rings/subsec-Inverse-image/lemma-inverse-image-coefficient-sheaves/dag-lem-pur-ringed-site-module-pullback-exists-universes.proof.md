+++
kind = "proof"
of = "dag-lem-pur-ringed-site-module-pullback-exists-universes"
tags = ["sheaf-dag"]
+++
1. The free module on the lifted representable at X corepresents sections at X, by the free-module adjunction and lifted Yoneda. Hence direct image has a partial left adjoint there, with value the free module at U(X).
2. Form the coproduct of free lifted representables indexed by all sections of a module presheaf M. Evaluation at the identity gives a sectionwise surjective map to M. Present its kernel by another such coproduct. The resulting cokernel is M. All indices lie in W. Closure of the domain of a partial left adjoint under coproducts and cokernels, using Mathlib Functor.leftAdjointObjIsDefined_of_isColimit, proves existence of the presheaf left adjoint.
3. Pass to a small model of D in the coefficient universe and use Mathlib hasSheafifyEssentiallySmallSite for additive sheafification. Use GrothendieckTopology.WEqualsLocallyBijective.ofEssentiallySmall for its locally-bijective criterion. Mathlib SheafOfModules.PullbackConstruction.adjunction then composes presheaf pullback with module sheafification to give the required sheaf-module adjunction. All these arguments are made directly from Mathlib; no K-flat-complex module is imported. (uses `def-weil-presheaf-modules-sheafification`)

Proof dependencies not drawn: `def-weil-presheaf-modules-sheafification`.
