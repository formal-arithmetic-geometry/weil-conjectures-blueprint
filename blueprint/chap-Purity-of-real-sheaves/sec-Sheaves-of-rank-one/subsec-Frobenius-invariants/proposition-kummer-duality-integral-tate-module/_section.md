+++
id = "proposition-kummer-duality-integral-tate-module"
kind = "proposition"
title = "Kummer, duality and the integral Tate module"
order = 1097
lean = ["AlgebraicGeometry.JacobianTorsionDatum", "AlgebraicGeometry.Scheme.EtaleTorsor.exists_picTorsionPairing"]
+++
Let $C_0/k_0$ be a smooth proper geometrically connected curve with
Jacobian $J_0$, and put $A_n=\mathbf Z/\ell^n$.  There are canonical compatible Galois-equivariant
identifications

$$
H^1(C,A_n(1))\simeq J[\ell^n](k),\qquad
\varprojlim_n H^1(C,A_n)
\simeq\Hom_{\mathbf Z_\ell}(T_\ell J,\mathbf Z_\ell).
$$

Here the transition maps are multiplication by $\ell$ on
$J[\ell^n](k)$ and reduction of coefficients on $H^1(C,A_n)$.  If
arithmetic Frobenius on $T_\ell J$ has matrix $B$, then geometric
Frobenius on $\Hom_{\mathbf Z_\ell}(T_\ell J,\mathbf Z_\ell)$ has matrix $B^t$ in the dual
basis.
