+++
id = "lem-weil-pbc-horseshoe-defect-factorization"
kind = "lemma"
title = "Factorization and cocycle identities of horseshoe defects"
uses = ["def-sp-abelian", "def-sp-injective-resolutions"]
lean = ["CategoryTheory.InjectiveResolution.horseshoe_defect_factorization"]
+++
Let C be an abelian category [def-sp-abelian], S and T short exact sequences in C,
and F a morphism from S to T. Let IA, IB, IC and JA, JB, JC be injective resolutions
[def-sp-injective-resolutions] of the three terms of S and T respectively. Let
alpha, beta and alpha', beta' be chain maps between the corresponding resolutions,
with zero composites, with short exact rows in every nonnegative degree, and with
all four augmentation squares commuting. Let phiA and phiC be prescribed chain maps
between the first and third resolutions respectively, lifting the first and third
components of F. Let t be a family of maps from IB in degree n to JB in degree n,
commuting with both outer row squares in every degree. Then there exist maps E from IC in degree n to JA in degree n+1, and e from S.X3
to JA in degree zero, satisfying these four identities (all composition below is diagrammatic):
(1) beta E alpha' is t followed by the target differential minus the source differential
followed by t in the next degree; (2) S.g e alpha' in degree zero is the difference
between the augmentation followed by t and the prescribed middle augmentation;
(3) the IC augmentation followed by E in degree zero equals e followed by the JA differential;
(4) the IC differential followed by E in the next degree is minus E followed by
the JA differential in the next degree.
