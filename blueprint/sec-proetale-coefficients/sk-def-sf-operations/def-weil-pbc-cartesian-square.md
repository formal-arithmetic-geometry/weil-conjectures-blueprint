+++
id = "def-weil-pbc-cartesian-square"
kind = "definition"
title = "Cartesian square and chosen pullback identification"
order = 1002
lean = ["AlgebraicGeometry.Etale.squareUpperStarIso", "AlgebraicGeometry.Etale.squareUpperStarIso_paste_horiz_hom", "AlgebraicGeometry.Etale.squareUpperStarIso_paste_vert_hom"]
uses = ["def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions"]
+++
Consider a commutative square of scheme morphisms
[def-weil-pbc-scheme-conventions]

$$
\begin{CD}
X' @>{g'}>> X\\
@V{f'}VV       @VV{f}V\\
Y' @>{g}>> Y,
\end{CD}
$$

that is, $f\circ g'=g\circ f'$ as maps to $Y$, and let $\mathcal A$ be a
Grothendieck abelian coefficient category for which presheaves on small
etale sites can be sheafified. The *square isomorphism* of the square is
the natural isomorphism

$$
 \theta_\square:f'^{-1}g^{-1}\xrightarrow{\sim}g'^{-1}f^{-1}
$$

of inverse image [def-weil-pbc-inverse-image] functors from
$\mathcal A$-valued etale sheaves on $Y$ to $\mathcal A$-valued etale
sheaves on $X'$, obtained by identifying both sides with the inverse image
along the common composite $fg'=gf':X'\to Y$ through the composition
isomorphisms of inverse images.

A *cartesian square* $\square=(f,f',g,g',\alpha)$ is such a commutative
square together with a chosen identification
$\alpha:X'\xrightarrow{\sim}X\times_YY'$ compatible with the maps; the
notation $g'^{-1}F$ always means inverse image using this specified
identification.

The square isomorphisms are compatible with identities and with pasting:
for two commutative squares pasted horizontally (or vertically), the
square isomorphism of the composite square is the composite of the two
square isomorphisms, modulo the composition isomorphisms of inverse
images along the horizontal (respectively vertical) maps.
