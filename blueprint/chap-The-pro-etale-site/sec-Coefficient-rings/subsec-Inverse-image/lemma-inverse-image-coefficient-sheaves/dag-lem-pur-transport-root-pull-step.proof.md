+++
kind = "proof"
of = "dag-lem-pur-transport-root-pull-step"
tags = ["sheaf-dag"]
+++
1. Use sheafification hom-extensionality to check rootComparison_transition on presheaf generators. The defining generator normalization identifies both sides with the m-th power of the same root; the kernel transition formula uses (m*N)/N=m for positive N. Conjugate the existing roots_inverse_transition equality by rootComparison. Include the equality transport ell^(n+1)=ell*ell^n by substitution to obtain rootPull_step. (uses `lem-pur-roots-of-unity-inverse-image-iso`)

Proof dependencies not drawn: `lem-pur-roots-of-unity-inverse-image-iso`.
