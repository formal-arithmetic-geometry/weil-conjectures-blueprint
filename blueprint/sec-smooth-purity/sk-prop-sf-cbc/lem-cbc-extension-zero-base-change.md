+++
id = "lem-cbc-extension-zero-base-change"
kind = "lemma"
title = "Extension by zero commutes with arbitrary base change"
order = 1829
uses = ["def-cbc-open-immersion-square", "def-weil-pbc-extension-by-zero", "def-weil-pbc-geometric-stalks", "def-weil-pbc-inverse-image", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let

$$
\begin{array}{ccc}
U'&\xrightarrow{g_U}&U\\
j'\downarrow&&\downarrow j\\
X'&\xrightarrow{g}&X
\end{array}
$$

be an open-immersion square.
For every abelian sheaf $F$ on $U_{\Et}$ the canonical map

$$
g^{-1}j_!F\xrightarrow{\ \sim\ }j'_!g_U^{-1}F
$$

is an isomorphism, where the canonical map is the one adjoint to the
identification $j'^{-1}g^{-1}=g_U^{-1}j^{-1}$ (the square commutes)
composed with the counit of
[def-weil-pbc-extension-by-zero]. For a finite commutative ring
$\Lambda$ and a complex of $\Lambda$-module sheaves the isomorphism
holds degreewise.
