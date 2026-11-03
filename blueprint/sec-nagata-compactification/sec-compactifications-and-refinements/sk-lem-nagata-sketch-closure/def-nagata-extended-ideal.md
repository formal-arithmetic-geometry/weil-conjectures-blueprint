+++
id = "def-nagata-extended-ideal"
kind = "definition"
title = "Extended ideal along a morphism"
order = 37
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.comap"]
+++
For $f\colon Y\to X$ and a quasi-coherent ideal
$\mathcal I\subseteq\mathcal O_X$ with closed subscheme
$V(\mathcal I)\hookrightarrow X$, define $\mathcal I\mathcal O_Y$ to be the
ideal sheaf of the closed subscheme

$$
Y\times_XV(\mathcal I)\hookrightarrow Y,
$$

that is, the kernel ideal of the first projection
$Y\times_XV(\mathcal I)\to Y$. Equivalently, it is the image ideal of the
composite $f^*\mathcal I\to f^*\mathcal O_X\to\mathcal O_Y$.
