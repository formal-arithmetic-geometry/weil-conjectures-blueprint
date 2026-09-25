+++
id = "def-sc-group-scheme"
kind = "definition"
title = "Group schemes over a field"
order = 426
+++
Let $k$ be a field. A $k$-*group scheme* is a $k$-scheme
$G$ together with morphisms $m:G\times_kG\to G$ (multiplication),
$i:G\to G$ (inverse) and $e:\operatorname{Spec}k\to G$ (identity)
such that the usual associativity, unit and inverse diagrams
commute; equivalently, the functor of points
$R\mapsto G(R)$ takes values in groups. The group scheme is
*commutative* if $m\circ s=m$, where $s$ swaps the two
factors. A *homomorphism* $f:G\to H$ of group schemes is a
morphism of schemes compatible with the multiplications; the
*kernel* of $f$ is the closed subgroup scheme

$$
\ker f:=G\times_{H,f,e_H}\operatorname{Spec}k.
$$
