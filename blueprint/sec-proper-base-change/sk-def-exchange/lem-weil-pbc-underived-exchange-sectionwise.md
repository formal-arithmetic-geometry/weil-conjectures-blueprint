+++
id = "lem-weil-pbc-underived-exchange-sectionwise"
kind = "lemma"
title = "Well-definedness of the sectionwise exchange rule"
order = 1037
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-weil-pbc-underived-exchange"]
+++
Let $\square$ be a cartesian square
[def-weil-pbc-cartesian-square], let $F\in\Ab(X_{\Et})$, and let
$V\to Y'$ be etale. For a representative of a section of $g^{-1}f_*F$ over
$V$, consisting of an etale $W\to Y$, a map $V\to W\times_YY'$, and a section
of $F$ on $X\times_YW$, restrict that section along $X'\times_{Y'}V\to
X\times_YW$ and sheafify. The resulting section of $f'_*g'^{-1}F$ over $V$
depends only on the class of that representative in $(g^{-1}f_*F)(V)$, and it
is the section corresponding to the underived exchange morphism
$\Ex^0_{\square,F}$ of [def-weil-pbc-underived-exchange] under the
adjunction $f'^{-1}\dashv f'_*$.
