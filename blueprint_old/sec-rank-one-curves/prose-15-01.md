+++
id = "prose-15-01"
kind = "hidden"
title = "Rank-one sheaves on curves"
order = 643
+++
Rankin's argument, as sketched in the Part opening, bounds the local
eigenvalues of a sheaf by its determinant weights. For that to mean
anything, the determinant of a lisse sheaf must have a weight, that is,
it must be pure. A determinant is a sheaf of rank one, and this section
shows that every rank-one lisse Weil sheaf on a smooth geometrically
connected curve is pure (Corollary [sk-cor-wrp-rankone-pure]); applied to
determinants, this gives Corollary [sk-d-real-detweights], the input of
Sections [sec-determinant-weights] and [sec-purity-real-sheaves].

In rank one the question is about characters. Let $U_0$ be a smooth
geometrically connected curve and $s\in W(U_0)$ a lift of Frobenius of
degree one (Convention [sk-d-real-weil]). A rank-one lisse Weil sheaf is a
character $\chi:W(U_0)\to E^\times$, continuous on $\pi_1(U)$. If $\chi$
is trivial on $\pi_1(U)$, the sheaf is one of the sheaves $\mathcal B_b$
with $b=\chi(s)$; at a closed point $x$ its eigenvalue is
$b^{\deg(x)}$, so it is pure of weight $2\log_q|\iota(b)|$. A Kummer
sheaf is the next simplest case. If $n\mid q-1$, the cover
$t\mapsto t^n$ of $\mathbf G_m$ is a $\mu_n$-torsor, and a character of
$\mu_n(k_0)$ gives a rank-one sheaf on $\mathbf G_{m,k_0}$ whose
geometric monodromy is cyclic of order dividing $n$. Its eigenvalues
are roots of unity, so it is pure of weight $0$. The main theorem says
that every rank-one sheaf behaves like these two up to a twist: the image
$\chi(\pi_1(U))$ is finite (Theorem [sk-p-real-rankone]). Then
$\chi(\operatorname{Frob}_x)$ is $\chi(s)^{\deg(x)}$ times a root of
unity, and the sheaf is pure of weight $2\log_q|\iota(\chi(s))|$.

Finiteness is a statement about Weil sheaves. On the
geometric curve there are rank-one local systems with infinite
monodromy. The tame fundamental group of
$\mathbf G_{m,k}$ has the quotient $\Zl(1)\simeq\Zl$, and
$a\mapsto(1+\ell)^a$ is a character of infinite order. It does not
carry a Weil structure, and the reason is the whole proof in miniature.
A Weil structure forces $\chi(s^{-1}gs)=\chi(g)$ for $g\in\pi_1(U)$,
while conjugation by $s$ acts on $\Zl(1)$ by multiplication by a power
$q^{\pm1}$. Hence a character of $\Zl(1)$ that extends to the Weil
group satisfies $\chi(g)^{q-1}=1$, and has finite order. In general there is no explicit
quotient to compute with, and we argue as follows. A power $\chi^N$
takes values in $1+\mathfrak m_E^r$, where the $\ell$-adic logarithm
converges, and $\log\chi^N$ is an additive character of $\pi_1(U)$
invariant under conjugation by $s$, that is, a class in $H^1(U,E)$
fixed by Frobenius (Lemma [sk-lem-wrp-additive]). Such a class is zero
(Proposition [sk-prop-wrp-h1-no-fixed]), so $\chi^N$ is trivial on
$\pi_1(U)$.

The vanishing of Frobenius-fixed classes in $H^1$ is the arithmetic
heart of the section, and it comes from the finiteness of the group of
rational points of the Jacobian. For a proper curve $C_0$ with Jacobian
$J_0$, Kummer theory and Poincaré duality identify
$\varprojlim_nH^1(C,\mathbf Z/\ell^n)$ with the dual of the Tate module
$T_\ell J$ (Proposition [sk-d-real-jacobian]). A fixed vector in the
dual means that $1$ is an eigenvalue of Frobenius on
$V_\ell J=T_\ell J\otimes\Ql$, and hence, after scaling, that Frobenius
fixes a nonzero element of $T_\ell J$. Such an element would be a compatible system of $\ell$-power
torsion points of $J$ defined over $k_0$, of unbounded order, in the
finite group $J_0(k_0)$ (Proposition [sk-p-tate]). For an
open curve the residue sequence adds the boundary term
$H^0(D,E(-1))$, on which a power of Frobenius acts by a power of
$q\ne1$. For $\mathbf G_m$ this is the computation above: there
$H^1(\mathbf G_{m,k},\Ql)=\Ql(-1)$, with Frobenius acting by $q$.

In Weil II, 1.3.4 [deligne80], Deligne deduces the finiteness
of geometric monodromy in rank one from class field theory. On a curve the argument
with the Jacobian is self-contained given
Appendices [sec-abelian-varieties] and [sec-picard-framework], and curves are all
we need: on a higher-dimensional base, weights are reached by
restriction to curves (Section [sec-deligne-laumon-general]).
