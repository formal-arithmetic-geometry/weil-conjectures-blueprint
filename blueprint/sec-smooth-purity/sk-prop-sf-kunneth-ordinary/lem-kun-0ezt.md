+++
id = "lem-kun-0ezt"
kind = "lemma"
title = "Higher direct images along limits of cartesian squares"
order = 2000
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-scheme-conventions"]
+++
Let $I$ be directed and let

$$
\begin{array}{ccc}
X_i&\xleftarrow{\;h_i\;}&Y_i\\
\Big\downarrow{\scriptstyle f_i}&&\Big\downarrow{\scriptstyle e_i}\\
S_i&\xleftarrow{\;g_i\;}&T_i
\end{array}
\qquad(i\in I)
$$

be an inverse system of
cartesian squares with affine
transition morphisms, where every $g_i$ is
quasi-compact and
quasi-separated. Write

$$
\begin{array}{ccc}
X&\xleftarrow{\;h\;}&Y\\
\Big\downarrow{\scriptstyle f}&&\Big\downarrow{\scriptstyle e}\\
S&\xleftarrow{\;g\;}&T
\end{array}
$$

If $(F_i)$ is a compatible system of torsion abelian sheaves on
$T_i$, $F=\varinjlim_ip_i^{-1}F_i$, and if for a fixed $q\ge0$ every
base-change map

$$
f_i^{-1}R^qg_{i,*}F_i\longrightarrow R^qh_{i,*}e_i^{-1}F_i
$$

is an isomorphism, then so is

$$
f^{-1}R^qg_*F\longrightarrow R^qh_*e^{-1}F.
$$
