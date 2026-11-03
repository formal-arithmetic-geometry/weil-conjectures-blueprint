+++
kind  = "proof"
of    = "lem-finrepair-modification-extension-zero"
+++
Extension by zero commutes with pullback here: the map
$\pi^*j_!G\to j'_!G'$ is obtained from its identity restriction on
$U'$, and is an isomorphism on every geometric stalk.
Over a point of $U'$ both stalks are the stalk of $G$;
outside $U'$ both are zero.
This uses the stalk descriptions in
[def-weil-pbc-inverse-image], [def-weil-pbc-extension-by-zero]
and conservativity in
[lemma-weil-pbc-geometric-stalk-conservative].
Adjunction supplies $j_!G\to\pi_*j'_!G'$.

At a geometric point $\bar x$ of $U$, the fibre of $\pi$ is
one geometric point and the restricted sheaf is $G_{\bar x}$.
At a geometric point of $X\setminus U$, the entire fibre is
disjoint from $U'$, and the restricted sheaf is zero.
The proper geometric-fibre formula of
[cor-weil-pbc-geometric-fiber-finite] therefore identifies
the displayed adjunction morphism with an isomorphism on all
stalks, and makes every positive-degree stalk $R^q\pi_*j'_!G'$
zero. Apply
[lemma-weil-pbc-geometric-stalk-conservative] once more.
