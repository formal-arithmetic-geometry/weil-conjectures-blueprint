+++
id = "prose-E-07"
kind = "hidden"
title = "The external product for nearby cycles"
order = 953
+++
To specialize a trace class we have to specialize the external product
$K\boxtimes \mathbb DK$, and hence we need to know that the comparison
map from the external product of nearby cycles to the nearby cycles of
the external product is an isomorphism. We prove this by the dimension
argument of
[illusie94, Theorem 4.7, pp. 51–53], on the classical
étale site.

From now on, $S$ is an excellent strictly henselian trait, with separably
closed residue field $k$, generic point $\eta$, and a chosen geometric
generic point $\bar\eta$. Let $p$ be the characteristic exponent of
$k$. The coefficients lie in a finite commutative $\ell$-primary ring
$A$, with $\ell$ invertible on $S$. On the geometric fibres we use the
ordinary external Künneth formula,
Proposition [sk-lem-sf-kunneth-star]. It applies over the
separably closed field $k$, since passing to an algebraic closure is a
purely inseparable extension and does not change the étale topos.

We use two further facts about traits, both from [sga4-5],
*Théorèmes de finitude*, §§3.4 and 3.7.
First, geometric nearby cycles are invariant under extension of
traits, with the corresponding restriction of the inertia action
(loc. cit., 3.7). Second, they admit the following description by
restriction to the generic point of a coordinate line (the calculation in loc. cit., 3.4).
Let $s'$ be a geometric generic point of the special fibre
$\mathbf A^1_k$ of $\mathbf A^1_S$, and let $S'=(\mathbf A^1_S)_{(s')}$ be
the strict localization of $\mathbf A^1_S$ at $s'$. This is a
strictly henselian trait with the same uniformizer as $S$. With
compatible geometric generic points, its inertia group fits into an exact sequence

$$
1\longrightarrow P\longrightarrow I'\longrightarrow I
\longrightarrow1,
$$

where $P$ is pro-$p$ (and is trivial when $p=1$).
For $a:W\to\mathbf A^1_S$, put $W'=W\times_{\mathbf A^1_S}S'$, and let $N'$ be the pullback
of $N\in D^b_{\mathrm{ctf}}(W_\eta,A)$. There is a canonical
identification

$$
(R\Psi_{W/S}N)|_{W_s\times_{\mathbf A^1_k}s'}
\simeq (R\Psi_{W'/S'}N')^P.
\tag{E.2}
$$

Here $(-)^P=R\Gamma(P,-)$ is exact on the discrete
torsion coefficients prime to $p$ under consideration. To obtain the formula,
we factor the map from the geometric generic fibre
through the geometric generic point of $S'$, which lies over
$\bar\eta$; the Galois group of the second step is $P$. The kernel
is pro-$p$ because the common uniformizer identifies the tame inertia
quotients. Factoring the maps of generic fibres in the same way and
using that the adjunctions for direct image are compatible with
composition, we see that the formula is compatible with the base change maps for
pullback and with the product maps obtained from $\bar i^*R\bar j_*$.

The functor of invariants in this statement commutes with tensoring by
an object on which $P$ acts trivially: for a complex $Q$ with
continuous $P$-action and a complex $B$ with trivial $P$-action, the
projection map is an isomorphism

$$
(Q\mathbin{\otimes_A^{\mathbf L}}B)^P
\simeq Q^P\mathbin{\otimes_A^{\mathbf L}}B.
\tag{E.3}
$$

Indeed, $P$-invariants are exact on discrete torsion
$A$-modules. For a finite quotient $G$ of $P$, the invariants are the
image of the averaging idempotent $|G|^{-1}\sum_{g\in G}g$, since the
$p$-power $|G|$ is invertible in $A$, and this idempotent commutes with
tensoring by $B$. By continuity we pass from the finite quotients to
$P$, and resolving $B$ by flat $A$-modules gives the derived identity.

For $X,Y$ separated of finite type over $S$, $L$ on $X_\eta$ and $M$
on $Y_\eta$, the comparison map $\Pi_{L,M}$ below is the restriction to
the special fibre of the map

$$
R\bar j_{X*}L_{\bar\eta}\boxtimes
R\bar j_{Y*}M_{\bar\eta}
\longrightarrow
R\bar j_{X\times Y,*}(L_{\bar\eta}\boxtimes M_{\bar\eta})
$$

defined by the base change maps for pullback and the lax monoidal
structure of direct image.
