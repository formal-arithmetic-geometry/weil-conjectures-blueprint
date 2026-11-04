+++
id = "prose-14-02"
kind = "hidden"
title = "Sheaves of rank one"
order = 1082
+++
This subsection shows that every rank-one lisse Weil sheaf on a smooth geometrically
connected curve is pure (Corollary [corollary-rank-one-weights]). In particular the
determinant of every lisse sheaf is pure (Corollary [corollary-determinant-weights]).
Rankin's argument bounds the local eigenvalues of a sheaf by its determinant
weights, so it needs this fact.
The later subsections
Sections [sec-Determinant-weights]–[sec-Exterior-powers-and-purity] are built on it.

In rank one the question is about characters. Let $U_0$ be a smooth
geometrically connected curve and $s\in W(U_0)$ a lift of Frobenius of
degree one (Convention [situation-weil]). A rank-one lisse Weil sheaf is a
character $\chi:W(U_0)\to E^\times$, continuous on $\pi_1(U)$. If $\chi$
is trivial on $\pi_1(U)$, the sheaf is one of the sheaves $\mathcal B_b$
with $b=\chi(s)$. At a closed point $x$ its eigenvalue is
$b^{\deg(x)}$, so it is pure of weight $2\log_q|\iota(b)|$. A Kummer
sheaf is the next simplest case. If $n\mid q-1$, the cover
$t\mapsto t^n$ of $\mathbf G_m$ is a $\mu_n$-torsor. A character of
$\mu_n(k_0)$ then gives a rank-one sheaf on $\mathbf G_{m,k_0}$ whose
geometric monodromy is cyclic of order dividing $n$. Its eigenvalues
are roots of unity, and it is pure of weight $0$.

Up to a twist, every rank-one sheaf behaves like these two. Indeed, by
Theorem [theorem-rank-one-sheaves-have-finite] the image $\chi(\pi_1(U))$
is finite. This means that $\chi(\operatorname{Frob}_x)$ is $\chi(s)^{\deg(x)}$
times a root of unity, and hence the sheaf is pure of weight
$2\log_q|\iota(\chi(s))|$.

Finiteness is a statement about Weil sheaves. On the
geometric curve there are rank-one local systems with infinite
monodromy. The tame fundamental group of
$\mathbf G_{m,k}$ has the quotient $\mathbf Z_\ell(1)\simeq\mathbf Z_\ell$, and
$a\mapsto(1+\ell)^a$ is a character of infinite order. But it has no
Weil structure. A Weil structure forces $\chi(s^{-1}gs)=\chi(g)$ for
$g\in\pi_1(U)$, while conjugation by $s$ acts on $\mathbf Z_\ell(1)$ by multiplication by
a power $q^{\pm1}$. A character of $\mathbf Z_\ell(1)$ that extends to the Weil group
therefore satisfies $\chi(g)^{q-1}=1$, and it has finite order.

The general proof follows the same pattern. Since there is no explicit
quotient to compute with, it uses a logarithm instead. A power $\chi^N$ takes
values in $1+\mathfrak m_E^r$, where the $\ell$-adic logarithm converges. Then
$\log\chi^N$ is an additive character of $\pi_1(U)$ invariant under
conjugation by $s$, that is, a class in $H^1(U,E)$ fixed by Frobenius
(Lemma [lemma-invariant-additive-characters]). Such a class is zero
(Proposition [proposition-no-fixed-class-degree-one]), so $\chi^N$ is
trivial on $\pi_1(U)$.

For a proper curve, Frobenius fixes no class in $H^1$ because the
Jacobian has only finitely many rational points. If $C_0$ is a proper
curve with Jacobian $J_0$, Kummer theory and Poincaré duality identify
$\varprojlim_nH^1(C,\mathbf Z/\ell^n)$ with the dual of the Tate module
$T_\ell J$ (Proposition [proposition-kummer-duality-integral-tate-module]). A fixed vector in the
dual means that $1$ is an eigenvalue of Frobenius on
$V_\ell J=T_\ell J\otimes\mathbf Q_\ell$. After scaling, Frobenius would then
fix a nonzero element of $T_\ell J$. Such an element is a compatible system
of $\ell$-power torsion points of $J$ defined over $k_0$, of unbounded order.
They cannot all lie in the finite group $J_0(k_0)$, and so there is no such
element (Proposition [proposition-no-frobenius-fixed-vector]).

For an open curve, the residue sequence contains in addition the boundary term
$H^0(D,E(-1))$. A power of Frobenius acts on it by a power of $q\ne1$, so it
has no fixed vector either. For $\mathbf G_m$ this is the computation above,
since there $H^1(\mathbf G_{m,k},\mathbf Q_\ell)=\mathbf Q_\ell(-1)$, with Frobenius acting by $q$.
