+++
kind = "proof"
of = "det-curve-affine-kummer-residue-sequence"
+++
*Part 1.* Let $P$ be a $\mu_n$-torsor on $U_{\mathrm{ét}}$. Its pushout along
$\mu_n\subseteq\mathbf G_m$ is a $\mathbf G_m$-torsor, i.e. a line bundle $L$
(Hilbert 90 and descent), and the pushout of $P$ along
$\mu_n\to\mathbf G_m$, $\zeta\mapsto\zeta^n=1$, is $L^{\otimes n}$ on the one
hand and the trivial torsor on the other, which gives
$\alpha:L^{\otimes n}\simeq\cO_U$. Conversely $P$ is recovered as the sheaf
of local sections $t$ of $L$ with $\alpha(t^{\otimes n})=1$; this sheaf is a
$\mu_n$-torsor because locally $L\cong\cO$ and the equation $t^n=a$ with $a$
a unit has a solution étale locally ([lem-sc-kummer-exact]). The two
constructions are inverse, compatible with isomorphisms, and turn contracted
products of torsors into tensor products of pairs. This is the standard
Kummer description underlying [lem-sc-kummer-les].

*Part 2.* As $\overline C$ is regular, every line bundle on $U$ extends to
$\overline C$ ([lem-sc-divisor-class-curve]: write $L=\cO_U(E)$ for a divisor
$E$ on $U$ and take the closure of $E$). Since $\alpha$ is an isomorphism on
$U$, the rational section $s$ is regular and nowhere zero on $U$, so
$\operatorname{div}(s)$ is supported on $D$. Two extensions differ by a
divisor supported on $D$: $\overline L'=\overline L(E)$ with
$\operatorname{supp}E\subseteq D$, and then the same $s$, viewed in
$\overline L'^{\otimes n}=\overline L^{\otimes n}(nE)$, has divisor
$\operatorname{div}(s)-nE$; the orders change by multiples of $n$. An
isomorphism of pairs $\varphi:(L,\alpha)\simeq(L',\alpha')$ extends to a
rational isomorphism of extensions carrying $s$ to $s'$, so it does not change
the residues either. For the product of two pairs the section is
$s\otimes s'$, whose orders add; thus $\partial$ is a homomorphism.

*Part 3.* Since $\deg\overline L^{\otimes n}=n\deg\overline L$ and the degree
of a line bundle is the degree of the divisor of any rational section,
$\sum_x\operatorname{ord}_x(s)=n\deg\overline L\equiv0\pmod n$; hence
$\sum\circ\partial=0$. The map $\sum$ is surjective because $D\neq\emptyset$.

*Exactness at $(\Z/n)^D$.* Let $(a_x)$ have $\sum_xa_x\equiv0$. Lift it to
integers $(b_x)$ and change $b_{x_1}$ by a multiple of $n$ so that
$\sum_xb_x=nd$. Put $B=\sum_xb_x\,x$ and fix a closed point $x_0$. The
line bundle $\cO(B)\otimes\cO(dx_0)^{\otimes-n}$ has degree $0$, so it lies
in $\operatorname{Pic}^0(\overline C)=J(k)$
([lem-sc-pic-proper-decomposition], [thm-sc-jacobian-representability]),
which is $n$-divisible ([thm-av-final](d)); write it as $M^{\otimes n}$ and
put $\overline L=\cO(dx_0)\otimes M$. Choose an isomorphism
$\beta:\overline L^{\otimes n}\simeq\cO(B)$ and let $1_B$ be the canonical
rational section of $\cO(B)$, with divisor $B$. On $U$, $\cO(B)|_U=\cO_U$
and $1_B$ restricts to $1$, so $\alpha=\beta|_U$ is a Kummer pair on $U$ with
$s=\beta^{-1}(1_B)$ of divisor $B$, whence $\partial(\overline L|_U,\alpha)=(a_x)$.

*Exactness at $H^1(U,\mu_n)$.* A pair $(\overline L,\overline\alpha)$ on
$\overline C$ restricted to $U$ may be extended by $\overline L$ itself, and
then $s=\overline\alpha^{-1}(1)$ has no zero or pole; so $\partial j^*=0$.
Conversely, suppose $\operatorname{ord}_x(s)=nm_x$ for all $x\in D$, and put
$E=\sum_xm_x\,x$. In $\overline L(-E)^{\otimes n}=\overline L^{\otimes n}(-nE)$
the section $s$ has divisor $\operatorname{div}(s)-nE=0$, so it is a nowhere
vanishing global section, i.e. an isomorphism
$\overline\alpha:\overline L(-E)^{\otimes n}\simeq\cO_{\overline C}$ with
$\overline\alpha(s)=1$, extending $\alpha$. Thus $(L,\alpha)$ lies in the
image of $j^*$.

*Injectivity of $j^*$.* If $(\overline L,\overline\alpha)$ becomes trivial on
$U$, there is a section $t$ of $\overline L$ over $U$ with
$t^{\otimes n}=\overline\alpha^{-1}(1)|_U$. As a rational section of
$\overline L$, $t$ satisfies
$n\operatorname{div}(t)=\operatorname{div}(\overline\alpha^{-1}(1))=0$, so
$\operatorname{div}(t)=0$ and $t$ is a global trivialization of
$\overline L$ with $\overline\alpha(t^{\otimes n})=1$; the pair is trivial on
$\overline C$.

*Rank.* $H^1(\overline C,\mu_n)\cong J[n](k)\cong(\Z/n)^{2g}$
([det-curveestimate-canonical-mu]), and $\ker\sum$ is free over $\Z/n$ with
basis $e_x-e_{x_1}$, $x\neq x_1$, of rank $r-1$. The short exact sequence
$0\to H^1(\overline C,\mu_n)\to H^1(U,\mu_n)\to\ker\sum\to0$ splits because
its quotient is free, so $H^1(U,\mu_n)\cong(\Z/n)^{2g+r-1}$.

*Part 4.* $\overline C_{k'}$ is smooth, proper and connected
([lem-sc-base-change-curve]), and $D_{k'}$ consists of the $r$ points
$x\otimes k'$ since each $x$ is a $k$-point. Pullback carries a pair
$(L,\alpha)$ to $(L_{k'},\alpha_{k'})$, an extension $\overline L$ to
$\overline L_{k'}$, and $s$ to $s_{k'}$. A uniformizer of
$\cO_{\overline C,x}$ remains a uniformizer of the local ring of
$\overline C_{k'}$ at $x\otimes k'$ (the closed fibre is
$\operatorname{Spec}k'$), so orders of vanishing are unchanged. Hence the
diagram formed by the two residue sequences and the pullback maps commutes,
with the identity on the residue and sum terms. The left vertical map is an
isomorphism by [det-curveestimate-canonical-mu], so the five lemma shows the
middle one is an isomorphism.
