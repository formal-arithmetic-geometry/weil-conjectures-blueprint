+++
id = "def-point-count-zeta"
kind = "definition"
title = "Point counts and zeta function"
order = 102
lean = ["AlgebraicGeometry.Scheme.Hom.X_mul_derivative_zetaSeries", "AlgebraicGeometry.Scheme.Hom.degreeOver", "AlgebraicGeometry.Scheme.Hom.pointCount", "AlgebraicGeometry.Scheme.Hom.zetaSeries"]
uses = ["def-weil-base-field"]
+++
For every finite-type $\Fq$-scheme $Y_0$ and $n\geq1$, put

$$
N_n(Y_0)=\#Y_0(\mathbf F_{q^n}).
$$

For a closed point $x\in|Y_0|$, set
$\deg(x)=[\kappa(x):\Fq]$. Define the Hasse–Weil zeta series by

$$
Z(Y_0,T)=
\exp\left(\sum_{n\geq1}N_n(Y_0)\frac{T^n}{n}\right)
\in1+T\mathbf Q[[T]].
$$

The exponential is the formal power-series exponential.
