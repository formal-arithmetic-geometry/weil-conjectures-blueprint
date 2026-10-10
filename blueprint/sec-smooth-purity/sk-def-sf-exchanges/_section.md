+++
id = "sk-def-sf-exchanges"
kind = "definition"
title = "Exchange and projection transformations, typed"
order = 1500
lean = ["AlgebraicGeometry.Etale.baseChange", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus", "AlgebraicGeometry.Etale.derivedBaseChangeMap", "AlgebraicGeometry.Etale.rightDerivedLowerShriekBaseChangeMap", "AlgebraicGeometry.Etale.projectionMap"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be separated of finite type with a Cartesian square (for
$\operatorname{Ex}_*$ any commutative square suffices)

$$
\begin{array}{ccc}
X'&\xrightarrow{\ g'\ }&X\\
{\scriptstyle f'}\downarrow&&\downarrow{\scriptstyle f}\\
Y'&\xrightarrow{\ g\ }&Y .
\end{array}
$$

The *exchange transformations* are the natural transformations

$$
\operatorname{Ex}_*:Lg^*Rf_*\longrightarrow Rf'_*Lg'^*,
\qquad
\operatorname{Ex}_!:Lg^*Rf_!\longrightarrow Rf'_!Lg'^*,
$$

the first between functors $D^+(X,\Lambda)\to D^+(Y',\Lambda)$, defined as the
composite of the unit of $Lf'^*\dashv Rf'_*$, the pullback comparison
$Lf'^*Lg^*\simeq Lg'^*Lf^*$ and the counit of $Lf^*\dashv Rf_*$, and the second
between functors on the ambient categories on which $Rf_!,Rf'_!$ are defined
([sk-def-sf-operations] (iv); at the adic stages, on the derived-complete
pro-étale complexes, it is the completed exchange
$\operatorname{Ex}^{\mathrm{comp}}_!$ through the completed pullbacks
$Lg^*_{\mathrm{comp}}$). For $K\in\Dbc(X,\Lambda)$ and
$L\in\Dctf(Y,\Lambda)$ the *projection transformation* is the morphism

$$
\operatorname{PF}_{f,K,L}:Rf_!K\otimes^L_\Lambda L\longrightarrow
Rf_!\bigl(K\otimes^L_\Lambda Lf^*L\bigr)
\qquad\text{in }D^+(Y,\Lambda),
$$

natural in $K$ and $L$.
