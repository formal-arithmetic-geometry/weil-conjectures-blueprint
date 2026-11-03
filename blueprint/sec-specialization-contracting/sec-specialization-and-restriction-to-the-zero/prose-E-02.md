+++
id = "prose-E-02"
kind = "hidden"
title = "Specialization and restriction to the zero section"
order = 941
+++
Specialization to the normal cone is defined by nearby cycles on the
deformation to the normal cone, so for Verdier's theorem
(Theorem [sk-thm-tf-sp-zero-section]; see
[varshavsky05, §§1.3–1.4 and 3]) we first recall the facts about
nearby cycles that we need.

Nearby cycles move a complex from the generic fibre of a family to its
special fibre, where no restriction functor is available. The first
attempt is to extend by $Rj_*$ along the open generic fibre and restrict
by $i^*$ to the special fibre. This is wrong already for the trait
itself. The fraction field of $S$ is not separably closed: its absolute
Galois group is the inertia group, whose tame quotient is
$\prod_{\ell'\neq p}\mathbf Z_{\ell'}(1)$. Hence for $n$ invertible in $k$
the stalk of $R^1j_*(\mathbf Z/n)$ at the closed point is
$H^1(\eta,\mathbf Z/n)=\mathbf Z/n(-1)\neq0$, a class that comes from
the arithmetic of $\eta$ and not from the geometry of the family. Passing first to the geometric
generic fibre removes these Galois classes, and then the constant sheaf
specializes to itself, in degree zero (the first calculation below). The specialization
functor of Theorem [sk-thm-tf-sp-zero-section] and the comparison of trace
classes in Proposition [sk-prop-tf-trace-specialization] are built from
nearby cycles.

Let $S$ be the strict henselization of
$\operatorname{Spec}k[t]_{(t)}$, choose a geometric generic point
$\bar\eta$, and let $\mathcal Y\to S$ be separated of finite type.
We pull $\mathcal Y$ back to the integral closure of $S$ in
the chosen separable closure of its fraction field, and let $\bar i$
and $\bar j$ be the inclusions of the special fibre and of the
geometric generic fibre of this pullback. For $L$ on
$\mathcal Y_\eta$ with pullback $L_{\bar\eta}$ to the geometric generic
fibre, the geometric nearby cycles are

$$
R\Psi_{\mathcal Y}(L)=\bar i^{*}R\bar j_*L_{\bar\eta}.
$$

This defines a functor
$R\Psi_{\mathcal Y}:D^b_c(\mathcal Y_{\eta,\acute et},A)\to D(\mathcal Y_{s,\acute et},A)$. We suppress the inertia action, except
where invariants under the wild inertia group of a finite extension of
traits are taken below.

By the finiteness theorem for nearby cycles with torsion coefficients
([sga4-5], *Théorèmes de finitude*, §3;
[illusie94, §4.1, pp. 44–45]), $R\Psi_{\mathcal Y}$ takes
bounded constructible complexes of finite Tor dimension to bounded
constructible complexes of finite Tor dimension. We need the
preservation of finite Tor dimension for traces. We deduce that
$R\Psi_{\mathcal Y}$ preserves bounded constructible complexes in
general as follows.
The underlying torsion sheaves of $A$-linear nearby cycles are the
usual nearby cycles of torsion sheaves, and hence boundedness and
constructibility can be checked after forgetting the $A$-action. Since
bounded constructible complexes are stable under extensions, truncation
reduces us to one finite $\ell$-primary constructible sheaf, and then to
the graded pieces of its filtration by powers of $\ell$. These are
constructible $\mathbf F_\ell$-sheaves, which have finite Tor dimension
over $\mathbf F_\ell$, so the theorem applies to them.

For a morphism $g:\mathcal Y'\to\mathcal Y$ of separated
$S$-schemes of finite type, there is a base change map for pullback

$$
g_s^*R\Psi_{\mathcal Y}
\longrightarrow R\Psi_{\mathcal Y'}g_\eta^*,
$$

which is invertible for smooth $g$. For proper $g$
there is a base change map for proper direct image

$$
Rg_{s*}R\Psi_{\mathcal Y'}
\xrightarrow{\sim}R\Psi_{\mathcal Y}Rg_{\eta*}.
$$

These base change maps commute with composition and with the specialization
map defined below. Their invertibility follows from two base change
theorems for torsion coefficients. Proper base change [Stacks, Tag 095T](https://stacks.math.columbia.edu/tag/095T)
says that restriction to a fibre commutes with proper direct image.
Smooth base change [Stacks, Tag 0F09](https://stacks.math.columbia.edu/tag/0F09) (for sheaves [Stacks, Tag 0EYU](https://stacks.math.columbia.edu/tag/0EYU)) says that
pullback along a smooth map commutes with direct image along a qcqs
morphism when the coefficients are torsion of order invertible on the
base. If $g$ is proper, the two direct images on the generic fibres
agree because direct image is compatible with composition, and
$\bar i^*$ commutes with the proper direct image by proper base change.
If $g$ is smooth, we apply smooth base change to $R\bar j_*$, which is
direct image along a qcqs morphism, and restrict to the special fibre.
This is allowed because the coefficients are annihilated by a power of $\ell$, which is
invertible on $S$. The same base change maps appear in
[sga7-2], Exposé XIII, (2.1.7.1)–(2.1.7.3).

We also use two calculations for a finite $A$-module $M$. The first is
$R\Psi_S(M_{\eta})=M$. To see this, note that the integral closure
$\bar S$ of $S$ in the separable closure is strictly henselian, so the
stalk of $R\bar j_*M$ at its closed point is
$R\Gamma(\bar\eta,M)=M$. The second says that $H^r(\mathbf A^1_k,M)=0$ for
$r>0$ and $H^0(\mathbf A^1_k,M)=M$. This is the usual
calculation for the affine line with coefficients prime to the
characteristic, and to prove it we apply [Stacks, Tag 03RR](https://stacks.math.columbia.edu/tag/03RR) to the
compactification $\mathbf A^1\subset\mathbf P^1$, which has genus zero
and one point at infinity. Over the algebraically closed field $k$, the
cyclic constant coefficients are isomorphic to the corresponding roots
of unity, and every finite $M$ is a finite direct sum of these.
By truncation the two calculations extend to a bounded complex
$M^\bullet$ of finite $A$-modules, viewed as a constant complex:

$$
R\Psi_S(M^\bullet_\eta)\simeq M^\bullet,
\qquad R\Gamma(\mathbf A^1_k,M^\bullet_{\mathbf A^1_k})\simeq M^\bullet.
$$

For a separated $k$-scheme $Y$ of finite type, the constant family
$Y\times S$ has special fibre $Y$. For $L$ on $Y$, let $L_\eta$ be its
pullback to the generic fibre. Restricting the adjunction unit of
$\bar j$ on the pullback of $L$ to the special fibre, we get the
specialization map $\sigma_Y(L)$ below.
