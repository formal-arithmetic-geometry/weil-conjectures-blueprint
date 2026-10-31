+++
id = "prose-10-08"
kind = "hidden"
title = "The trace map of affine space"
order = 440
+++
Every identification of $f^!$ in this section is ultimately an
adjunction whose counit is integration along affine lines, so we first
make that integration explicit. The affine line is not proper, and we
cannot integrate on it directly; instead we integrate on $\mathbf P^1$,
where on a geometric fibre
$H^2(\mathbf P^1,\mathbf Z/\ell^n(1))\simeq\mathbf Z/\ell^n$, generated
by $c_1(\mathcal O(1))$, the class of a point. The trace map of
$\mathbf P^1$ reads off the coefficient of this class, and the trace map
of $\mathbf A^1$ is its composite with the map
$H^2_c(\mathbf A^1,\mathbf Z/\ell^n(1))\to H^2(\mathbf P^1,\mathbf Z/\ell^n(1))$
given by extension by zero; over an algebraically closed field this map
is an isomorphism of groups $\mathbf Z/\ell^n$. Two
facts about this construction carry the rest of the proof: it works
over an arbitrary base $S$ and commutes with base change, and iterating
it gives the trace map (10.7) of
$\mathbf A^d$, the counit of the adjunction on a chart. The subsection
then records the device used to compare such local adjunctions, pairs
consisting of an object and a counit
(Definition [sk-def-sp-representing-pair]), and ends with purity for
vector bundles (Proposition [sk-prop-an]), the first case in
which the trace map is defined without a choice of coordinates.

For a scheme $T$, Chern classes are defined by the Kummer sequence on $T_{\acute{e}t}$,

$$
1\longrightarrow\mu_{\ell^n}\longrightarrow\mathbf G_m
\xrightarrow{\ (\cdot)^{\ell^n}\ }\mathbf G_m
\longrightarrow1,
\tag{10.3}
$$

whose boundary $H^1(T_{\acute{e}t},\mathbf G_m)\to H^2(T_{\acute{e}t},(\mathbf Z/\ell^n\mathbf Z)_T(1))$ sends a line bundle $L$
to $c_1(L)$. For a scheme $S$, let $q:\mathbf P^1_S\to S$ be the projection. By
Lemma [sk-lem-geo-p1-cohomology], the unit and
$c_1(\mathcal O_{\mathbf P^1_S}(1))$ give an isomorphism, compatible with base change,

$$
Rq_*(\mathbf Z/\ell^n\mathbf Z)_{\mathbf P^1_S}
\simeq(\mathbf Z/\ell^n\mathbf Z)_{S}\oplus(\mathbf Z/\ell^n\mathbf Z)_{S}(-1)[-2],
\tag{10.4}
$$

and the *trace map*
$\operatorname{Tr}_q:Rq_*(\mathbf Z/\ell^n\mathbf Z)_{\mathbf P^1_S}(1)[2] \to(\mathbf Z/\ell^n\mathbf Z)_{S}$ is the projection onto the second
summand, after twisting. It sends $c_1(\mathcal O_{\mathbf P^1_{\bar s}}(1))$ on
each geometric fibre to $1$.

Let $p_1,p_2$ be the projections of
$\mathbf P^1_S\times_S\mathbf P^1_S$, and let $x_0,x_1$ and $y_0,y_1$ be the
pullbacks along $p_1$ and $p_2$ of the homogeneous coordinates of
$\mathbf P^1_S$. The diagonal $\Delta$ is the zero locus of the section
$x_0y_1-x_1y_0$ of $p_1^*\mathcal O(1)\otimes p_2^*\mathcal O(1)$, so that
$\mathcal O(\Delta)$ is this line bundle and $x_0y_1-x_1y_0$ is its
canonical section. Lemma [sk-lem-geo-cartier] provides the cycle
class of $\Delta$,

$$
\delta:\Delta_*(\mathbf Z/\ell^n\mathbf Z)_{\mathbf P^1_S}
\longrightarrow(\mathbf Z/\ell^n\mathbf Z)_{\mathbf P^1_S\times_S\mathbf P^1_S}(1)[2],
$$

the Kummer boundary of $\mathcal O(\Delta)$ with its canonical section,
compatible with every base change on $S$. Let
$\operatorname{Tr}_{p_i}$ be the pullback of $\operatorname{Tr}_q$. Then the
diagonal integrates to $1$ along either factor, that is,

$$
\operatorname{Tr}_{p_i}\circ Rp_{i*}\delta
=\operatorname{id}_{(\mathbf Z/\ell^n\mathbf Z)_{\mathbf P^1_S}}
\qquad(i=1,2).
\tag{10.5}
$$

This is (7.5) of Proposition [sk-prop-geo-p1-adjunction]. Both sides
are endomorphisms of a constant sheaf, and so it suffices to check
(10.5) on geometric fibres of $p_i$. There the
diagonal is a single rational point, whose line bundle is $\mathcal O(1)$.
Hence $\delta$ restricts to $c_1(\mathcal O(1))$, which
$\operatorname{Tr}_q$ sends to $1$.

For $\Lambda=\mathbf Z/\ell^n\mathbf Z$,
Proposition [sk-prop-geo-p1-adjunction] gives the adjunction
$Rq_*\dashv q^*(-)(1)[2]$, and its unit and counit, (7.6) and
(7.7) there, take the following form. The counit is integration
along the fibres,

