+++
id = "def-weil-pbc-property-detailed"
kind = "definition"
title = "Proper-base-change property"
order = 1294
uses = ["def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions"]
+++
For a proper morphism [def-weil-pbc-scheme-conventions] $f:X\to Y$, write
$\mathrm{PBC}(f)$ if, for every morphism $g:Y'\to Y$, every associated
cartesian square [def-weil-pbc-cartesian-square-detailed] $\square$, and
every torsion sheaf [def-weil-pbc-etale-sheaves] $F\in\Ab(X_{\Et})$, the
specified map

$$
 \Ex_{\square,F}:g^{-1}Rf_*F\longrightarrow Rf'_*g'^{-1}F
$$

of the derived exchange morphism [def-weil-pbc-derived-exchange-detailed] is
an isomorphism in $\Dplus(Y'_{\Et})$.
