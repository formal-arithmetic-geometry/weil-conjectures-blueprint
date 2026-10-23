+++
kind = "proof"
of = "sk-thm-curveestimate"
+++
Pull back the Kummer sequence of $C_{\mathrm{ét}}$ ([def-sc-kummer-sequence]) by
$\nu_C^*$; it is the exact sequence of sheaves on $C_{\mathrm{proét}}$

$$
0\longrightarrow\mu_n\longrightarrow\mathcal G_m^{\mathrm{cl}}
\xrightarrow{(\cdot)^n}\mathcal G_m^{\mathrm{cl}}\longrightarrow0.
$$

Exactness is local ([lem-sc-kummer-exact]): for a unit $a$, the equation
$T^n=a$ defines an étale cover, since $n$ and $T$ are invertible. Global
units on the proper connected curve are $k^\times$, an $n$-divisible group.
[sk-thm-br] therefore turns the long exact sequence into

$$
H^1(C,\mu_n)=\operatorname{Pic}(C)[n],\qquad
H^2(C,\mu_n)=\operatorname{Pic}(C)/n,
$$

with all higher groups zero ([det-prop-h1], [lem-sc-kummer-les]).

The degree sequence of [sk-cor-picard-degree] is

$$
0\longrightarrow J(k)\longrightarrow\operatorname{Pic}(C)
\xrightarrow{\deg}\Z\longrightarrow0.
$$

Multiplication by $n$ on $J(k)$ is surjective, with kernel $J[n](k)$, and
$J[n]$ is finite étale of rank $n^{2g}$ ([sk-cor-jacobian-torsion]). The
snake lemma gives the two identifications asserted above, and $J[n](k)$ is
noncanonically isomorphic to $(\Z/n)^{2g}$. This is the calculation of
(Stacks, Tag 03RQ).

Under an algebraically closed extension $k'/k$, the schemes $J$ and $J[n]$
base change to the corresponding objects for $C_{k'}$, and the map
$J[n](k)\to J[n](k')$ is bijective by [sk-cor-jacobian-torsion]. The same
argument applies to the finite étale scheme $\mu_n$, and pullback of line
bundles preserves the degree. Hence the pullback maps on cohomology are
isomorphisms. Finally [sk-prop-sf-comparison]
identifies these étale groups and maps with the pro-étale ones.
