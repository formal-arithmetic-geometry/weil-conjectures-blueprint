+++
id = "lemma-weil-pbc-projection-formula-proper-piece"
kind = "lemma"
title = "Proper compactification piece"
order = 2082
lean = ["AlgebraicGeometry.Etale.rightDerivedLowerStarProjectionMap", "AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarProjectionMap_app_app_of_isDualizable"]
uses = ["def-weil-pbc-projection-compactification"]
+++
Let $p:\overline X\to Y$ be the proper morphism of a chosen compactification
[def-weil-pbc-projection-compactification] (the argument uses no property of
$p$). For every $M$ in the derived category of sheaves on $\overline X_{\Et}$,
for instance $M=j_!E$, and every dualizable object $F$ of the derived category
of sheaves on $Y_{\Et}$ (for instance a strict-perfect complex), the
projection map

$$
\pi_{p,M,F}:(Rp_*M)\otimes^LF\longrightarrow Rp_*(M\otimes^LLp^*F),
$$

adjoint to
$Lp^*(Rp_*M\otimes^LF)\cong Lp^*Rp_*M\otimes^LLp^*F
\xrightarrow{\epsilon_M\otimes1}M\otimes^LLp^*F$, is an isomorphism.
