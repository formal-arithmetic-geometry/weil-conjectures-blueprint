+++
id = "lemma-weil-pbc-frobenius-level-rectangle"
kind = "lemma"
title = "The finite rectangle is a Weil rectangle"
order = 1393
uses = ["def-weil-pbc-frobenius-corner-structures", "lemma-weil-pbc-derived-exchange-coherence", "lemma-weil-pbc-level-map-rectangle"]
+++
All four finite-level edges are Weil-equivariant:

$$
\begin{aligned}
h_n\Theta_{A,n}&=\Theta_{B,n}\Phi_{Y'}(h_n),&
v_n\Theta_{A,n}&=\Theta_{C,n}\Phi_{Y'}(v_n),\\
h'_n\Theta_{C,n}&=\Theta_{D,n}\Phi_{Y'}(h'_n),&
v'_n\Theta_{B,n}&=\Theta_{D,n}\Phi_{Y'}(v'_n).
\end{aligned}
$$

In particular the two explicitly typed composites

$$
\begin{aligned}
\mathcal P_n&:=
\Phi_{Y'}A_n\xrightarrow{\Theta_{A,n}}A_n
\xrightarrow{v'_nh_n}D_n,\\
\mathcal Q_n&:=
\Phi_{Y'}A_n\xrightarrow{\Phi_{Y'}(v'_nh_n)}\Phi_{Y'}D_n
\xrightarrow{\Theta_{D,n}}D_n
\end{aligned}
$$

are equal. The same common map is obtained after replacing $v'_nh_n$ by
$h'_nv_n$.
