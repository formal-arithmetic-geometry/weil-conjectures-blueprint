+++
id = "def-weil-pbc-finite-pushforward-extension-zero"
kind = "definition"
title = "Finite pushforward and extension by zero"
order = 1706
uses = ["def-weil-pbc-cartesian-square-detailed", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions", "def-weil-pbc-underived-exchange-detailed"]
+++
For a cartesian square [def-weil-pbc-cartesian-square-detailed]

$$
 \begin{array}{ccc}
 U&\xrightarrow{j_U}&X\\
 v\downarrow&&\downarrow\bar v\\
 V&\xrightarrow{j_V}&Y,
 \end{array}
$$

with $j_U,j_V$ open immersions and $\bar v$ finite, define

$$
 \beta_{\bar v,j_V,G}:(j_V)_!v_*G
 \longrightarrow\bar v_*(j_U)_!G
$$

as the adjoint of the finite-base-change identification after restriction to
$V$.
