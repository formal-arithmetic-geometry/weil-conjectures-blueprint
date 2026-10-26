+++
id = "sbc-thm-cohomological-dimension-of-an-affine-curve"
kind = "theorem"
title = "Affine-curve cohomological dimension"
lean = ["AlgebraicGeometry.subsingleton_sheafH_constantZMod_and_nonempty_addEquiv_sheafH_zero"]
order = 2049
uses = ["def-weil-pbc-etale-cohomology", "def-weil-pbc-scheme-conventions", "thm-sc-affine-cohomology"]
+++
Let $k$ be algebraically closed, let $C$ be a
smooth affine curve over
$k$, and let $d\geq1$ be prime to $\operatorname{char}k$. Then

$$
H^q(C_{\Et},\mathbf Z/d\mathbf Z)=0\qquad(q>1)
$$

with $H^0(C_{\Et},\mathbf Z/d\mathbf Z)=\mathbf Z/d\mathbf Z$.
