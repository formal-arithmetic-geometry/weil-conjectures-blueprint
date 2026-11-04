+++
id = "lemma-reduction-curve-over-normal-base"
kind = "lemma"
title = "Reduction to a curve over a normal base"
order = 675
lean = ["AlgebraicGeometry.Etale.CurveTestDatum", "AlgebraicGeometry.Etale.exists_curveTestDatum"]
uses = ["definition-derived-base-change-map"]
+++
Suppose $g:Y'\to Y$ is affine and smooth of relative dimension
one, $n$ is invertible on $Y$, and $\mathrm{BC}(g,n,q-1)$ holds. If
$\mathrm{BC}(g,n,q)$ fails, there are an affine scheme
$S=\operatorname{Spec}R$ over $Y$ with $R$ a normal domain whose fraction
field $L$ is algebraically closed, an algebraically closed extension
field $\Omega$ of $L$, an integer $m\mid n$, and, for the smooth affine curve
$C=Y'\times_YS$, the cartesian square

$$
\begin{CD}
C_\Omega @>{h}>> C\\
@VVV @VVV\\
\operatorname{Spec}\Omega @>>> S
\end{CD}
$$

such that

$$
R^qh_*\underline{\mathbf Z/m}\ne0.
$$
