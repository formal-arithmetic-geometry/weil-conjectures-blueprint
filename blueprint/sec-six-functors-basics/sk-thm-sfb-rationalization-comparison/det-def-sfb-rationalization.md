+++
id = "det-def-sfb-rationalization"
kind = "definition"
title = "Rationalization of a linear triangulated category"
order = 2200
lean = ["CategoryTheory.Rationalization.torsion", "CategoryTheory.Rationalization.instIsTriangulatedTorsion", "CategoryTheory.Rationalization.W", "CategoryTheory.Rationalization.W_smul_id", "CategoryTheory.Rationalization", "CategoryTheory.Rationalization.Q", "CategoryTheory.Rationalization.isIso_smul_id", "CategoryTheory.Rationalization.linear", "CategoryTheory.Rationalization.algebraMap_smul"]
+++
Let $\mathcal T$ be a triangulated category that is linear over a commutative ring $R$,
with $R$-linear shift functors, and let $M\subseteq R$ be a submonoid. An object $X$ is
*$M$-torsion* if $m\cdot\mathrm{id}_X=0$ for some $m\in M$. The *rationalization*
$\mathcal T[M^{-1}]$ is the Verdier quotient of $\mathcal T$ by the $M$-torsion objects,
i.e. the localization of $\mathcal T$ at the morphisms whose mapping cone is
$M$-torsion. It is a triangulated category, and the localization functor
$\mathcal T\to\mathcal T[M^{-1}]$ is triangulated. Every $m\in M$ acts invertibly on
$\mathcal T[M^{-1}]$, and $\mathcal T[M^{-1}]$ is linear over every localization of $R$ at
$M$, for instance over $R[M^{-1}]$, compatibly with its $R$-linear structure. For
$M=\{\ell^n\}$ write $\mathcal T[\ell^{-1}]$.
