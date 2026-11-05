+++
id = "prose-E-02"
kind = "hidden"
title = "Specialization to the normal cone (1)"
order = 1624
+++
Let $S$ be the strict henselization of $\operatorname{Spec}k[t]_{(t)}$,
with generic point $\eta$. Nearby cycles move a complex from the generic
fibre of a family over $S$ to its special fibre. Since the special fibre
does not lie in the generic fibre, we cannot simply restrict. The obvious
attempt is to extend by $Rj_*$ along the open generic fibre and restrict
by $i^*$ to the special fibre. This fails already for $S$ itself,
because the fraction field of $S$ is not separably closed. Its absolute Galois group is the inertia group, whose tame quotient is
$\prod_{\ell'\neq p}\mathbf Z_{\ell'}(1)$. For $n$ invertible in $k$,
the stalk of $R^1j_*(\mathbf Z/n)$ at the closed point is therefore
$H^1(\eta,\mathbf Z/n)=\mathbf Z/n(-1)\neq0$. This class comes from
the arithmetic of $\eta$, not from the geometry of the family. Passing
first to the geometric generic fibre removes such Galois classes. After
this change, the constant sheaf specializes to itself, in degree zero, by
the first calculation below.

Both specialization to the normal cone and the comparison of trace classes in
Proposition [proposition-specialization-trace-class] are built from
nearby cycles on the deformation to the normal cone. The key input is
Verdier's theorem,
Theorem [theorem-verdier-s-theorem-specialization-zero]
(see [varshavsky05, §§1.3–1.4 and 3]).

The basic computation is that nearby cycles of a constant family
$Y\times S$ give back the complex we started with
(Lemma [lemma-nearby-cycles-constant-family]). We use it twice. It
makes the map $\tau_{X,Z}$ below land in $i^*L$, and it makes the
specialization of trace classes the identity when the fixed scheme does
not move (Corollary [corollary-specialization-when-fixed-point-scheme]).
Its proof uses only the definition of nearby cycles, their base change
maps and two calculations, which we now recall.

Choose a geometric generic point $\bar\eta$ of $S$, and let $\mathcal Y\to S$ be separated of finite type.
To define nearby cycles, we pull $\mathcal Y$ back to the integral closure of $S$ in
the chosen separable closure of its fraction field, and let $\bar i$
and $\bar j$ be the inclusions of the special fibre and of the
geometric generic fibre of this pullback.  Then, for $L$ on
$\mathcal Y_\eta$ with pullback $L_{\bar\eta}$ to the geometric generic
fibre, the geometric nearby cycles are

$$
R\Psi_{\mathcal Y}(L)=\bar i^{*}R\bar j_*L_{\bar\eta}.
$$

This defines a functor
$R\Psi_{\mathcal Y}:D^b_c(\mathcal Y_{\eta,\acute et},A)\to
D(\mathcal Y_{s,\acute et},A)$. We suppress the inertia action, except
where invariants under the wild inertia group of a finite extension of
traits are taken below.
