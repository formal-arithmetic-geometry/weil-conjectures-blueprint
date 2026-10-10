+++
id = "def-weil-pbc-injective-acyclicity-property"
kind = "definition"
title = "Injective-acyclicity property"
order = 1050
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions"]
+++
For a proper morphism [def-weil-pbc-scheme-conventions] $f:X\to Y$ and a
prime $r$, write $\mathrm{IA}_r(f)$ if, after every base change $g:Y'\to Y$,
every injective sheaf $I$ of $\mathbf F_r$-modules on $X_{\Et}$ satisfies

$$
 R^qf'_*g'^{-1}I=0\qquad(q>0),
$$

where $f'$ and $g'$ are the maps of the associated cartesian square
[def-weil-pbc-cartesian-square] and $R^q$ is the higher direct image
[def-weil-pbc-direct-image]. Write $\mathrm{IA}(f)$ if this holds for every
prime $r$.
