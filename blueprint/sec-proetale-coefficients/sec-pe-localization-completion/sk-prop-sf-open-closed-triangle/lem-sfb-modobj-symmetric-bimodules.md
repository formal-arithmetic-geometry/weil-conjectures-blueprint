+++
id = "lem-sfb-modobj-symmetric-bimodules"
kind = "lemma"
title = "Module objects over a commutative monoid are symmetric bimodules"
order = 1146
uses = ["det-def-sfb-module-objects-definition"]
lean = ["CategoryTheory.Mod.toBimodObj", "CategoryTheory.Mod.toBimod", "CategoryTheory.Mod.fullyFaithfulToBimod", "Bimod.IsSymmetric", "Bimod.isSymmetric_toBimodObj"]
+++
Let $\mathcal C$ be a braided monoidal category with braiding $\beta$, and let
$\mathcal R$ be a commutative monoid object of $\mathcal C$. Let $M$ be an
$\mathcal R$-module object ([det-def-sfb-module-objects-definition]). Then the left action $\gamma_M$
and the right action
$$
\rho_M:=\gamma_M\circ\beta_{M,\mathcal R}\colon M\otimes\mathcal R\to M
$$
make $M$ an $\mathcal R$-$\mathcal R$-bimodule. Call a bimodule *symmetric* if its right
action is the braiding followed by its left action. The functor
$M\mapsto(M,\gamma_M,\rho_M)$ from $\Mod_{\mathcal R}(\mathcal C)$ to
$\mathcal R$-$\mathcal R$-bimodules is fully faithful, and its values are symmetric
bimodules.
