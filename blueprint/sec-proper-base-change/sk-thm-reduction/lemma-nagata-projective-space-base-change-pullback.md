+++
id = "lemma-nagata-projective-space-base-change-pullback"
kind = "lemma"
title = "Projective space commutes with base change"
order = 1191
lean = ["AlgebraicGeometry.ProjectiveSpace.isPullback_map"]
uses = ["def-nagata-affine-proj", "def-nagata-projective-space-base-change"]
+++
For every index set $n$ and every morphism of schemes $g\colon X\to S$, the
square

$$
\begin{array}{ccc}
\mathbf P(n;X) & \longrightarrow & \mathbf P(n;S)\\
\downarrow & & \downarrow\\
X & \xrightarrow{\ g\ } & S
\end{array}
$$

is cartesian, that is, $\mathbf P(n;X)\cong X\times_S\mathbf P(n;S)$ over
$X$.