$$
\varepsilon_K:Rq_*\bigl(q^{*}K(1)[2]\bigr)
\simeq K\otimes^{\mathbf L} Rq_*(\mathbf Z/\ell^n\mathbf Z)_{\mathbf P^1_S}(1)[2]
\xrightarrow{\ \operatorname{id}_K\otimes\operatorname{Tr}_q\ } K,
\tag{10.6}
$$

and the unit is the class of the diagonal,

$$
\eta_M:\ M\simeq Rp_{2*}\Delta_*M
\xrightarrow{\ Rp_{2*}(\delta\otimes p_1^*M)\ } Rp_{2*}p_{1}^{*}M(1)[2]
\simeq q^{*}Rq_*M(1)[2],
$$

using the projection formulas and proper base change. Both commute with
base change on $S$, and the triangle identities reduce to
(10.5).

Let $j:\mathbf A^1_S\hookrightarrow\mathbf P^1_S$ be the complement of
the section at infinity, and let $p=q\circ j$. Composing
this adjunction with $j_!\dashv j^*$ we obtain an adjunction
$Rp_!\dashv p^*(-)(1)[2]$ between
$D^b_{\mathrm{ctf}}(\mathbf A^1_{S,\mathrm{pro}\acute{e}t},\mathbf Z/\ell^n\mathbf Z)$ and
$D^b_{\mathrm{ctf}}(S_{\mathrm{pro}\acute{e}t},\mathbf Z/\ell^n\mathbf Z)$, whose counit is the counit for the
open immersion followed by $\varepsilon_K$. For the constant sheaf, applying
$Rq_*$ to the localization triangle for the section at infinity shows that
$Rp_!(\mathbf Z/\ell^n\mathbf Z)_{\mathbf A^1_S}\simeq (\mathbf Z/\ell^n\mathbf Z)_S(-1)[-2]$ is the second summand of
(10.4). Indeed, restriction to infinity is the
identity on the first summand and kills the second, because the pullback of
$\mathcal O(1)$ along the section at infinity is the trivial line bundle on
$S$, so that the restriction of $c_1(\mathcal O(1))$ is $0$. It follows that the counit at the constant sheaf, which we call the
*trace map of the affine line*
$\operatorname{Tr}_p:Rp_!(\mathbf Z/\ell^n\mathbf Z)_{\mathbf A^1_S}(1)[2] \to(\mathbf Z/\ell^n\mathbf Z)_S$, is an isomorphism. Over a geometric
point this is $H^2_c(\mathbf A^1,(\mathbf Z/\ell^n\mathbf Z)(1))\simeq \mathbf Z/\ell^n\mathbf Z$, generated by the class $\kappa$ that maps to
the class of a point in $H^2(\mathbf P^1,(\mathbf Z/\ell^n\mathbf Z)(1))$.

For affine space, let $p_j:\mathbf A^j_S\to S$ be the projection and
let $r_j:\mathbf A^j_S\to\mathbf A^{j-1}_S$ be the map forgetting the last
coordinate. We define $\operatorname{Tr}_{p_j}$ inductively as the composite

$$
\begin{aligned}
Rp_{j!}(\mathbf Z/\ell^n\mathbf Z)_{\mathbf A^j_S}(j)[2j]
&\simeq Rp_{j-1!}\bigl(Rr_{j!}(\mathbf Z/\ell^n\mathbf Z)_{\mathbf A^j_S}(1)[2]\bigr)(j-1)[2j-2]\\
&\xrightarrow{\ \operatorname{Tr}_{p_{j-1}}\circ Rp_{j-1!}(\operatorname{Tr}_{r_j})\ }
(\mathbf Z/\ell^n\mathbf Z)_S,
\end{aligned}
$$

using $Rp_{j!}=Rp_{j-1!}Rr_{j!}$ and the projection formula. For $j=d$
this is the *trace map of affine space*, an isomorphism (the identity when $d=0$)

$$
\operatorname{Tr}_{p_d}:Rp_{d!}(\mathbf Z/\ell^n\mathbf Z)_{\mathbf A^d_S}(d)[2d]
\xrightarrow{\sim}(\mathbf Z/\ell^n\mathbf Z)_{S}.
\tag{10.7}
$$

By Lemma [sk-lem-geo-affine-local](1), $Rp_{d!}\dashv p_d^*(-)(d)[2d]$, and the counit is the composite of the $d$ counits for the
affine lines, which at the constant sheaf is
(10.7). The unit and counit commute with base
change. On a geometric fibre, the external product
$\kappa\boxtimes\cdots\boxtimes\kappa\in H_c^{2d}(\mathbf A^d_{\bar s},(\mathbf Z/\ell^n\mathbf Z)(d))$
integrates to $1$, since by the projection formula, integrating along the
last coordinate replaces the last factor by its integral, which is $1$.

On a chart $U\to\mathbf A^d_Y$ we now have an explicit candidate for
$f^!K|_U$, namely $e^*p_d^*K(d)[2d]$ with the counit given by the trace
map of affine space. To compare the candidates with $f^!K$, and later,
for towers, to glue $f^!$ from them, we need a notion that makes sense
on each open separately. A right adjoint is a functor on the whole of
$X$, and knowing an object of $D(U)$ isomorphic to $f^!K|_U$ is of no
use for comparison: two isomorphisms on an overlap may differ by an
automorphism. What is preserved by restriction is a pair, an object
together with a counit, which satisfies a universal property. Such a
pair is unique up to a unique isomorphism compatible with the counit, so
local pairs are compared on overlaps without any choice of transition
maps. This is used for the comparison following
Definition [sk-def-sp-representing-pair] and in the construction of
the right adjoint for towers (Proposition [sk-prop-sp-tower-geometric]).
