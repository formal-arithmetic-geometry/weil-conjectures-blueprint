+++
id = "sk-thm-vanishing"
kind = "theorem"
title = "Vanishing in the universal curve test"
order = 1410
uses = ["sk-def-smooth", "sk-prop-cd-affine", "sk-prop-etale-normal", "sk-prop-ext-invariance", "sk-prop-input-spreading", "sk-prop-input-torsors", "sk-prop-normal-form"]
lean = ["AlgebraicGeometry.Etale.CurveTestDatum.isZero_higherDirectImage_constantSheaf"]
tags = ["sketch"]
+++
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
