+++
id = "def-weil-pbc-underived-exchange-detailed"
kind = "definition"
title = "Underived exchange morphism"
order = 1280
uses = ["def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image"]
+++
For $F\in\Ab(X_{\Et})$ and a cartesian square
[def-weil-pbc-cartesian-square-detailed] $\square$, define the *underived
exchange morphism*

$$
 \Ex^0_{\square,F}:g^{-1}f_*F\longrightarrow f'_*g'^{-1}F
$$

to be the adjoint, under $f'^{-1}\dashv f'_*$, of the composite

$$
 f'^{-1}g^{-1}f_*F\xrightarrow{\theta_\square}
 g'^{-1}f^{-1}f_*F\xrightarrow{g'^{-1}\varepsilon_f}g'^{-1}F,
$$

where $\theta_\square$ is the specified isomorphism of the cartesian-square
identification [def-weil-pbc-cartesian-square-detailed] and $\varepsilon_f$
is the counit of the inverse-image adjunction
[def-weil-pbc-inverse-image], and where $f_*$, $f'_*$ are the direct image
[def-weil-pbc-direct-image] functors. For an etale $V\to Y'$, a
representative of a section of $g^{-1}f_*F$ on $V$ consists of an etale $W\to
Y$, a map $V\to W\times_YY'$, and a section of $F$ on $X\times_YW$; its image
is the restriction of that section along

$$
 X'\times_{Y'}V\longrightarrow X\times_YW,
$$

followed by sheafification.
