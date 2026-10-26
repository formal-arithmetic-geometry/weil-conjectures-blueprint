+++
id = "def-sfb-rationalization-linear"
kind = "definition"
title = "Linear structure of the rationalization"
order = 2178
uses = ["def-sfb-rationalization-quotient", "lem-sfb-smul-id-in-w"]
lean = ["CategoryTheory.Rationalization.isIso_smul_id", "CategoryTheory.Rationalization.toCatCenter", "CategoryTheory.Rationalization.linear", "CategoryTheory.Rationalization.algebraMap_smul"]
+++
In the situation of [def-sfb-rationalization-quotient], for every $m\in M$ and every
object $Y$ of $\mathcal T[M^{-1}]$, the morphism $m\cdot\mathrm{id}_Y$ is an isomorphism.
Consequently, for every localization $A$ of $R$ at $M$ (for instance $A=R[M^{-1}]$), the
ring map $R\to Z(\mathcal T[M^{-1}])$ to the center (the endomorphisms of the identity
functor) given by the $R$-action extends along $R\to A$, and the resulting ring map
$A\to Z(\mathcal T[M^{-1}])$ makes $\mathcal T[M^{-1}]$ an $A$-linear category, with
$\bar r\cdot f=r\cdot f$ for the image $\bar r\in A$ of $r\in R$.
