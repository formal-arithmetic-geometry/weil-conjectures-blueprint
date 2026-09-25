+++
id = "sk-d-real-lie"
kind = "section"
title = "Lie algebras and tangent actions"
order = 2814
uses = ["sk-d-real-monodromy"]
+++
*Definition (sketch).*

A Lie algebra is a vector space with a bilinear alternating bracket
satisfying Jacobi. An ideal $I$ satisfies $[L,I]\subseteq I$;
$Z(L)=\{x:[x,L]=0\}$. Set $D^0L=L$ and
$D^{j+1}L=[D^jL,D^jL]$, taking linear spans of brackets.
Solvable means $D^jL=0$ for some $j$; in finite dimension the radical
$\operatorname{rad}L$ is the largest solvable ideal.
The quotient by an ideal has bracket $[x+I,y+I]=[x,y]+I$.
A Lie representation is a bracket-preserving linear map
$L\to\operatorname{End}_K(V)$; faithful means injective, and irreducible
means that $V\ne0$ has no proper nonzero invariant subspace.
Its Killing form is
$B_L(x,y)=\Tr(\operatorname{ad}x\operatorname{ad}y)$, where
$\operatorname{ad}x(y)=[x,y]$; nondegeneracy means that its kernel is zero.
For a matrix group, define

$$
\Lie G=\{x:1+\varepsilon x\in G(K[\varepsilon]/\varepsilon^2)\},
\quad [x,y]=xy-yx,\quad
r(1+\varepsilon x)=1+\varepsilon\,dr(x).
$$

The same tangent definition applies to a subgroup scheme given by matrix
equations, before it is known to be reduced. Write
$\operatorname{Ad}(g)x=gxg^{-1}$.
def:lie-algebra; def:lie-representation; def:lie-radical; def:lie-quotient; def:lie-killing; def:lie-matrix-group

Uses: [sk-d-real-monodromy]
