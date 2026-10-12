+++
kind = "proof"
of = "k1-constant-mod-sheaf-prime-coefficient-identification"
+++
The characteristic-r simplification shows Ideal.span {(r : ULift (ZMod r))} = bottom. Apply Submodule.quotEquivOfEqBot, convert the linear equivalence with LinearEquiv.toModuleIso, and map this isomorphism through constantSheaf. The result has the required source by unfolding Etale.constantModSheaf.
