+++
kind  = "proof"
of    = "lem-pc-finite-linear-avoidance"
+++
First reduce to finite dimension: choose $v_j\in V\setminus W_j$ for
each $j$ and replace $V$ by the span $V'$ of $v_1,\dots,v_s$ and each
$W_j$ by $W_j\cap V'$, which is proper in $V'$ as it misses $v_j$; a
vector of $V'$ outside all $W_j\cap V'$ lies outside all $W_j$. So
assume $V$ finite-dimensional.
For each $j$, extend a basis of $W_j$ to one of $V$ and take a
nonzero coordinate functional $\lambda_j$ vanishing on $W_j$.
Their product is a nonzero polynomial on $V$, since the polynomial
ring over $k$ is a domain. A nonzero polynomial over an infinite
field cannot vanish at every point of affine space: in one variable
it has at most its degree many roots; in several variables first
choose values at which one nonzero coefficient polynomial is nonzero,
by induction, and then choose the last coordinate avoiding the
finitely many roots of the resulting one-variable polynomial.
A point where $\prod_j\lambda_j$ does not vanish belongs to none
of the $W_j$. For $s=0$ any vector suffices.
