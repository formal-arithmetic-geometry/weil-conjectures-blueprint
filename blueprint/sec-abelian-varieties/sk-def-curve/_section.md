+++
id = "sk-def-curve"
kind = "definition"
title = "Curves and genus"
lean = ["AlgebraicGeometry.IsCurve", "AlgebraicGeometry.IsConnectedCurve", "AlgebraicGeometry.Scheme.Hom.genus"]
order = 528
tags = ["sketch"]
+++
Let $k$ be a field (in this chapter algebraically closed). A *curve*
over $k$ is a separated scheme of finite type over $k$ of dimension
$\le1$; it is *smooth* (resp. *proper*) if its structure morphism is
smooth (resp. proper). A *connected curve* is a nonempty
connected curve of dimension exactly $1$ (so $\Spec k$ is a curve but
not a connected curve).
For $C$ smooth proper connected, the
*genus* of $C$ is $g=\dim_{k}H^0(C,\Omega^1_{C/k})$ (invariant
under algebraically closed extension of $k$).
