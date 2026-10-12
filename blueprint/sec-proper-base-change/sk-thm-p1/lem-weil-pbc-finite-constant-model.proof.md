+++
kind = "proof"
of = "lem-weil-pbc-finite-constant-model"
+++
If X is empty, Etale.isZero_sheaf_of_isEmpty makes F and the constant sheaf at the zero module zero. Their unique isomorphism gives the model; the zero module is finitely generated.

Otherwise choose x in X and the geometric point s with field SeparableClosure κ(x). Constancy supplies M and F ≅ M_X using Sheaf.mem_essImage_of_isConstant.

The functor sheafFiber maps this isomorphism to an isomorphism on stalks. Compose with Point.sheafFiberConstantSheafIso M to identify F_s with M, then transport finite generation using ConcreteCategory.IsFinitelyGenerated.of_iso and ModuleCat.isFinitelyGenerated_iff.
