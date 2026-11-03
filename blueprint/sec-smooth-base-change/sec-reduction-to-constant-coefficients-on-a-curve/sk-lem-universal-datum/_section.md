+++
id = "sk-lem-universal-datum"
kind = "lemma"
title = "Reduction to a curve over a normal base"
order = 407
lean = ["AlgebraicGeometry.Etale.CurveTestDatum", "AlgebraicGeometry.Etale.exists_curveTestDatum"]
uses = ["sk-def-bc", "sk-def-smooth", "sk-lem-failure-field", "sk-lem-sbc-integral-tests", "sk-prop-injectivity"]
tags = ["sketch"]
+++
Suppose $g:Y'\to Y$ is affine and smooth of relative dimension
one, $n$ is invertible on $Y$, and $\mathrm{BC}(g,n,q-1)$ holds. If
$\mathrm{BC}(g,n,q)$ fails, there are an affine scheme
$S=\operatorname{Spec}R$ over $Y$ with $R$ a normal domain whose fraction
field $L$ is algebraically closed, an algebraically closed extension
field $\Omega$ of $L$, an integer $m\mid n$, and, for the smooth affine curve
$C=Y'\times_YS$, the cartesian square

$$
\begin{CD}
C_\Omega @>{h}>> C\\
@VVV @VVV\\
\operatorname{Spec}\Omega @>>> S
\end{CD}
$$

such that

$$
R^qh_*\underline{\mathbf Z/m}\ne0.
$$

*Complement.* In the notation of [sk-def-bc] (smooth side $f$, qcqs side $g$):

Let $f:X\to S$ be affine and smooth of relative dimension one with $X$
affine, let $\Lambda$ be a commutative ring, let $n$ be an integer
invertible on $S$ with $n\Lambda=0$, and let $q\ge1$. If
$\mathrm{BC}(f,\Lambda,q')$ holds universally for all $q'\le q-1$ but
$\mathrm{BC}(f,\Lambda,q)$ does not hold ([sk-def-bc]), then
there is a universal curve-test datum: a morphism $S'\to S$ and a
Cartesian square

$$
\begin{array}{ccc}
X'=X\times_SS' & \xleftarrow{\;h\;} & Y\\
f'\downarrow & & \downarrow e\\
S' & \xleftarrow{\;g\;} & \Spec K
\end{array}
$$

with $S'=\Spec A$ affine, integral, normal, fraction field $L$
algebraically closed, $K/L$ an extension of algebraically closed
fields and $g$ the corresponding geometric generic point, $f'$ the base
change of $f$ (so affine and smooth of relative dimension one), and an
integer $d\mid n$, invertible on $S'$, such that

$$
R^qh_*(\Lambda/d\Lambda)\ \neq\ 0 .
$$
