+++
kind = "proof"
of = "det-pbc-complete-tower-calculus"
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
computes $Ru_*\operatorname{ev}_nI_\bullet$. Units and counits are defined
levelwise, so they are compatible.

(4) The functor $u^{\operatorname{Tow}}_*$ is right adjoint to the exact functor
$u^*_{\operatorname{Tow}}$ ([sk-prop-sfb-module-pullback-exact], levelwise), and
$\varprojlim$ is right adjoint to the exact functor $c$; hence both preserve
K-injective complexes, by the argument of (1). Therefore
$R\varprojlim\circ Ru^{\operatorname{Tow}}_*=R(\varprojlim\circ u^{\operatorname{Tow}}_*)$
and $Ru_*\circ R\varprojlim=R(u_*\circ\varprojlim)$. The underived functors agree,
$\varprojlim\circ u^{\operatorname{Tow}}_*=u_*\circ\varprojlim$, because $u_*$
commutes with limits; this gives the isomorphism.

(5) Products in $\Mod_{\mathcal O_{E,T}}$ are exact ([sk-prop-pe-products]), so
$R\varprojlim$ is computed on any tower of complexes by the Milnor cone of
[sk-prop-pe-milnor], which agrees with the K-injective computation by
[lem-weil-derived-limit-existence] (3). The Milnor cone is built from a
product and a cone. An exact equivalence preserves products and cones. For a
bounded complex $P$ of finite free modules, $-\otimes P$ is a finite iterated
cone of finite direct sums of shifts of the identity, applied termwise, so it
commutes with $\prod_n$ and with the cone of $1-T$.
