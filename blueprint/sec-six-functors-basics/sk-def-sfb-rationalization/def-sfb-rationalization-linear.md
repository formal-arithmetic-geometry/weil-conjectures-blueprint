+++
id = "def-sfb-rationalization-linear"
kind = "definition"
title = "Linear structure of the rationalization"
order = 1632
uses = ["def-sfb-rationalization-quotient", "lem-sfb-smul-id-in-w"]
lean = ["CategoryTheory.Rationalization.isIso_smul_id", "CategoryTheory.Rationalization.linear"]
+++
In the situation of [def-sfb-rationalization-quotient], for every $m\in M$ and every
object $Y$ of $\mathcal T[M^{-1}]$, the morphism $m\cdot\mathrm{id}_Y$ is an isomorphism.
Consequently, for every localization $A$ of $R$ at $M$ (for instance $A=R[M^{-1}]$), the
action of $R$ on $\mathcal T[M^{-1}]$ extends uniquely to an $A$-linear structure, with
$\bar r\cdot f=r\cdot f$ for the image $\bar r\in A$ of $r\in R$.
