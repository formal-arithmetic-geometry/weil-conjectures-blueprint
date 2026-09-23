+++
id = "def-weil-pbc-cartesian-square-detailed"
kind = "definition"
title = "Cartesian square with chosen identification"
order = 1279
uses = ["def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions"]
+++
A *cartesian square* $\square=(f,f',g,g',\alpha)$ is a diagram

$$
 \begin{array}{ccc}
 X'&\xrightarrow{g'}&X\\
 f'\downarrow&&\downarrow f\\
 Y'&\xrightarrow{g}&Y
 \end{array}
$$

of scheme morphisms [def-weil-pbc-scheme-conventions] together with a chosen
identification $\alpha:X'\xrightarrow{\sim}X\times_YY'$ and the corresponding
equality $fg'=gf'$. This choice gives a specified natural isomorphism

$$
 \theta_\square:f'^{-1}g^{-1}\xrightarrow{\sim}g'^{-1}f^{-1}
$$

of inverse image [def-weil-pbc-inverse-image] functors, compatible with
identities and pasted squares.
