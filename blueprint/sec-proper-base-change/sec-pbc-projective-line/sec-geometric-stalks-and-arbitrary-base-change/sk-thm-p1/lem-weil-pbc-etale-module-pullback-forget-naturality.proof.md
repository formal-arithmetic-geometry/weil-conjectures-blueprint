+++
kind = "proof"
of = "lem-weil-pbc-etale-module-pullback-forget-naturality"
uses = ["def-weil-pbc-inverse-image"]
+++
The forgetful functor U:ModuleCat Λ→AddCommGrpCat preserves colimits of size u+1, by Mathlib ModuleCat.forget₂PreservesColimitsOfSize. It preserves the limits and covering-sieve colimits in the plus construction, so GrothendieckTopology.instPreservesSheafification gives the sheafification comparison sheafComposeNatIso. All these are natural transformations of functors.

Set L equal to the opposite of the small-etale base-change functor. Preservation of comma-category colimits supplies PreservesPointwiseLeftKanExtensionAt at each object. Since these pointwise Kan extensions exist, preservesPointwiseLKEOfHasPointwiseAndPreservesPointwise supplies preservation of left Kan extensions. Mathlib Functor.lanCompIsoOfPreserves now gives the natural isomorphism L.lan ⋙ whiskeringRight(U) ≅ whiskeringRight(U) ⋙ L.lan.

Unfold upperStar as sheafToPresheaf ⋙ L.lan ⋙ presheafToSheaf. Compose the inverse sheafification comparison with the Kan-extension comparison and whisker by sheafToPresheaf. Insert the associativity isomorphisms of functor composition. The remaining source presheaf functors are definitionally equal, closed by Iso.refl. This constructs one natural isomorphism of the two displayed functors, so its naturality holds for every sheaf morphism. Identity maps, zero rings and empty schemes require no separate choices or extra hypotheses. ([def-weil-pbc-inverse-image]).
