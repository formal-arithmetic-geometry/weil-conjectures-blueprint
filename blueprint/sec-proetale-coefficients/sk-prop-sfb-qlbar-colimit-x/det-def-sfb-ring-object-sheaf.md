+++
id = "det-def-sfb-ring-object-sheaf"
kind = "lemma"
title = "Sheaves of rings are ring objects of abelian sheaves"
lean = ["CategoryTheory.Sheaf.sheafifyRingPresheafIso", "CategoryTheory.Sheaf.monObj_sheafCompose_obj", "CategoryTheory.Sheaf.isMonHom_sheafifyRingPresheafIso_hom", "CategoryTheory.Sheaf.isCommMonObj_sheafCompose_obj", "CategoryTheory.Sheaf.isMonHom_sheafCompose_map"]
order = 1238
uses = ["det-def-sfb-ring-object-presheaf"]
+++
In the situation of [det-def-sfb-ring-object-presheaf], let $\mathcal R$ be a sheaf of rings on
$C$. Then its underlying abelian presheaf $\mathcal R_{\Ab}$ is a sheaf, and it carries a unique
ring object structure in $\Sh(C,\Ab)$ such that the counit isomorphism
$a(\mathcal R_{\Ab})\cong\mathcal R_{\Ab}$ is an isomorphism of ring objects, where
$a(\mathcal R_{\Ab})$ has the structure of [det-def-sfb-ring-object-presheaf]. Concretely, its
multiplication $\mathcal R_{\Ab}\otimes\mathcal R_{\Ab}=a(\mathcal R_{\Ab}\otimes_p\mathcal R_{\Ab})\to\mathcal R_{\Ab}$
is the unique morphism of sheaves extending the objectwise ring multiplication, and its unit
$\underline{\mathbf Z}\to\mathcal R_{\Ab}$ is the unique morphism extending $n\mapsto n\cdot1$. It is
commutative when all rings $\mathcal R(U)$ are commutative, and a morphism of sheaves of rings is
a morphism of ring objects.
