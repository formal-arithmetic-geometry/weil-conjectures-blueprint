+++
id = "lem-pc-hilb-representable"
kind = "lemma"
title = "Hilbert schemes of points are representable"
order = 4369
lean = ["AlgebraicGeometry.hilbFunctor_isRepresentable"]
uses = ["lem-pc-hilb-sheaf", "def-pc-fppf-site", "lem-pc-schemes-criterion", "def-pc-finite-locally-free", "def-pc-hilb-functor"]
+++
(Picard Schemes of Curves, Proposition 44.2.6, [Tag
0B9A](https://stacks.math.columbia.edu/tag/0B9A), with Remark 44.2.7, [Tag
0B9B](https://stacks.math.columbia.edu/tag/0B9B).) Let $X\to S$ be a
morphism of schemes and $d\geq0$. Assume that for all points $s\in S$ and
$x_1,\dots,x_d\in X_s$ (a finite set of points of a fibre) there exists an
affine open $U\subset X$ containing them (e.g. if $X\to S$ is
quasi-projective, or if there exists an ample invertible sheaf on $X$).
Then $\operatorname{Hilb}^d_{X/S}$ is representable by a scheme
$\underline{\operatorname{Hilb}}^d_{X/S}$.

## Proof

*Step 1: the closed-immersion claim.* We shall use the following claim.
*Let $i:X'\hookrightarrow Y$ be a closed immersion, let
$Z\in\operatorname{Hilb}^d_{Y/S}(T)$; then there is a largest closed subscheme
$T_{X'}\subseteq T$ such that $T'\to T$ factors through $T_{X'}$ iff the
pullback $Z_{T'}\to Y_{T'}$ factors through $X'_{T'}$ (and $Z_{T'}$ is the
closed subscheme of $X'_{T'}$ obtained by base change).* Proof: the
condition is local on $T$, so take $T=\operatorname{Spec}(A)$ and, shrinking
$T$, assume $Z=\operatorname{Spec}(B)$ with $B\cong A^{\oplus d}$ as an
$A$-module and $Z\hookrightarrow Y_T$ given by the $A$-algebra map $C\to B$
(with $Y=\operatorname{Spec}(C)$, $X'=\operatorname{Spec}(C/J)$). Let
$g_\beta\in J$ be a set of generators of the ideal $J$; with the
trivialization $\varphi:B\stackrel{\sim}{\to}A^{\oplus d}$ write
$\varphi(g_\beta\cdot-)=(g_\beta^1,\dots,g_\beta^d)$. The factorization
condition is $g_\beta^j=0$ for all $\beta,j$ (the composite $C/J\to B$ is a
well-defined ring homomorphism iff $g_\beta$ acts as zero on $B$, for all
$\beta$), so
$T_{X'}:=\operatorname{Spec}\bigl(A/(g_\beta^j)_{\beta,j}\bigr)$ is the
largest such closed subscheme. (The set $(g_\beta^j)$ may be infinite; a
closed subscheme is nonetheless defined by the ideal they generate, and it
is the largest one with the property.)

*Step 2: reduction to affine $S$.* For an open subscheme $V\subseteq S$ let
$F_V$ be the subfunctor of $\operatorname{Hilb}^d_{X/S}$ consisting of those
$T$ whose structure morphism $T\to S$ factors through $V$; it agrees with
$\operatorname{Hilb}^d_{X_V/V}$ via the canonical isomorphism
$X_T\cong X_V\times_VT$ for such $T$. The family $(F_V)_V$ over the open
affines $V$ of $S$ covers $\operatorname{Hilb}^d_{X/S}$, each inclusion is
representable by an open immersion, and [lem-pc-hilb-sheaf] says
$\operatorname{Hilb}^d_{X/S}$ is a Zariski sheaf (Zariski coverings are fppf
coverings, [def-pc-fppf-site]); hence by [lem-pc-schemes-criterion] it
suffices to prove representability when $S$ is affine.

*Step 3: the affine case.* Assume $S=\operatorname{Spec}(R)$ and
$X=\operatorname{Spec}(A)$ affine over $S$. For an affine open $U\subseteq X$
let $F_U\subseteq\operatorname{Hilb}^d_{X/S}$ be the subfunctor with
$Z\in F_U(T)$ iff $Z\subseteq U_T$. We prove the *affine claim:
$\operatorname{Hilb}^d_{X/S}$ is representable for $X$ and $S$ affine* by
[lem-pc-schemes-criterion] applied to the family $(F_U)_U$: the sheaf
condition (1) is [lem-pc-hilb-sheaf]; (2)(a) is the affine claim itself
(the identity $F_U=\operatorname{Hilb}^d_{U/S}$); (2)(b) and (2)(c) are Steps
5 and 6. So it remains to prove the affine claim, which is Step 4.

*Step 4: the affine claim.* Choose elements $x_i\in A$, $i\in I$,
generating $A$ as an $R$-algebra (take all elements of $A$); then
$R[x_i;i\in I]\to A$ is surjective, so
$X\to Y:=\operatorname{Spec}(R[x_i;i\in I])$ is a closed immersion. By Step 1,
applied to the universal object once the functor for $Y$ is representable,
$\operatorname{Hilb}^d_{X/S}$ is representable by a closed subscheme of
$\underline{\operatorname{Hilb}}^d_{Y/S}$; so it suffices to treat
$A=R[x_i;i\in I]$.

For a finite subset $W=\{f_1,\dots,f_d\}\subseteq A$ of $d$ elements define
the subfunctor $F_W$ of $\operatorname{Hilb}^d_{X/S}$: for a scheme $T$ over
$S$, $Z\in F_W(T)$ iff the map
$$
\bigoplus_{f\in W}\mathcal{O}_T\longrightarrow\mathcal{O}_Z,\qquad
(g_f)\mapsto\sum_{f\in W}g_f\,f|_Z,
$$
is surjective (equivalently an isomorphism, $\mathcal{O}_Z$ being finite
locally free of rank $d$); here $f|_Z$ is the image of $f$ under
$\mathcal{O}_X\to\mathcal{O}_Z$. We verify the conditions of
[lem-pc-schemes-criterion] for the family $(F_W)_W$.

(1) The sheaf condition holds by [lem-pc-hilb-sheaf] (a surjectivity
condition on a finite locally free module is Zariski-local).

(2)(a) *Representability of $F_W$*: fix a numbering $f_1,\dots,f_d$ of $W$
and construct a universal element over an affine
$T_{\mathrm{univ}}=\operatorname{Spec}(R_{\mathrm{univ}})$:
$$
R_{\mathrm{univ}}:=R\bigl[c^m_{kl},b^l,b^l_i\bigr]/\mathfrak a_{\mathrm{univ}},
\qquad
B_{\mathrm{univ}}:=\bigoplus_{l=1}^{d}R_{\mathrm{univ}}e_l,
$$
where the indices range over $1\le k,l,m\le d$ and $i\in I$. Put
$e_ke_l:=\sum_mc^m_{kl}e_m$ and take $\mathfrak a_{\mathrm{univ}}$ to be
the ideal generated by: (i) $c^m_{lk}-c^m_{kl}$ (commutativity); (ii)
$\sum_mc^m_{lk}c^p_{mn}-\sum_qc^q_{kn}c^p_{lq}$ (associativity, for all
$k,l,n,p$); (iii) $\sum_lb^lc^m_{lk}-\delta_{km}$ (the element
$\sum_lb^le_l$ is a unit); (iv) the coefficients $h^m_l$ of
$\Psi(f_l)-e_l=\sum_mh^m_le_m$, where
$\Psi:A\otimes_RR_{\mathrm{univ}}\to B_{\mathrm{univ}}$ is the
$R_{\mathrm{univ}}$-algebra map sending
$1\otimes1\mapsto\sum_lb^le_l$ and $x_i\mapsto\sum_lb^l_ie_l$ (this map
exists by the universal property of the polynomial algebra, and the
$\Psi(x_i)$ and $e_l$ generate $B_{\mathrm{univ}}$).

Then $B_{\mathrm{univ}}$ is a commutative $R_{\mathrm{univ}}$-algebra with
unit $\sum_lb^le_l$ (by (i)–(iii)), $\Psi$ is a ring map, and
$\Psi(f_l)=e_l$ by (iv); hence
$Z_{\mathrm{univ}}:=\operatorname{Spec}(B_{\mathrm{univ}})\subseteq
X_{T_{\mathrm{univ}}}$ is a closed subscheme with
$\mathcal{O}_{Z_{\mathrm{univ}}}=B_{\mathrm{univ}}$ finite locally free of
rank $d$ over $R_{\mathrm{univ}}$ and with the $f_l|_Z$ spanning
$B_{\mathrm{univ}}$: an element of $F_W(T_{\mathrm{univ}})$. It is
universal: for $Z\in F_W(T)$, the images $f_l|_Z\in\mathcal{O}_Z$ form a
basis of the finite locally free $\mathcal{O}_T$-module $\mathcal{O}_Z$
(they span and $\mathcal{O}_Z$ has rank $d$); the structure constants
$c^m_{kl}$ of the basis, the coordinates $b^l$ of $1\in\mathcal{O}_Z$ and
the coordinates $b^l_i$ of the images of the $x_i$ give a morphism
$T\to T_{\mathrm{univ}}$ with
$Z\cong Z_{\mathrm{univ}}\times_{T_{\mathrm{univ}}}T$; uniqueness is clear
from the same data, so $F_W$ is representable by the affine scheme
$T_{\mathrm{univ}}$.

(2)(b) *Openness*: surjectivity of a morphism of finite locally free
modules is an open condition (Algebra, Lemma 10.79.4, [Tag
00O0](https://stacks.math.columbia.edu/tag/00O0)), so each inclusion
$F_W\subseteq\operatorname{Hilb}^d_{X/S}$ is representable by open immersions.

(2)(c) *Covering*: for a field-valued
$Z\in\operatorname{Hilb}^d_{X/S}(\kappa)$ the map
$A\otimes_R\kappa\to\mathcal{O}_Z$ is surjective and $\mathcal{O}_Z$ is a
$d$-dimensional $\kappa$-vector space, so there is a finite subset
$W\subseteq A$ of $d$ elements whose images in $\mathcal{O}_Z$ form a
basis; for a general $T$ and $t\in T$ use the same argument over
$\kappa(t)$ and Nakayama's lemma (Algebra, Lemma 10.20.1, [Tag
00DV](https://stacks.math.columbia.edu/tag/00DV)): $Z_V\in F_W(V)$ on an
open neighbourhood $V$ of $t$.

By [lem-pc-schemes-criterion] the functor $\operatorname{Hilb}^d_{Y/S}$ is
representable, hence so is $\operatorname{Hilb}^d_{X/S}$ for the original
affine $X$ (Step 1). This proves the affine claim.

*Step 5: openness of $F_U$ for $U\subseteq X$ affine.* For
$Z\in\operatorname{Hilb}^d_{X/S}(T)$ define
$$
B:=\bigl(Z\to T\bigr)\Bigl(\bigl(Z\to X_T\to X\bigr)^{-1}(X\setminus U)\Bigr).
$$
This is a closed subset of $T$: the set $(Z\to X)^{-1}(X\setminus U)$ is
closed in $Z$, and $Z\to T$ is closed (it is finite,
[def-pc-finite-locally-free]). Over the open $T_{Z,U}:=T\setminus B$ every
fibre of $Z$ maps into $U$, so the closed subscheme $Z_{T_{Z,U}}$ of
$X_{T_{Z,U}}$ has underlying space inside $U_{T_{Z,U}}$, hence is contained
in $U_{T_{Z,U}}$ (a closed subscheme whose underlying space lies in an open
subscheme is contained in that open subscheme); conversely if $T'\to T$ has
$Z_{T'}\subseteq U_{T'}$, then $T'$ avoids $B$. So $T'$ factors through
$T_{Z,U}$ iff $Z_{T'}\subseteq U_{T'}$: the inclusion
$F_U\subseteq\operatorname{Hilb}^d_{X/S}$ is representable by open immersions.

*Step 6: the $F_U$ cover; conclusion.* Let $T=\operatorname{Spec}(\kappa)$
with $\kappa$ a field, let $s\in S$ be the image of the point of $T$ and
let $Z\in\operatorname{Hilb}^d_{X/S}(T)$. The points of $Z$ map to points of
the fibre $X_s$ and there are at most $d$ of them ($Z$ is finite locally
free of rank $d$ over the field $\kappa$), so by the hypothesis of the
lemma there is an affine open $U\subseteq X$ containing them all; then the
underlying space of $Z$ lies in $U_T$, hence $Z\subseteq U_T$, i.e.
$Z\in F_U(T)$: the family $(F_U)_U$ covers $\operatorname{Hilb}^d_{X/S}$.
Combining Steps 3–6 with [lem-pc-schemes-criterion] gives representability
for affine $S$, and Step 2 extends it to arbitrary $S$.

Unresolved dependencies: def:sc-ample
