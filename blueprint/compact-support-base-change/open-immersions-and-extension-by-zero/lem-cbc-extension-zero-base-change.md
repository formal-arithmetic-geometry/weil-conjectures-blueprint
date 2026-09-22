+++
id = "lem-cbc-extension-zero-base-change"
kind = "lemma"
title = "Extension by zero commutes with arbitrary base change"
order = 6604
lean = ["AlgebraicGeometry.Etale.extensionByZero_baseChange"]
uses = ["def-cbc-open-immersion-square", "def-cbc-extension-by-zero"]
+++
Let
$$
 \begin{array}{ccc}
 U'&\xrightarrow{g_U}&U\\
 j'\downarrow&&\downarrow j\\
 X'&\xrightarrow{g}&X
 \end{array}
$$
be an open-immersion square ([def-cbc-open-immersion-square]). For every
abelian sheaf $F$ on $U_{\Et}$ the canonical map
$$
 g^{-1}j_!F\xrightarrow{\ \sim\ }j'_!g_U^{-1}F
$$
is an isomorphism; it is the mate of the identification
$j'^{-1}g^{-1}=g_U^{-1}j^{-1}$ (the square commutes) composed with the counit
of the extension-by-zero adjunction. For a finite commutative ring $\Lambda$
and a complex of $\Lambda$-module sheaves the isomorphism holds degreewise.

*Import note.* The displayed sentence describing the map is truncated in the
source (a stray line break leaves an isolated `u`); it has been completed here
in the obvious way, as the mate of the stated identification.

## Proof

Fix a geometric point $\bar x'$ of $X'$ with image $\bar x=g(\bar x')$.
By the stalk characterization of [def-cbc-extension-by-zero],
$$
 (g^{-1}j_!F)_{\bar x'}=(j_!F)_{\bar x}=
 \begin{cases}
 F_{\bar x},& \bar x\in U,\\
 0,&\bar x\in X\setminus U,
 \end{cases}
 \qquad
 (j'_!g_U^{-1}F)_{\bar x'}=
 \begin{cases}
 (g_U^{-1}F)_{\bar x'}=F_{\bar x},&\bar x'\in U',\\
 0,&\bar x'\in X'\setminus U',
 \end{cases}
$$
and $\bar x\in U$ if and only if $\bar x'\in U'$ because the square is
cartesian. Under these identifications the two stalks of the map agree (the
adjoint construction of the map is precisely the corresponding restriction of
sections); the inverse image functors are exact, and the conservativity of
geometric stalks makes the map an isomorphism. For complexes the argument
applies termwise, exactness of $j_!$ giving the derived statement.

Unresolved dependencies: def:weil-pbc-extension-by-zero, def:weil-pbc-inverse-image, def:weil-pbc-geometric-stalks, lem:weil-pbc-geometric-stalk-conservative
