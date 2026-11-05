+++
id = "corollary-h-1-c-stalk-fourier"
kind = "corollary"
title = "$H^1_c$ as a stalk of the Fourier transform"
order = 1290
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.nonempty_equiv_stalk_origin_of_isFourierPartner", "AlgebraicGeometry.hasWeightsAtMost_compactlySupportedCohomology_one"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-sp-unique-adjoint", "definition-weights", "lemma-artin-schreier-character-sheaf", "proposition-fourier-transform-middle-extension", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
We have $H_c^2(\mathbf A^1,j_*M)=0$, and there is a Frobenius-equivariant
isomorphism $H_c^1(\mathbf A^1,j_*M)\simeq(j'_*M')_{0'}$ with the stalk
at the origin $0'$ of the dual line. In particular $H_c^1(\mathbf A^1,j_*M)$
has weights at most $w+1$.
