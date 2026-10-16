+++
id = "def-nagata-flat-pullback-rees-map"
kind = "definition"
title = "Flat pullback map for Rees algebras"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.reesPullbackData"]
order = 122
uses = ["def-nagata-extended-ideal", "def-nagata-sheaf-rees-algebra"]
+++
For a quasi-coherent ideal $\mathcal I\subseteq\mathcal O_X$ and flat
$g\colon Y\to X$, define $\beta_g$ degreewise by the canonical
maps

$$
g^*(\mathcal I^n)\longrightarrow
(\mathcal I\mathcal O_Y)^n.
$$

Thus

$$
\beta_g\colon g^*\mathcal R_X(\mathcal I)\longrightarrow
\mathcal R_Y(\mathcal I\mathcal O_Y).
$$
