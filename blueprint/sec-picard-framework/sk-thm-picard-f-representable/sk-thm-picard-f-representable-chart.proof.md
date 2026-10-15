+++
kind  = "proof"
of    = "det-picard-f-representable-chart"
+++
(1) By construction in [thm-pc-f-representable], the isomorphism
$h_W\to F$ is the Yoneda map of the class
$\cL_W:=\cL_g|_{C\times W}\in F(W)$, where
$\cL_g=\cO(D_g)\otimes\operatorname{pr}^*P_{H_g}^*\cO(D_g)^{-1}$ is the
normalized universal sheaf. A $T$-point $m:T\to W$ is therefore sent to
$(\mathrm{id}_C\times m)^*\cL_W$. Pullback of relative effective Cartier
divisors commutes with base change, so
$(\mathrm{id}_C\times m)^*\cO(D_g)=\cO_{C_T}(D)$ for the divisor
$D=(\mathrm{id}_C\times m)^{-1}D_g$ classified by $m$, and
$(\mathrm{id}_C\times m)^*\operatorname{pr}^*P_{H_g}^*\cO(D_g)=f_T^*P_T^*\cO_{C_T}(D)$
since $P_{H_g}\circ m=(\mathrm{id}_C\times m)\circ P_T$. Hence the image
is the normalization of $\cO_{C_T}(D)$ along $P_T$, and via
[cor-pc-sigma-pic-iso] this is the rigidified class of $\cO_{C_T}(D)$
(with its canonical rigidification
$P_T^*(\cO(D)\otimes f_T^*P_T^*\cO(D)^{-1})\cong\cO_T$).

(2) By [thm-pc-hilb-curves], $H_g$ is smooth of pure dimension $g$ over
$k$. Smoothness and relative dimension are local on the source, so the
open subscheme $W$ is smooth of pure dimension $g$. Since $h_W\cong F$,
the functor $F$ is represented by a smooth $k$-scheme of dimension $g$.
