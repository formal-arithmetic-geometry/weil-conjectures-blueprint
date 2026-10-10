+++
kind  = "proof"
of    = "lemma-weil-pbc-frobenius-level-rectangle"
+++
The equations for $h_n$ and $h'_n$ are the two transport definitions. For
$v'_n$, expand the upper-right and lower-left routes in the Frobenius cube.
Pasting coherence for exchange and naturality in $\vartheta_n$ identify both
with

$$
\begin{aligned}
\Phi_{Y'}Lg^*Rf_*K_n
&\xrightarrow{\kappa_g}Lg^*\Phi_YRf_*K_n
\xrightarrow{Lg^*\beta_{f,n}}Lg^*Rf_*\Phi_XK_n\\
&\xrightarrow{\xi_{\Phi_XK_n}}Rf'_*L(g')^*\Phi_XK_n
\xrightarrow{Rf'_*L(g')^*\vartheta_n}D_n.
\end{aligned}
$$

This proves the fourth equation with every pullback and exchange map typed.
For the remaining vertical edge, use the ordinary rectangle and the three
equations already proved:

$$
\begin{aligned}
h'_nv_n\Theta_{A,n}
&=v'_nh_n\Theta_{A,n}
=v'_n\Theta_{B,n}\Phi_{Y'}(h_n)\\
&=\Theta_{D,n}\Phi_{Y'}(v'_nh_n)
=h'_n\Theta_{C,n}\Phi_{Y'}(v_n).
\end{aligned}
$$

Cancel the isomorphism $h'_n$. Composing either pair of edge equations and
using $v'_nh_n=h'_nv_n$ gives
$\mathcal P_n=\mathcal Q_n$ and the final assertion.
