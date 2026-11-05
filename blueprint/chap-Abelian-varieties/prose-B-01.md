+++
id = "prose-B-01"
kind = "hidden"
title = "Abelian varieties"
order = 1474
+++
Two steps of the main proof come down to the torsion points of a
Jacobian. By the Kummer sequence, $H^1(C,\mu_n)$ of a curve is the $n$-torsion of its Jacobian. The first step, the finiteness of $H^1$ needed for proper base change, is therefore a count of torsion points. The second step is
the finiteness of geometric monodromy in rank one, where purity begins.
It needs Frobenius to fix no class in $H^1$ of a curve over
$\mathbf F_q$ (Proposition [proposition-no-fixed-class-degree-one]).

For a complex torus $\mathbf C^g/\Lambda$ the count is trivial: the
$n$-torsion is $\tfrac1n\Lambda/\Lambda\simeq(\mathbf Z/n)^{2g}$. For an abelian variety $A$ of dimension $g$ over an arbitrary field $k$, however, there is no lattice, and the torsion points must be counted algebraically. This is what we do: we prove that for $n$ invertible in $k$ the group scheme $A[n]$ is finite
étale of rank $n^{2g}$ (Proposition [proposition-multiplication-n]).
It follows that the Tate module $T_\ell A=\varprojlim_mA[\ell^m](\bar k)$
is free of rank $2g$ over $\mathbf Z_\ell$
(Proposition [proposition-integral-tate-module]). Moreover, over $\mathbf F_q$, no power of Frobenius has a nonzero fixed vector on
$T_\ell A$ (Proposition [proposition-no-frobenius-fixed-vector]).
The reason is short: a fixed vector would be a compatible system of
$\ell$-power torsion points of unbounded order in the finite group
$A_0(\mathbf F_{q^m})$.

The count rests on one formula. If $\mathcal N$ is a symmetric ample
invertible sheaf on $A$, then

$$
[n]^*\mathcal N\simeq\mathcal N^{\otimes n^2}
$$

(Proposition [proposition-pullback-multiplication-n]). On an elliptic
curve with $\mathcal N=\mathcal O(e)$ this says that the divisor
$[n]^*(e)$ is linearly equivalent to $n^2(e)$. When $n$ is prime to the
characteristic, $[n]$ is étale and $[n]^*(e)$ is the reduced divisor
$E[n]$. Comparing degrees then gives $\#E[n]=n^2$.

In general the formula is used twice. First, it forces $[n]$ to have
finite fibres. Indeed, $\mathcal N^{\otimes n^2}$ has positive degree
on every complete curve in $A$, while $[n]^*\mathcal N$ is trivial on a
curve contracted by $[n]$. Second, we compute the Euler characteristics
$\chi(A,[n]^*\mathcal N^{\otimes m})$ in two ways, and comparing their
leading coefficients gives $\deg[n]=n^{2g}$.

The formula itself comes from the theorem of the cube
(Theorem [theorem-theorem-cube]). Following [Stacks, [0BEZ](https://stacks.math.columbia.edu/tag/0BEZ)], we prove the theorem of the cube together with the rigidity lemma. As a by-product, from the rigidity lemma we deduce that $A$ is commutative; see also [milne-av].

In this appendix all group schemes are of finite type over a field $k$
of arbitrary characteristic.
