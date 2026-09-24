+++
id = "lem-weil-pbc-chow-affine-immersion-projective"
kind = "lemma"
title = "Affine opens of finite type sit in a projective space"
order = 1584
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $Y=\operatorname{Spec}A$ be affine and let $U$ be an affine scheme of
finite type over $Y$, say $U=\operatorname{Spec}B$ with $B$ generated as an
$A$-algebra by $b_1,\dots,b_m$. Then the $A$-algebra surjection
$A[x_1,\dots,x_m]\twoheadrightarrow B$, $x_j\mapsto b_j$, defines a closed
immersion

$$
 U\hookrightarrow\mathbf A^m_Y,
$$

and composing with the open immersion $\mathbf A^m_Y\hookrightarrow\mathbf
P^m_Y$ (where $\mathbf A^m_Y=D_+(x_0)\subseteq\mathbf P^m_Y$) gives an
immersion $j:U\hookrightarrow\mathbf P^m_Y$.

## Proof

The surjection $A[x_1,\dots,x_m]\twoheadrightarrow B$ is a surjective ring
homomorphism between the coordinate rings of affine schemes, so it induces a
closed immersion of affine schemes (on affines, closed immersions are exactly
those induced by surjective ring homomorphisms). The composite with the open
immersion $\mathbf A^m_Y=D_+(x_0)\hookrightarrow\mathbf P^m_Y$ is an
immersion, since a composite of an open and a closed immersion is an
immersion.
