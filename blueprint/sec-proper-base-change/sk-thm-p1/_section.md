+++
id = "sk-thm-p1"
kind = "section"
title = "Curve calculations $\\Rightarrow$ PBC($\\Pone$)"
order = 1107
uses = ["sk-def-br", "sk-def-conv", "sk-def-ia", "sk-def-pbc", "sk-thm-curveestimate", "sk-thm-iff"]
+++
*Theorem (sketch).*

For every scheme $S$, the projection $\Pone_S\to S$ satisfies
$\mathrm{PBC}$.

## Proof

It suffices ([sk-thm-iff]) to prove $\mathrm{IA}_r$ for the
projection, i.e. the vanishings of [sk-def-ia]. The proof depends
on the *curve calculations*, which we now exhibit.

*(i) The curve calculations.* For $C$ separated of finite type
over an algebraically closed $k$ with $\dim C\le1$ and $F$ torsion,
they are the eight assertions on
$(C_1)\ H^q(C_{\Et},F)=0\ (q>2);$  
$(C_2)\ C\ \text{affine}\ \Rightarrow\ H^q=0\ (q>1);$  
$(C_3)\ \operatorname{char}k=p,\ F\ p\text{-primary}\ \Rightarrow\ H^q=0\ (q>1);$  
$(C_4)\ F\ \text{constructible, prime to }p\ \Rightarrow\ H^q(C,F)\ \text{finite};$  
$(C_5)\ C\ \text{proper},\ F\ \text{constructible}\ \Rightarrow\ H^q(C,F)\ \text{finite};$  
$(C_6)\ k\subset k'\ \text{algebraically closed},\ F\ \text{prime to }p \Rightarrow\ H^q(C,F)\cong H^q(C_{k'},F);$  
$(C_7)\ C\ \text{proper}\ \Rightarrow\ H^q(C,F)\cong H^q(C_{k'},F) \text{ for all torsion }F;$  
$(C_8)\ a:U\hookrightarrow C\ \text{open}\ \Rightarrow\ a^*:H^2(C,F)\twoheadrightarrow H^2(U,a^{-1}F).$
(**Uses Thm [sk-thm-curveestimate]**) For the constant sheaf $\Fq$ on a smooth curve these are explicit
computations: $H^0(C,\Fq)=\Fq$, $H^1(C,\Fq)=\Fq^{2g}$ ($g$ the genus;
the ``Kummer route'' $\mathbf F_n\simeq\mu_n$), and
$H^q(C,\Fq)=0$ for $q\ge2$ (the étale cohomological dimension of a
curve is $1$); on an affine $U$ one has $H^q(U,j_!\Fq)=0$ for $q\ge2$,
and the analogues hold for $\Fp$ in characteristic $p$.  
From these,
by finiteness of the normalization, constructible and dense-open
reduction
($0\to j_!j^{-1}F\to F\to i_*i^{-1}F\to0$), locally constant
reduction (finite $r$-group filtration + trace splitting) and
dévissage, $(C_1)$–$(C_8)$ hold for every torsion $F$ and every
such $C$. In particular $(C_6)$/$(C_7)$ give the *invariance*
$H^q(C,F)\cong H^q(C_{k'},F)$ under algebraically closed extension
of the base field, and hence — passing to algebraic closures and
using that universal homeomorphisms do not change the étale site
— under *separably closed* extension $k\subset k'$.

*(ii) Strictly henselian base.* For $A$ strictly henselian
with closed point $s$, the degree-zero comparison
$\Gamma(Z,F)\cong\Gamma(Z_s,F|_{Z_s})$ ($Z$ proper over $A$; Stein's
connectedness), applied through the Mayer–Vietoris sequence to the
two affine opens of $\Pone_A$, kills $H^q$ of an injective for
$q\ge2$; the remaining class in $H^1$ is killed by the
constructible/finite-étale machinery (Gabber's affine comparison +
torsor lifting over a proper henselian pair). Hence
$H^q(\Pone_A,F)\cong H^q(\Pone_s,F|)$ for every torsion $F$. (This
comparison is where the curve calculations of (i) enter for the
constant sheaf on the closed fibre $\Pone_s$.)

*(iii) Arbitrary $S$.* The stalk of the exchange morphism at a
geometric point $\bar t\to T$ (over $\bar s\to S$) is the canonical
pullback $H^q(\Pone_{\kappa(\bar s)},F)\to H^q(\Pone_{\kappa(\bar t)},F)$ between separably closed fields, an
isomorphism by the invariance obtained in (i) (the curve
calculations). So the exchange map is an isomorphism at every
geometric stalk: $\mathrm{IA}_r$ holds for the projection (geometric
stalks are conservative), and [sk-thm-iff] converts it into
$\mathrm{PBC}$.

Uses: [sk-def-conv], [sk-def-ia], [sk-def-pbc], [sk-thm-curveestimate], [sk-thm-iff]
