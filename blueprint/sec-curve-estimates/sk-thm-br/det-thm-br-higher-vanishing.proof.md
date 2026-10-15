+++
kind = "proof"
of = "det-thm-br-higher-vanishing"
+++
*Reduction to an integral curve.* The noetherian scheme $C$ is the finite
disjoint union of its connected components, and étale cohomology of a finite
disjoint union is the product of the cohomologies of the pieces. A connected
smooth $k$-scheme is normal and connected, hence integral, of dimension zero
or one. If it has dimension zero it is $\operatorname{Spec}k$, whose étale
cohomology vanishes in positive degrees for every abelian sheaf
([lem-weil-pbc-zero-dimensional-cohomology]). So we may assume $C$ integral
of dimension one, with generic point $\eta:\operatorname{Spec}K\to C$,
$K=k(C)$. It is regular, and its codimension-one points are its closed
points.

*The divisor sequence.* By [lem-sc-divisor-sequence-general] there is an
exact sequence of étale sheaves

$$
0\longrightarrow\mathbf G_m\longrightarrow\eta_*\mathbf G_{m,\eta}
\xrightarrow{\ \operatorname{div}\ }D\longrightarrow0,\qquad
D=\bigoplus_{x\in C\text{ closed}}i_{x*}\mathbf Z .
$$

*Step 1: $H^q(C,D)=0$ for $q\geq1$.* For a closed point $x$, the morphism
$i_x:\operatorname{Spec}k\to C$ is a closed immersion, so $i_{x*}$ is exact
(on geometric stalks it is the stalk on the point, or zero) and has the exact
left adjoint $i_x^{-1}$, hence preserves injectives. Thus
$H^q(C,i_{x*}\mathbf Z)=H^q(\operatorname{Spec}k,\mathbf Z)=0$ for $q\geq1$
by [lem-sc-point-z-cohomology]. Finite direct sums follow, and $D$ is the
filtered colimit of its finite partial sums; cohomology on the
quasi-compact quasi-separated scheme $C$ commutes with filtered colimits of
abelian sheaves ([lem-weil-pbc-cohomology-filtered-colimit]).

*Step 2: $R^b\eta_*\mathbf G_{m,\eta}=0$ for $b\geq1$.* The morphism $\eta$
is quasi-compact and quasi-separated, so the stalk of $R^b\eta_*$ at a
geometric point $\bar x$ of $C$ is the cohomology of the base change of
$\eta$ to the strict henselization (Stacks, Étale Cohomology, stalks of
higher direct images; the formula holds for arbitrary abelian sheaves). If
$\bar x$ lies over a closed point $x$, the strict henselization
$\mathcal O^{\mathrm{sh}}_{C,\bar x}$ is a discrete valuation ring (étale
localization preserves regularity and dimension,
[lem-sc-regular-dim1-dvr]), and its generic fibre over $C$ is the spectrum
of its fraction field $K^{\mathrm{sh}}_x$. Hence

$$
(R^b\eta_*\mathbf G_{m,\eta})_{\bar x}
=H^b(\operatorname{Spec}K^{\mathrm{sh}}_x,\mathbf G_m)=0\qquad(b\geq1)
$$

by [det-thm-br-field-units], $K^{\mathrm{sh}}_x$ being algebraic over $K$. If
$\bar x$ lies over $\eta$, the strict henselization is a separable closure
of $K$, and the stalk is $H^b(\operatorname{Spec}K^{\mathrm{sep}},\mathbf G_m)=0$.

*Step 3: $H^a(C,\eta_*\mathbf G_{m,\eta})=0$ for $a\geq1$.* The functor
$\eta_*$ has the exact left adjoint $\eta^{-1}$, so it sends injectives to
injectives, and the Grothendieck spectral sequence ([thm-sp-grothendieck])
$H^a(C,R^b\eta_*\mathbf G_{m,\eta})\Rightarrow
H^{a+b}(\operatorname{Spec}K,\mathbf G_m)$ is concentrated in the row
$b=0$ by Step 2. Hence
$H^a(C,\eta_*\mathbf G_{m,\eta})=H^a(\operatorname{Spec}K,\mathbf G_m)$,
which vanishes for $a\geq1$ by [det-thm-br-field-units] with $L=K$.

*Conclusion.* The long exact sequence of the divisor sequence contains

$$
H^{q-1}(C,D)\longrightarrow H^q(C,\mathbf G_m)\longrightarrow
H^q(C,\eta_*\mathbf G_{m,\eta}).
$$

For $q\geq2$ the left term vanishes by Step 1 and the right term by Step 3,
so $H^q(C_{\mathrm{ét}},\mathbf G_m)=0$. This is (Stacks, Tag 03RM).
