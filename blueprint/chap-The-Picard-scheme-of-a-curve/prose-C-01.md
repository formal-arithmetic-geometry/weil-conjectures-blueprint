+++
id = "prose-C-01"
kind = "hidden"
title = "The Picard scheme of a curve"
order = 1518
+++
For a curve $C$ proper and connected over a separably closed field and
$n$ invertible in that field, the Kummer sequence shows that
$H^1(C,\mu_n)$ is the $n$-torsion of the Picard group of $C$. But the
Picard group is an abstract group. In particular, nothing about it says that its
$n$-torsion is finite, let alone isomorphic to $(\mathbf Z/n)^{2g}$. Nor
does it say why Frobenius should have no fixed vector on the $\ell$-adic
limit, as Proposition [proposition-no-fixed-class-degree-one]
requires. Both questions become statements of
Appendix [chap-Abelian-varieties] once we know that
$\operatorname{Pic}^0(C)$, the group of invertible sheaves of degree
zero, is the group of points of an abelian variety.

Over $\mathbf C$ this is the Abel–Jacobi theorem, $\operatorname{Pic}^0(C)\simeq
H^0(C,\Omega^1)^\vee/H_1(C,\mathbf Z)$. Over an arbitrary field we
construct the Jacobian as a Picard scheme, which represents invertible
sheaves in families.

Let $C$ be a smooth proper connected curve of genus $g$ over a separably
closed field $k$. The idea is that most invertible sheaves of degree $g$
are given by divisors. Suppose $\mathcal L$ has degree $g$ and
$h^0(\mathcal L)=1$. Then the zeros of its unique section up to scalars
form an effective divisor of degree $g$, and this divisor determines
$\mathcal L$. Effective divisors of degree $g$ are the points of the
Hilbert scheme $\operatorname{Hilb}^{g}_{C/k}$, a smooth proper variety of
dimension $g$ (Theorem [theorem-hilbert-schemes-points-smooth-curve]).

By Riemann–Roch, every invertible sheaf of degree $g$ has $h^0\geq1$,
with equality exactly when $h^1=0$. This condition is open in families,
by semicontinuity, and it defines an open chart
$W\subset\operatorname{Hilb}^{g}_{C/k}$ of the Picard functor
(Proposition [proposition-divisors-degree-g-open-chart]).
Riemann–Roch also moves every invertible sheaf into this chart by a twist
defined over $k$ (Lemma [lemma-twisting-h-0-1-h]). Hence the
translates of $W$ cover the Picard functor, and they glue to the Picard
scheme. Its components are proper because the Abel map
$\operatorname{Hilb}^{g}_{C/k}\to\operatorname{Pic}^g$ is surjective and
its source is proper.

The Picard functor itself is a sheafified quotient of
$T\mapsto\operatorname{Pic}(C\times T)$. We have to divide out the
invertible sheaves pulled back from $T$, since these are trivial locally
on $T$. When $C$ has a rational point, we describe the Picard functor by
invertible sheaves trivialized along that point
(Lemma [lemma-rigidification-along-section]).

The outcome is
Theorem [theorem-picard-scheme-jacobian-over-separably]: the
component of degree zero, the Jacobian $J(C)$, is an abelian variety of
dimension $g$ with $J(C)(k)=\operatorname{Pic}^0(C)$ and tangent space
$H^1(C,\mathcal O_C)$ at the origin.
Over a finite field we descend the Jacobian to an abelian
variety $J_0$ over $\mathbf F_q$. Then
Propositions [proposition-jacobian-over-ground-field]
and [proposition-h-1-curve-tate-module] give an isomorphism
$\varprojlim_nH^1(C,\mathbf Z/\ell^n(1))\simeq T_\ell J_0$ compatible
with Frobenius, which is the form in which
Proposition [proposition-no-fixed-class-degree-one] uses the
Jacobian; see also [milne-jv].
