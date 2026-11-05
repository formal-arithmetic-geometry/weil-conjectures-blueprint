+++
id = "prose-B-07"
kind = "hidden"
title = "Multiplication by $n$ (1)"
order = 1495
+++
Let $\mathcal L$ be an invertible sheaf on an abelian variety $A$. We
pull $\mathcal L$ back to $A\times A\times A$ along the partial sums of
the coordinates. There the theorem of the cube gives a second order
recursion for $n\mapsto[n]^*\mathcal L$, whose solution is

$$
[n]^*\mathcal L\simeq\mathcal L^{\otimes n(n+1)/2}\otimes([-1]^*\mathcal L)^{\otimes n(n-1)/2}
$$

(Proposition [proposition-pullback-multiplication-n]). For symmetric $\mathcal L$ the
formula gives $\mathcal L^{\otimes n^2}$. If
$[-1]^*\mathcal L\simeq\mathcal L^{-1}$, as for an invertible sheaf of
degree zero on an elliptic curve, it gives $\mathcal L^{\otimes n}$.

We apply the formula to a symmetric ample sheaf
(Lemma [lemma-symmetric-ample-sheaf]). It shows that $[n]$ is
finite and flat of degree $n^{2g}$, and that $[n]$ is étale when $n$
is invertible in $k$ (Proposition [proposition-multiplication-n]).
The hypothesis on $n$ cannot be dropped. For example, in characteristic $p$ the
differential of $[p]$ is zero, and as a consequence an elliptic curve has at most $p$
points of order dividing $p$ over $\bar k$, although $E[p]$ has rank
$p^2$.
