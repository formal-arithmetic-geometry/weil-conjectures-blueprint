+++
id = "lem-wf-affine-product-reduced"
kind = "lemma"
title = "Products of reduced affine varieties are reduced"
order = 2826
uses = ["lem-wf-affine-nullstellensatz-vanishing"]
+++
Let $k$ be algebraically closed and let $X,Y$ be affine varieties over
$k$, with reduced finitely generated coordinate algebras $A=k[X]$ and
$B=k[Y]$. Then $A\otimes_kB$ is a reduced finitely generated
$k$-algebra, so $X\times Y=\operatorname{Spec}(A\otimes_kB)$ is an
affine variety whose $k$-points are the pairs $(x,y)$ of $k$-points.
In particular the vanishing principle of
[lem-wf-affine-nullstellensatz-vanishing] applies to it: a regular
function on $X\times Y$ vanishing at all $k$-points $(x,y)$ is zero.
Thus an identity between regular maps defined on $X\times Y$ (such as a
commutator map) may be checked on $k$-points, one variable at a time.
