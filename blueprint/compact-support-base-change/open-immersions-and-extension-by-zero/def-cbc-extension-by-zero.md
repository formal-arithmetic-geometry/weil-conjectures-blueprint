+++
id = "def-cbc-extension-by-zero"
kind = "definition"
title = "Extension by zero"
order = 6603
lean = ["AlgebraicGeometry.Etale.extensionByZero"]
uses = ["def-cbc-open-immersion-square"]
+++
For an open immersion $j:U\hookrightarrow X$, *extension by zero* is the
functor
$$
 j_!:\Ab(U_{\Et})\longrightarrow\Ab(X_{\Et})
$$
the exact functor left adjoint to $j^{-1}$, acting by
$$
 (j_!F)_{\bar x}=
 \begin{cases}
 F_{\bar x_U},&\bar x\text{ lies in }U,\\
 0,&\bar x\text{ lies in }X\setminus U,
 \end{cases}
$$
on geometric stalks, and exact, hence acting degreewise on complexes. For a
finite commutative ring $\Lambda$ the same construction is used for sheaves of
$\Lambda$-modules.

Unresolved dependencies: def:weil-pbc-extension-by-zero, def:weil-pbc-etale-site, def:weil-pbc-geometric-stalks, def:weil-pbc-scheme-conventions
