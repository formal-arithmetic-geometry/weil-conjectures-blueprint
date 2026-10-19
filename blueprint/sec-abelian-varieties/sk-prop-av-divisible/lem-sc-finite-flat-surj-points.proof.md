+++
kind  = "proof"
of    = "lem-sc-finite-flat-surj-points"
+++
Let $y:\Spec k\to Y$. The fibre $X_y=X\times_{Y,y}\Spec k$ is finite
over $k$, being a base change of $f$, and nonempty, since $f$ is
surjective and a base change of a surjective morphism is surjective.
So it is a nonempty finite $k$-scheme, which has a $k$-point
$s:\Spec k\to X_y$ by [lem-sc-finite-nonempty-point]. The composite
$x$ of $s$ with the projection $X_y\to X$ satisfies $f\circ x=y$. If
$f$ is a morphism of $k$-schemes and $y$ is a $k$-point, then $x$ is a
$k$-point as well, because the structure morphism of $X$ is that of $Y$
composed with $f$.
