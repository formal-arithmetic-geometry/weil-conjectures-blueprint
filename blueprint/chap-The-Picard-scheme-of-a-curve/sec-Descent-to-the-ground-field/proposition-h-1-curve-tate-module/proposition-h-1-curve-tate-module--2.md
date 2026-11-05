+++
id = "proposition-h-1-curve-tate-module--2"
kind = "proposition"
title = "$H^1$ of a curve and the Tate module of its Jacobian (2)"
name_showing = false
order = 1565002
aliases = ["bp-r489-2"]
lean = []
uses = ["proposition-jacobian-over-ground-field", "definition-tate-twists", "definition-tate-module"]
+++
This inverse-limit identification is bypassed by the Lean route and has
no corresponding declaration in the mainline.

For the smooth proper geometrically connected curve $C_0/k$, its
geometric fibre $C$, and its Jacobian $J_0$, with $\ell$ invertible in $k$,
the assertion is

$$
\varprojlim_n H^1(C,\mathbf Z/\ell^n(1))\simeq T_\ell J_0
$$

as $\mathbf Z_\ell$-modules with Galois action.

The mainline works with compatible characters of the finite groups
$\operatorname{Pic}(C)[\ell^n]$. Over a finite ground field,
`AlgebraicGeometry.JacobianTorsionDatum.nonempty` supplies the compatible
Galois-equivariant identifications with $J_0[\ell^n](\bar k)$, and
`AlgebraicGeometry.Scheme.EtaleTorsor.exists_picTorsionPairing` supplies
the pairings with finite constant torsors. The subsequent Frobenius
argument uses these finite-level data without constructing the
displayed inverse-limit isomorphism.
