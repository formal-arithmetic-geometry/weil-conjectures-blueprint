+++
kind = "proof"
of = "lem-weil-pbc-colimit-rings-flat"
+++
Apply the equational criterion to the target ring S as an R-module through ψ. It suffices to trivialize every finite relation ∑ₖ rₖ • xₖ = 0.

Every element of a filtered colimit of rings comes from some stage; choose stage representatives aₖ of each coefficient rₖ. Filteredness supplies an object j receiving morphisms from all of the finitely many representing objects, including the empty family. Transport aₖ to bₖ in Rⱼ. The coprojection equations give ιⱼ(bₖ) = rₖ.

Regard S as an Rⱼ-module through ψ ∘ ιⱼ. The relation ∑ₖ bₖ • xₖ = 0 is the original relation because ιⱼ(bₖ) = rₖ. This module is flat by hypothesis. The forward equational criterion gives a finite matrix cₖₜ in Rⱼ and elements yₜ in S with xₖ = ∑ₜ cₖₜ • yₜ and ∑ₖ bₖ cₖₜ = 0.

Use the matrix ιⱼ(cₖₜ) over R and the same yₜ. Its action on S is unchanged by the definition of the composite map. Applying the ring homomorphism ιⱼ to ∑ₖ bₖ cₖₜ = 0 yields ∑ₖ rₖ ιⱼ(cₖₜ) = 0. This is a trivialization of the original relation. The backward equational criterion proves flatness.
