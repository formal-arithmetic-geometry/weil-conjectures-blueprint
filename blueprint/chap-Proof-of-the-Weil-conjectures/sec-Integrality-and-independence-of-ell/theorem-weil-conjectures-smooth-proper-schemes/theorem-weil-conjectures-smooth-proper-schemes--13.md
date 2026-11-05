+++
id = "theorem-weil-conjectures-smooth-proper-schemes--13"
kind = "theorem"
title = "Top-degree dimension"
order = 1388014
aliases = ["bp-r429-13"]
lean = []
uses = ["corollary-point-counting-zeta-function", "theorem-weil-conjectures-smooth-proper-schemes--6"]
+++
For $X_0$ smooth, proper and geometrically connected of pure dimension $d$,
$$
\dim_{\overline{\mathbf Q}_\ell}\overline H^{2d}_\ell=1.
$$
For any integral realization in degree $2d$ this gives $b_{2d}=1$. Lean proves the displayed dimension equality as the local assertion `hfin` inside `AlgebraicGeometry.Scheme.frobeniusCharpolyRev_two_mul`; it has no separate declaration.
