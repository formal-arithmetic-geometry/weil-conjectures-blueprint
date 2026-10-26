+++
id = "det-def-sfb-module-objects-category"
kind = "lemma"
title = "$\\Mod_{\\mathcal R}(\\mathcal C)$ is a category with a faithful forgetful functor"
uses = ["det-def-sfb-module-objects-definition"]
lean = ["CategoryTheory.Mod.id", "CategoryTheory.Mod.comp", "CategoryTheory.Mod.hom_ext", "CategoryTheory.Mod.forget", "CategoryTheory.Mod.regular"]
order = 1128
+++
In the situation of [det-def-sfb-module-objects-definition]:

1. identities are morphisms of module objects, and composites of morphisms of module objects are
   morphisms of module objects, so $\Mod_{\mathcal R}(\mathcal C)$ is a category;
2. the forgetful functor $\Mod_{\mathcal R}(\mathcal C)\to\mathcal C$ is a faithful functor;
3. the regular module $(\mathcal R,\mu)$ is an $\mathcal R$-module object.
