+++
id = "def-nagata-module-strict-transform"
kind = "definition"
title = "Strict transform of a quasi-coherent module"
order = 332
uses = ["def-nagata-global-blowup", "def-nagata-power-torsion"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

For a morphism $f\colon Y\to X$, a quasi-coherent
$\mathcal O_Y$-module $\mathcal F$, a finite-type quasi-coherent ideal
$\mathcal I\subseteq\mathcal O_X$, and its blow-up
$X'=\operatorname{Bl}_{\mathcal I}(X)$, define the pullback center ideal on
$Y\times_XX'$ to be the image of
$\mathcal I\mathcal O_{X'}$ in $\mathcal O_{Y\times_XX'}$. The strict
transform of $\mathcal F$ is its pullback to $Y\times_XX'$ modulo the
subsheaf of sections killed locally by a power of this named ideal.
