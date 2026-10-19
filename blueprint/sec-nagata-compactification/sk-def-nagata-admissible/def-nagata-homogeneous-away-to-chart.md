+++
id = "def-nagata-homogeneous-away-to-chart"
kind = "definition"
title = "Homogeneous-localization chart map"
lean = ["AlgebraicGeometry.AffineBlowup.homogeneousAwayToChart", "AlgebraicGeometry.AffineBlowup.coe_homogeneousAwayToChart_mk"]
order = 37
uses = ["def-nagata-blowup-chart-ring", "def-nagata-rees-algebra"]
+++
For $a\in I$, let

$$
\theta_a\colon\mathcal R_A(I)_{(at),0}\longrightarrow A[I/a]
$$

be the ring homomorphism given on degree-zero homogeneous fractions by

$$
\theta_a\!\left(\frac{xt^n}{(at)^n}\right)=\frac{x}{a^n},
\qquad x\in I^n.
$$

The value is independent of the chosen homogeneous representative, and
$\theta_a$ is a well-defined ring homomorphism.
