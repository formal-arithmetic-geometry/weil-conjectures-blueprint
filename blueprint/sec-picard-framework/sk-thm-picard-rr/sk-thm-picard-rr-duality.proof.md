+++
kind  = "proof"
of    = "det-picard-rr-duality"
+++
*Step 0.* $C$ is geometrically connected and geometrically reduced
(smooth), proper, so $H^0(C,\cO_C)=k$ ([lem-pc-h0-geom-connected]), and
$C$ is integral of pure dimension $1$. Coherent cohomology vanishes in
degrees $\ge2$, so $\chi=h^0-h^1$ and Riemann–Roch for line bundles
(proved in the sketch proof) reads $\chi(\cL)=\deg\cL+1-g$.

*(1).* Apply [sk-thm-picard-duality] with $n=1$, $q=1$ and the finite
locally free module $\cF=\cL$: the trace pairing
$H^1(C,\cL)\otimes H^0(C,\cL^\vee\otimes\omega)\to H^1(C,\omega)\to k$ is
perfect, and $\cL^\vee=\cL^{-1}$.

*(2).* Take $\cL=\cO_C$ in (1): $h^0(\omega)=h^1(\cO_C)=g$. Take $q=0$:
$h^1(\omega)=h^0(\cO_C)=1$. Hence $\chi(\omega)=g-1$, and Riemann–Roch
gives $\deg\omega=\chi(\omega)-(1-g)=2g-2$.

*(3).* The sheaf $\cM=\omega\otimes\cL^{-1}$ has degree
$2g-2-\deg\cL<0$ (degree is additive under tensor product). If $s$ were a
nonzero section of $\cM$, then, $C$ being integral, $s$ is nonzero at the
generic point and its zero scheme is an effective Cartier divisor
$Z(s)=\sum_xn_x\,x$ with all $n_x\ge0$ and $\cM\cong\cO_C(Z(s))$; so
$\deg\cM=\sum_xn_x[\kappa(x):k]\ge0$, a contradiction. Thus
$H^0(\cM)=0$, so $H^1(C,\cL)=0$ by (1), and
$h^0(\cL)=\chi(\cL)=\deg\cL+1-g$.

*(4).* Smoothness, projectivity and geometric connectedness are stable
under base change; the genus is preserved by
[lem-pc-genus-base-change] (flat base change
[lem-sc-flat-base-change-coherent] for $\cO_C$), and the degree by
[lem-pc-degree-base-change]. Kähler differentials commute with base
change, so $\omega_{C_K/K}=\omega_K$. Cup product and evaluation commute
with flat base change, and so does the trace $t_C$: on the residue
description of [sk-thm-picard-duality], $H^1(C,\omega)$ is a quotient of
$\bigoplus_x\Omega^1_{k(C)/k}/\omega_x$ and the residues are $k$-linear
and compatible with extension of scalars, so $t_{C_K}=t_C\otimes K$ on
$H^1(C_K,\omega_K)=H^1(C,\omega)\otimes_kK$ (both are $K$-linear maps on a
one-dimensional space which agree on the image of $H^1(C,\omega)$).
Hence the pairing for $(C_K,\cL_K)$ is the $K$-linear extension of the
pairing for $(C,\cL)$, and so is the induced isomorphism.
