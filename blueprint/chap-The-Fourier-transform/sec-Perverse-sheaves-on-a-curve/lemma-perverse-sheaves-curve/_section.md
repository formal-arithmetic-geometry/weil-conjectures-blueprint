+++
id = "lemma-perverse-sheaves-curve"
kind = "lemma"
title = "Perverse sheaves on a curve"
order = 1243
lean = ["AlgebraicGeometry.WeilComplex.isCurvePerverseLower_iff_forall_hom_eq_zero", "AlgebraicGeometry.WeilComplex.isCurvePerverse_toComplex_obj", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isCurvePerverse_middleExtension", "AlgebraicGeometry.WeilComplex.isCurvePerverse_of_mono"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-perverse-sheaves-curve", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness"]
+++
The classes ${}^pD^{\le0}$ and ${}^pD^{\ge0}$ of
Definition [definition-perverse-sheaves-curve] form a bounded
t-structure on $D^b_c(C_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)$, and its heart, the category
of perverse sheaves on $C$, is abelian. A punctual sheaf in degree zero
is perverse, and so is $(j_*M)[1]$ for a lisse sheaf $M$ on a dense
open $j:U\hookrightarrow C$.
