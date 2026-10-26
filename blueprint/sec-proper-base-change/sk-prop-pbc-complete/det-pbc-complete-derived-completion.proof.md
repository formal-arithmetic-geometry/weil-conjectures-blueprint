+++
kind = "proof"
of = "det-pbc-complete-derived-completion"
uses = ["det-pe-derived-nakayama-resolution", "def-pe-derived-complete", "det-pe-products-exact", "det-pe-milnor-sequence", "lem-weil-derived-limit-existence", "det-prop-sfb-module-pullback-exact-main", "def-weil-derived-direct-image"]
+++
(1) $\operatorname{Tow}(T)$ is the category of functors from the poset
$\mathbf Z_{\geq1}^{\mathrm{op}}$ to the Grothendieck abelian category
$\Mod_{\mathcal O_{E,T}}$, hence Grothendieck abelian, with limits, colimits and
exactness computed levelwise. The left adjoint of $\operatorname{ev}_n$ sends
$N$ to the tower equal to $N$ in levels $m\leq n$, with identity transitions
there, and to $0$ in levels $m>n$; it is exact. A right adjoint of a functor
with an exact left adjoint preserves K-injective complexes:
$\operatorname{Hom}(B,\operatorname{ev}_nI)=\operatorname{Hom}(L_nB,I)$ is acyclic
for acyclic $B$.

(2) Cohomology in $\operatorname{Tow}(T)$ is computed levelwise, so a complex of
towers is acyclic if and only if each level is. Apply this to the cone of a
representative of $a$.

(3) The first equality holds on the nose. For the second, compute
$Ru^{\operatorname{Tow}}_*$ by a K-injective complex of towers $I_\bullet$; by
(1) each $\operatorname{ev}_nI_\bullet$ is K-injective, so
$\operatorname{ev}_nu^{\operatorname{Tow}}_*I_\bullet=u_*\operatorname{ev}_nI_\bullet$
computes $Ru_*\operatorname{ev}_nI_\bullet$ ([def-weil-derived-direct-image]).
Units and counits are defined levelwise, so they are compatible.

(4) The functor $u^{\operatorname{Tow}}_*$ is right adjoint to the exact functor
$u^*_{\operatorname{Tow}}$ ([det-prop-sfb-module-pullback-exact-main], levelwise), and
$\varprojlim$ is right adjoint to the exact functor $c$; hence both preserve
K-injective complexes, by the argument of (1). Therefore
$R\varprojlim\circ Ru^{\operatorname{Tow}}_*=R(\varprojlim\circ u^{\operatorname{Tow}}_*)$
and $Ru_*\circ R\varprojlim=R(u_*\circ\varprojlim)$. The underived functors agree,
$\varprojlim\circ u^{\operatorname{Tow}}_*=u_*\circ\varprojlim$, because $u_*$
commutes with limits; this gives the isomorphism.

(5) Countable products in $\Mod_{\mathcal O_{E,T}}$ are exact ([det-pe-products-exact]), so
$R\varprojlim$ is computed on any tower of complexes by the Milnor cone
([det-pe-milnor-sequence]), which agrees with the K-injective computation by
[lem-weil-derived-limit-existence] (3). The Milnor cone is built from a
product and a cone. An exact equivalence preserves products and cones. For a
bounded complex $P$ of finite free modules, $-\otimes P$ is a finite iterated
cone of finite direct sums of shifts of the identity, applied termwise, so it
commutes with $\prod_n$ and with the cone of $1-T$.

(6) Fix $m$ and put $R_m=[\mathcal O_{E,T}\xrightarrow{\pi_E^m}\mathcal O_{E,T}]$, so that
$\operatorname{red}(N)_m=N\otimes R_m$ ([det-pe-derived-nakayama-resolution]). By (5),

$$
\widehat M\otimes R_m\simeq R\varprojlim_n\bigl(M\otimes R_n\otimes R_m\bigr).
$$

For $n\geq m$ the complex $R_n\otimes R_m$ is quasi-isomorphic, compatibly with
the transitions in $n$, to $R_n\otimes(\mathcal O_E/\pi_E^m)_T=
[(\mathcal O_E/\pi_E^m)_T\xrightarrow{0}(\mathcal O_E/\pi_E^m)_T]$, which is the
direct sum of $(\mathcal O_E/\pi_E^m)_T$ in degree $0$, with identity
transitions, and $(\mathcal O_E/\pi_E^m)_T[1]$, with transitions multiplication
by $\pi_E$ (the degree $-1$ component of the transition maps of notation 3).
Hence the tower $(M\otimes R_n\otimes R_m)_{n\geq m}$
is the direct sum of the constant tower $c(M_m)$ and a tower $N_\bullet$ in
which every composite of $m$ transitions is multiplication by $\pi_E^m$, which
is zero on $M_m$. For $N_\bullet$ the endomorphism $T$ of $\prod_nN_n$ in the
Milnor cone satisfies $T^m=0$, so $1-T$ is invertible with inverse
$\sum_{k<m}T^k$, and $R\varprojlim N_\bullet=0$. Finitely many levels $n<m$ do
not change the derived limit. Therefore $\widehat M\otimes R_m\simeq
R\varprojlim c(M_m)\simeq M_m$, and this isomorphism is inverse to
$\kappa_M\otimes R_m$, since $\kappa_M\otimes R_m$ is induced by the inclusion of
the constant summand. The identifications are compatible with $m+1\to m$, which
gives the isomorphism of towers $\operatorname{red}(\kappa_M)$ (an isomorphism
in $D(\operatorname{Tow}(T))$ by (2)).

Completeness of $\widehat M$. The same computation with the roles of $n$ and
$m$ exchanged shows that, for fixed $n$, the complex $N_n=M\otimes R_n$ is
derived complete: for $m\geq n$, $R_m\otimes R_n\simeq
[(\mathcal O_E/\pi_E^n)_T\xrightarrow{0}(\mathcal O_E/\pi_E^n)_T]$ compatibly with
the transitions in $m$, so $(N_n\otimes R_m)_m$ is the sum of the constant tower
$c(N_n)$ and a tower whose $n$-fold composites of transitions vanish, and
$\kappa_{N_n}\colon N_n\to R\varprojlim_m(N_n\otimes R_m)$ is an isomorphism. Now
$\widehat M=R\varprojlim_nN_n$, and by (5)

$$
\widehat{\widehat M}=R\varprojlim_m\Bigl(\bigl(R\varprojlim_nN_n\bigr)\otimes R_m\Bigr)
\simeq R\varprojlim_mR\varprojlim_n(N_n\otimes R_m)
\simeq R\varprojlim_nR\varprojlim_m(N_n\otimes R_m),
$$

the last step because both iterated Milnor cones are the total complex of the
commutative square formed by $1-T_n$ and $1-T_m$ on
$\prod_{n,m}N_n\otimes R_m$. Under these identifications
$\kappa_{\widehat M}=R\varprojlim_n\kappa_{N_n}$, since both are induced by the
inclusions of the constant towers. Each $\kappa_{N_n}$ is an isomorphism, hence
so is $\kappa_{\widehat M}$, and $\widehat M$ is derived complete
([def-pe-derived-complete]).
