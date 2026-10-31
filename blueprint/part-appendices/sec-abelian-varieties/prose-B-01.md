+++
id = "prose-B-01"
kind = "hidden"
title = "Abelian varieties and Tate modules"
order = 852
+++
A complex torus $\mathbf C^g/\Lambda$ has $n$-torsion
$\tfrac1n\Lambda/\Lambda\simeq(\mathbf Z/n)^{2g}$, and its first homology is
the lattice $\Lambda$, of rank $2g$. For an abelian variety $A$ of
dimension $g$ over an arbitrary field $k$ there is no lattice, but the
torsion points still see the $2g$ cycles, and this is how they enter
étale cohomology. By the Kummer sequence, $H^1(C,\mu_n)$ of a curve is
the $n$-torsion of its Jacobian. We prove the algebraic counterparts of the
facts about the torus. For $n$ invertible in $k$, the group scheme $A[n]$
is finite étale of rank $n^{2g}$
(Proposition [sk-prop-av-isogeny]), the Tate module
$T_\ell A=\varprojlim_mA[\ell^m](\bar k)$ is free of rank $2g$ over $\Zl$
(Proposition [sk-prop-av-tate-rank]), and over $\mathbf F_q$ no power of
Frobenius has a nonzero fixed vector on $T_\ell A$
(Proposition [sk-p-tate]). Applied to the Jacobian of
Appendix [sec-picard-framework], the first two facts compute $H^1$ of a curve in
Appendix [sec-curve-estimates], and the third proves that Frobenius has no fixed
class in $H^1$ of a curve (Proposition [sk-prop-wrp-h1-no-fixed]), which makes
the geometric monodromy of a lisse sheaf of rank one finite. The last
statement is the simplest of the three: a fixed vector would be a
compatible system of $\ell$-power torsion points in the finite group
$A_0(\mathbf F_{q^m})$, and such a system is zero.

Everything rests on one formula. If $\mathcal N$ is a symmetric ample
invertible sheaf on $A$, then

$$
[n]^*\mathcal N\simeq\mathcal N^{\otimes n^2}
$$

(Proposition [sk-prop-av-mult-n-pullback]). On an elliptic curve with
$\mathcal N=\mathcal O(e)$ this says that the divisor $[n]^*(e)$ is
linearly equivalent to $n^2(e)$. When $n$ is prime to the
characteristic, $[n]$ is étale and $[n]^*(e)$ is the reduced divisor
$E[n]$, so comparing degrees gives $\#E[n]=n^2$. In general the formula forces $[n]$ to
have finite fibres, since $\mathcal N^{\otimes n^2}$ has positive degree
on every complete curve in $A$ while $[n]^*\mathcal N$ is trivial on a curve contracted by
$[n]$, and comparing the leading coefficients of the Euler characteristics
$\chi(A,[n]^*\mathcal N^{\otimes m})$ computed in two ways gives $\deg[n]=n^{2g}$. The formula itself comes from the
theorem of the cube (Theorem [sk-prop-av-cube]): an invertible
sheaf on a product of three complete varieties that is trivial on three
slices through a point is trivial. We prove the theorem of the cube
following [Stacks, Tag 0BEZ](https://stacks.math.columbia.edu/tag/0BEZ), together with the rigidity lemma that makes $A$
commutative; see also (Milne AV). We quote
semicontinuity, the Künneth formula and minimal complexes for coherent
cohomology, and the theorem that a group scheme of finite type over a
field is quasi-projective.

In this appendix all group schemes are of finite type over a field $k$
of arbitrary characteristic.
