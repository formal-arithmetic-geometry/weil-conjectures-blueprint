+++
id = "def-weil-pbc-extension-by-zero"
kind = "definition"
title = "Extension by zero for open immersions"
order = 1159
lean = ["AlgebraicGeometry.Etale.lowerShriek", "AlgebraicGeometry.Etale.lowerShriekAdjunction", "AlgebraicGeometry.Etale.lowerShriek_stalk"]
+++
For an open immersion $j:U\hookrightarrow X$, extension by zero is the exact
functor

$$
 j_!:\Ab(U_{\Et})\longrightarrow\Ab(X_{\Et})
$$

left adjoint to $j^{-1}$. It is characterized on geometric stalks by

$$
 (j_!F)_{\bar x}=
 \begin{cases}
 F_{\bar x},&\bar x\text{ lies in }U,\\
 0,&\bar x\text{ lies in }X\setminus U.
 \end{cases}
$$

Unresolved dependencies: def:weil-pbc-etale-sheaves, def:weil-pbc-etale-site, def:weil-pbc-geometric-stalks, def:weil-pbc-scheme-conventions
