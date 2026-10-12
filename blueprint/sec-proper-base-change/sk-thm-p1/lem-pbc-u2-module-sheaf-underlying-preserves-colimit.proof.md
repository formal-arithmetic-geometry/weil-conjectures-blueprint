+++
kind = "proof"
of = "lem-pbc-u2-module-sheaf-underlying-preserves-colimit"
+++
Let J be the small etale topology and U the ModuleCat-to-AddCommGrpCat forgetful functor. Apply Mathlib CategoryTheory.GrothendieckTopology.instPreservesSheafification J U; the required preservation of matching-family limits and filtered colimits is supplied by the module and abelian-group forgetful instances. This is the plus-construction sheafification comparison, without changing either sheaf encoding.

Mathlib CategoryTheory.sheafComposeNatIso J U, applied to the module and abelian sheafification adjunctions, identifies presheaf forgetting followed by abelian sheafification with module sheafification followed by sheafCompose J U. Presheaf forgetting preserves colimits by ModuleCat.forget₂PreservesColimitsOfSize and the functor-category instances; abelian sheafification preserves colimits as a left adjoint. Transfer preservation of colimits of shape A through this natural isomorphism using preservesColimitsOfShape_of_natIso.

Apply Mathlib CategoryTheory.Adjunction.preservesColimitsOfShape_iff to the module sheafification adjunction, whose inclusion right adjoint is fully faithful. Preservation by the composite with sheafification from the preceding step gives PreservesColimitsOfShape A (sheafCompose J U), and its instance gives preservation of the specified diagram D.
