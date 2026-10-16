+++
id = "lem-weil-derived-tensor-functorial"
kind = "lemma"
title = "Functoriality of the derived tensor product"
lean = ["AlgebraicGeometry.ProEtale.derivedTensor_map_app_comp_map"]
order = 2215
uses = ["def-weil-derived-tensor", "def-weil-pbc-proetale-site", "lem-weil-derived-tensor-resolution-independent"]
+++
Fix a scheme $Y$ and a commutative ring $A$, and use the small pro-etale site
[def-weil-pbc-proetale-site] $Y_{\mathrm{proet}}$. For complexes
$K_1,K_2,K_1',K_2'$ of $A_Y$-modules, every pair of morphisms $K_1\to K_1'$
and $K_2\to K_2'$ in $D(Y_{\mathrm{proet}},A)$ induces a morphism

$$
 K_1\otimes_A^LK_2\longrightarrow K_1'\otimes_A^LK_2'
$$

between the objects of [def-weil-derived-tensor], and the assignment carries
identities to identities and composites to composites in each variable.
