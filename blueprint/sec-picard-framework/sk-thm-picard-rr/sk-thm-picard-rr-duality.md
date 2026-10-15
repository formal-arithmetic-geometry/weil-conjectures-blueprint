+++
id = "det-picard-rr-duality"
kind = "lemma"
title = "Duality, canonical degree and vanishing above $2g-2$ over any field"
uses = ["sk-thm-picard-duality", "lem-sc-flat-base-change-coherent", "lem-pc-degree-base-change", "lem-pc-genus-base-change", "lem-pc-h0-geom-connected"]
+++
Let $C$ be a smooth projective geometrically connected curve over a
field $k$, $g=\dim_kH^1(C,\cO_C)$, $\omega=\omega_{C/k}=\Omega^1_{C/k}$,
and let $\cL$ be an invertible sheaf on $C$. Then:

1. $H^1(C,\cL)^\vee\simeq H^0(C,\omega\otimes\cL^{-1})$, via the trace
pairing;
1. $h^0(C,\omega)=g$, $h^1(C,\omega)=1$, and $\deg\omega=2g-2$;
1. if $\deg\cL>2g-2$, then $H^1(C,\cL)=0$ and
$h^0(C,\cL)=\deg\cL+1-g$;
1. for every field extension $K/k$, the base change $C_K$ is again a
smooth projective geometrically connected curve of genus $g$,
$\deg\cL_K=\deg\cL$, $\omega_{C_K/K}=\omega_K$, and the isomorphism in
(1) for $(C_K,\cL_K)$ is the $K$-linear extension of the one for
$(C,\cL)$ under $H^i(C_K,-_K)=H^i(C,-)\otimes_kK$.
