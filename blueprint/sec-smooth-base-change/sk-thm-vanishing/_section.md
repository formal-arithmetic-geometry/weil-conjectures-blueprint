+++
id = "sk-thm-vanishing"
kind = "section"
title = "Vanishing in the universal curve test"
order = 1410
uses = ["sk-def-smooth", "sk-prop-cd-affine", "sk-prop-etale-normal", "sk-prop-ext-invariance", "sk-prop-input-spreading", "sk-prop-input-torsors", "sk-prop-normal-form"]
lean = ["AlgebraicGeometry.Etale.CurveTestDatum.isZero_higherDirectImage_constantSheaf"]
+++
*Theorem (sketch).*

Let $X\to S$ be affine smooth of relative dimension one with $X$
affine, $S=\Spec A$ normal with algebraically closed fraction field
$L$, $K/L$ an extension of algebraically closed fields, $d$
invertible on $S$, and

$$
\begin{array}{ccc}
X & \xleftarrow{\;h\;} & Y=X\times_S\Spec K\\
f\downarrow & & \downarrow e\\
S & \xleftarrow{\;g\;} & \Spec K.
\end{array}
$$

Then

$$
R^qh_*(\Z/d\Z)=0\qquad(q\ge1).
$$

## Proof

$R^qh_*(\Z/d\Z)$ is the sheaf associated with
$U\mapsto H^q(U\times_S\Spec K,\Z/d\Z)$ on $X_{\Et}$; we must kill
each $\xi$ in one of these groups on an étale cover of $U$.

- $q>1$: $U\times_S\Spec K$ is an affine smooth curve over
$K$, and [sk-prop-cd-affine] gives the vanishing.
- $q=1$: by [sk-prop-normal-form] replace $U$ by an étale
cover with $U\to V\to S$, $U\to V$ affine smooth with geometrically connected fibres
and a section $\sigma$, $V\to S$ étale; by
[sk-prop-etale-normal], $V$ is an open
of the normal $S$, so we may assume $X\to S$ affine smooth, with
geometrically connected fibres and a section $\sigma$, and
$\xi\in H^1(Y,\Z/d\Z)$. By [sk-prop-ext-invariance] the pullback
map $H^1(X_L,\Z/d\Z)\to H^1(Y,\Z/d\Z)$ is an isomorphism, so $\xi$ comes from a class on
$X_L$; by [sk-prop-input-torsors] this
class is a $\Z/d\Z$-torsor $P\to X_L$, i.e. a finite étale Galois
cover; over the $L$-point $\sigma(\eta)$ it is trivial ($L$
algebraically closed), so $P$ has an $L$-point above
$\sigma(\eta)$; by [sk-prop-input-spreading] $P$ spreads to a
finite étale Galois cover
$X'\to X$; then $X'\times_XY$ is the pullback of $P$ along itself
and carries the diagonal section, so the class of $\xi$ is killed in
$H^1(X'\times_XY,\Z/d\Z)$: $\{X'\to X\}$ is the required étale
cover and the sheaf is zero.

Uses: [sk-def-smooth], [sk-prop-cd-affine], [sk-prop-etale-normal], [sk-prop-ext-invariance], [sk-prop-input-spreading], [sk-prop-input-torsors], [sk-prop-normal-form]
