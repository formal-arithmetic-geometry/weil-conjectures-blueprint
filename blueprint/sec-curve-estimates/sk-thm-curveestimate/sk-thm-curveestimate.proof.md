+++
kind = "proof"
of = "sk-thm-curveestimate"
+++
Pull back the Kummer sequence of $C_{\mathrm{ét}}$ ([sk-def-kummer]) by
$\nu_C^*$; it is the exact sequence of sheaves on $C_{\mathrm{proét}}$

$$
0\longrightarrow\mu_n\longrightarrow\mathcal G_m^{\mathrm{cl}}
\xrightarrow{(\cdot)^n}\mathcal G_m^{\mathrm{cl}}\longrightarrow0.
$$

Exactness is local ([sk-prop-kummer-exact]): for a unit $a$, the equation
$T^n=a$ defines an étale cover, since $n$ and $T$ are invertible. Global
units on the proper connected curve are $k^\times$, an $n$-divisible group.
[sk-thm-br] therefore turns the long exact sequence into

$$
H^1(C,\mu_n)=\operatorname{Pic}(C)[n],\qquad
H^2(C,\mu_n)=\operatorname{Pic}(C)/n,
$$

with all higher groups zero ([sk-prop-h1], [sk-prop-h2]).

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

Under an algebraically closed extension $k'/k$, $J$ and $J[n]$ base change to
the corresponding objects for $C_{k'}$. The map $J[n](k)\to J[n](k')$ is
bijective because a finite étale scheme over an algebraically closed field is
a finite disjoint union of copies of its spectrum; the same holds for roots
of unity. Pullback of a line bundle preserves degree. Hence the pullback maps
on cohomology themselves are isomorphisms. Finally [sk-prop-sf-comparison]
identifies these étale groups and maps with the pro-étale ones.
