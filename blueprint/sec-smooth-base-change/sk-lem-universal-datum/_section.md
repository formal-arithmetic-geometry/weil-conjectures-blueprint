+++
id = "sk-lem-universal-datum"
kind = "lemma"
title = "Universal curve-test datum for a failure"
order = 1448
uses = ["sk-def-bc", "sk-def-smooth"]
lean = ["AlgebraicGeometry.Etale.CurveTestDatum", "AlgebraicGeometry.Etale.exists_curveTestDatum"]
tags = ["sketch"]
+++
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
