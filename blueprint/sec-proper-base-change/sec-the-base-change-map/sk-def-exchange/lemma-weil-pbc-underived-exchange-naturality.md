+++
id = "lemma-weil-pbc-underived-exchange-naturality"
kind = "lemma"
title = "Sectionwise exchange is natural"
order = 1404
lean = ["AlgebraicGeometry.Etale.baseChangeMap_naturality"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-underived-exchange", "lem-weil-pbc-underived-exchange-sectionwise"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and $\square$ a commutative
square of schemes as in [def-weil-pbc-underived-exchange] (for instance a
cartesian square [def-weil-pbc-cartesian-square]). For every morphism
$u:F\to G$ of $\mathcal A$-valued sheaves on $X_{\Et}$, the square

$$
 \begin{array}{ccc}
 g^{-1}f_*F&\xrightarrow{\Ex^0_{\square,F}}&f'_*g'^{-1}F\\
 g^{-1}f_*u\downarrow&&\downarrow f'_*g'^{-1}u\\
 g^{-1}f_*G&\xrightarrow{\Ex^0_{\square,G}}&f'_*g'^{-1}G
 \end{array}
$$

commutes.
