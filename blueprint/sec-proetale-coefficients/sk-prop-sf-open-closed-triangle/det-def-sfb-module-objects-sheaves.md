+++
id = "det-def-sfb-module-objects-sheaves"
kind = "definition"
title = "Sheaves of $\\Lambda_X$-modules"
uses = ["det-def-sfb-module-objects-definition", "det-def-sfb-module-objects-category", "det-def-sfb-pulled-back-coefficients-ring", "det-def-sfb-sheaf-tensor-structure", "def-weil-pbc-proetale-site"]
lean = ["CategoryTheory.Mod", "AlgebraicGeometry.ProEtale.condensedRingObj", "AlgebraicGeometry.ProEtale.sheafMonoidalCategory"]
order = 1171
+++
Let $X$ be a scheme with small pro-étale site $X_{\mathrm{proét}}$ ([def-weil-pbc-proetale-site]),
and give $\Sh(X_{\mathrm{proét}},\Ab)$ the tensor product of [det-def-sfb-sheaf-tensor-structure]
(sheafified objectwise $\otimes_{\mathbf Z}$, unit $\underline{\mathbf Z}$). Let $\Lambda$ be a condensed
ring and $\Lambda_X=p_X^*\Lambda$ the ring object of $\Sh(X_{\mathrm{proét}},\Ab)$ of
[det-def-sfb-pulled-back-coefficients-ring]. The category of *sheaves of $\Lambda_X$-modules* is
$$
\Mod_{\Lambda_X}:=\Mod_{\Lambda_X}\bigl(\Sh(X_{\mathrm{proét}},\Ab)\bigr)
$$
of [det-def-sfb-module-objects-definition]: an object is an abelian sheaf $M$ on $X_{\mathrm{proét}}$
with a morphism of sheaves $\gamma_M\colon\Lambda_X\otimes M\to M$ satisfying the unit and
associativity axioms, and morphisms are morphisms of abelian sheaves commuting with the actions. It
is a category with a faithful forgetful functor to $\Sh(X_{\mathrm{proét}},\Ab)$
([det-def-sfb-module-objects-category]), and $\Lambda_X$ itself is an object (the regular module).
