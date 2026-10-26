+++
id = "lem-kun-0ezt"
kind = "lemma"
title = "Higher direct images along limits of cartesian squares"
order = 3079
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
quasi-separated and every $S_i$ and every $X_i$ is a quasi-compact and
quasi-separated scheme. Write

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

*On the quasi-compactness hypotheses.* The hypothesis that the $S_i$ and
$X_i$ are quasi-compact and quasi-separated is not in Stacks 0EZT; it is
expected to be removable by localising on $S_{i_0}$ and $X_{i_0}$ for one
index $i_0$. Every use of the lemma in this blueprint satisfies it (the
smooth-limit base change, Stacks 0F09, after localising on its base).
