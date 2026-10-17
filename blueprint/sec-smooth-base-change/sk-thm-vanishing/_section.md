+++
id = "sk-thm-vanishing"
kind = "proposition"
title = "Base change to a larger algebraically closed field"
order = 1431
uses = ["sk-def-smooth", "sk-prop-cd-affine", "sk-prop-etale-normal", "sk-prop-ext-invariance", "sk-thm-curve-package", "sk-lem-pe-torsor-comparison", "sk-prop-input-spreading", "sk-prop-input-torsors", "sk-prop-normal-form"]
lean = ["AlgebraicGeometry.Etale.CurveTestDatum.isZero_higherDirectImage_constantSheaf"]
tags = ["sketch"]
+++
Let $S=\operatorname{Spec}A$ for a normal domain $A$ with algebraically
closed fraction field $L$, and let $a\colon C\to S$ be affine and smooth
of relative dimension one. Let $K/L$ be an extension of algebraically
closed fields, let $d$ be a positive integer invertible on $S$, and let
$h\colon C_K\to C$ be the projection. Then

$$
 R^qh_*\underline{\mathbf Z/d}=0\qquad(q\geq1)
$$

on $C_{\mathrm{pro\acute et}}$.

*Complement.* More generally, for every commutative ring $\Lambda$ the constant sheaf of
$\Lambda/d\Lambda$-modules has vanishing higher direct images on the étale site:

Let $X\to S$ be affine smooth of relative dimension one with $X$
affine, $S=\Spec A$ with $A$ a normal domain with algebraically closed
fraction field $L$, $K/L$ an extension of algebraically closed fields
with $g$ the corresponding geometric generic point of $S$, $d$ an integer
invertible on $S$, $\Lambda$ a commutative ring, and

$$
\begin{array}{ccc}
X & \xleftarrow{\;h\;} & Y=X\times_S\Spec K\\
f\downarrow & & \downarrow e\\
S & \xleftarrow{\;g\;} & \Spec K.
\end{array}
$$

Then

$$
R^qh_*(\Lambda/d\Lambda)=0\qquad(q\ge1)
$$

for the constant sheaf $\Lambda/d\Lambda$ on $Y_{\Et}$.
