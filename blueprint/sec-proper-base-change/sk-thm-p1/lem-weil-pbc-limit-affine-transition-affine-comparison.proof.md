+++
kind = "proof"
of = "lem-weil-pbc-limit-affine-transition-affine-comparison"
+++
Install affineness of every stage. Mathlib Scheme.isAffine_of_isLimit gives affineness of c.pt. Applying isColimitOfPreserves Scheme.Γ to hc.op gives a colimit cocone of global sections, using Mathlib preservesColimit_Γ for affine stages.

Let eΓ be the unique isomorphism from Γ(c.pt) to the chosen ring colimit. Compose c.pt.isoSpec with Scheme.Spec.mapIso eΓ.symm.op. The coprojection equation comp_coconePointUniqueUpToIso_inv and Spec.map_comp reduce projection compatibility to Scheme.isoSpec_hom_naturality.
