+++
id = "sbc-lem-bc-universal-test"
kind = "lemma"
title = "Universal curve-test datum for a failure"
lean = ["AlgebraicGeometry.Etale.exists_not_isZero_higherDirectImage_constantModSheaf", "AlgebraicGeometry.Etale.exists_isPullback_not_isZero_higherDirectImage"]
order = 2047
uses = ["sbc-def-base-change-map", "sbc-def-base-change-property", "sbc-lem-bc-failure-field", "sbc-lem-bc-integral-base", "sbc-lem-bc-integral-surjective"]
+++
With $f:X\to S$ and $n$ as in [sbc-def-base-change-property] assume for
some $q\geq1$ that $\mathrm{BC}(f,n,q')$ holds universally for all
$q'\leq q-1$, but $\mathrm{BC}(f,n,q)$ does not hold universally. Then there exist a commutative diagram

$$
\begin{array}{ccccc}
X & \longleftarrow & X' & \longleftarrow & Y\\
f\big\downarrow & & \big\downarrow & & \big\downarrow h\\
S & \longleftarrow & S' & \longleftarrow & \operatorname{Spec}K
\end{array}
$$

with both squares Cartesian, where

1. $S'$ is affine, integral, and normal with algebraically closed
function field;
1. $K$ is algebraically closed and $\operatorname{Spec}K\to S'$ is
dominant (in other words $K$ is an extension of the function
field of $S'$),

and there exists an integer $d\mid n$ such that
$R^qh_*(\mathbf Z/d\mathbf Z)$ is nonzero.
