+++
id = "def-weil-pbc-cartesian-square"
kind = "definition"
title = "Cartesian square and chosen pullback identification"
order = 1508
lean = ["AlgebraicGeometry.Etale.squareUpperStarIso"]
+++
For schemes and morphisms

$$
\begin{CD}
X' @>{g'}>> X\\
@V{f'}VV       @VV{f}V\\
Y' @>{g}>> Y,
\end{CD}
$$

we write $\square=(f,f',g,g',\alpha)$ when
$\alpha:X'\xrightarrow{\sim}X\times_Y Y'$ is a specified isomorphism and
$f\circ g'=g\circ f'$ as maps to $Y$. The notation
$g'^{-1}F$ always means inverse image using this specified identification.
