+++
id = "def-nagata-blowup-universal-graded-map"
kind = "definition"
title = "Graded map induced by an invertible quotient"
order = 271
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup"]
uses = ["def-nagata-extended-ideal", "def-nagata-invertible-ideal", "def-nagata-sheaf-rees-algebra"]
+++
Let $f\colon Y\to X$, let $\mathcal I\subseteq\mathcal O_X$ be a
quasi-coherent ideal, and let
$\mathcal L\hookrightarrow\mathcal O_Y$ be an invertible ideal together with
a surjection $q\colon f^*\mathcal I\twoheadrightarrow\mathcal L$ such that
the composite $\mathcal L\hookrightarrow\mathcal O_Y$ after $q$ is the
canonical map whose image is the extended ideal
$\mathcal I\mathcal O_Y$ of
[def-nagata-extended-ideal]. Define $\alpha_f$ degreewise by the
tensor powers of this quotient:

$$
\alpha_f\colon
f^*\Bigl(\bigoplus_{n\geq0}\mathcal I^n\Bigr)
\longrightarrow\bigoplus_{n\geq0}\mathcal L^{\otimes n}.
$$
