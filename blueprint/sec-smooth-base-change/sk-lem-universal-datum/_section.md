+++
id = "sk-lem-universal-datum"
kind = "section"
title = "Universal curve-test datum for a failure"
order = 1392
uses = ["sk-def-bc", "sk-def-smooth"]
lean = ["AlgebraicGeometry.Etale.exists_curveTestDatum"]
+++
*Lemma (sketch).*

(Stacks Project, Lemma 59.88.7, Tag `0F08`.) If
$\mathrm{BC}(f,n,q-1)$ holds but $\mathrm{BC}(f,n,q)$ fails, then
there is a universal curve-test datum: a Cartesian square

$$
\begin{array}{ccc}
X & \xleftarrow{\;h\;} & Y\\
f\downarrow & & \downarrow e\\
S & \xleftarrow{\;g\;} & \Spec K
\end{array}
$$

with $S=\Spec A$ affine, integral, normal, fraction field $L$
algebraically closed, $K/L$ an extension of algebraically closed
fields, $X\to S$ affine smooth of relative dimension one, and an
integer $d\mid n$ such that

$$
R^qh_*(\Z/d\Z)\ \neq\ 0 .
$$

## Proof

By [sk-lem-failure-field] one works over a field; an integral
surjective base change to an algebraic closure of $K$ preserves the
failure (surjectivity on a geometric point makes the same element
survive), so $K$ is algebraically closed; a
$\Z/n\Z$-module on a geometric point is a sum of $\Z/d\Z$'s, so one
passes to a constant $\Z/d\Z$ with $d\mid n$; finally the
normalization of $S'$ in $\Spec K$ is integral, so the
integral base-change lemma gives the normal $S$.

Uses: [sk-def-bc], [sk-def-smooth]
