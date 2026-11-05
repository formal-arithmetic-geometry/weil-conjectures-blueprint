+++
kind = "proof"
of = "theorem-smooth-purity-all-admissible-coefficients--6"
order = 731013
+++
*Property (1), integral and rational coefficients.* For
$\Lambda=\mathcal O_E$ we write the left side $\phi$ of (1) as
$u\circ\operatorname{Tr}_p$ and show that $u=1$ by reducing modulo $\ell^n$.

First, the trace map $\operatorname{Tr}_p$ of
(9.1) is an isomorphism, and this is what
makes $u$ well defined. Its reduction modulo $\ell$ is the trace map with
coefficients $\mathcal O_E/\ell$, because the trace of
Proposition [proposition-ell-adic-cycle-class-diagonal] lifts the
finite ones. This reduction is an isomorphism. Indeed, it is obtained by
extension of scalars along the free map $\mathbf Z/\ell\to\mathcal O_E/\ell$
from the trace map with coefficients $\mathbf Z/\ell$, which is an
isomorphism (Section [sec-The-trace-map-of-affine-space]). So the cone $C$ of
$\operatorname{Tr}_p$ has $C/\ell=0$, and hence
$C/\pi_E=(C/\ell)\otimes^{\mathbf L}_{\mathcal O_E/\ell}\mathcal O_E/\pi_E=0$.
The complex $C$ is derived complete, since its source and target lie in
$\Dbc(Y,\mathcal O_E)$. Derived Nakayama
(Lemma [lemma-reduction-derived-nakayama]) gives $C=0$. Thus
$\phi=u\circ\operatorname{Tr}_p$ for a unique endomorphism $u$ of
$\mathcal O_{E,Y}$, that is, for an element
$u\in H^0(Y,\mathcal O_E)=\varprojlim_nH^0(Y,\mathcal O_E/\ell^n)$.

Next, we show that $u\equiv1$ modulo $\ell^n$ for every $n$, so that $u=1$.
The trace part of
Proposition [proposition-compatibility-purity-change-coefficients] for
$\mathcal O_E\to\mathcal O_E/\ell^n$ shows that the reduction of $\phi$
modulo $\ell^n$ is the left side of (1) with coefficients
$\mathcal O_E/\ell^n$. By the finite case it equals the trace map with
these coefficients. This is also the reduction of $\operatorname{Tr}_p$,
and that reduction is an isomorphism. Hence $u\equiv1$ modulo $\ell^n$.
For $E$ and $\overline{\mathbf Q}_\ell$ both sides are obtained from the integral ones by inverting
$\ell$ and extending scalars.

*Source:* the proof of Proposition [proposition-compatibility-purity-change-coefficients].
