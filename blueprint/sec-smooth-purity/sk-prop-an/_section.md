+++
id = "sk-prop-an"
kind = "proposition"
title = "$\\Aaf^1\\Rightarrow\\Aaf^n$: the model purity"
order = 1962
uses = ["sk-def-purity-conv", "sk-lem-sf-mate", "sk-prop-a1", "sk-prop-a1-inv", "sk-prop-a1-kummer", "sk-prop-cd", "sk-prop-h2", "sk-prop-sf-cbc", "sk-prop-sf-open-closed-triangle", "sk-thm-properbasechange"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineSpaceZero", "AlgebraicGeometry.Etale.isIso_supportedClassMap_kummerBoundaryProduct_coord"]
tags = ["sketch"]
+++
In the conventions of [sk-def-purity-conv], let $B$ be separated finite
type, $\pi=p_c:\Aaf^c_B\to B$ the projection and $z:B\hookrightarrow\Aaf^c_B$
the zero section.

- **(i)** *The $Rz^{!}$-form: the Thom class.*

$$
Rz^{!}\Lambda_{\Aaf^c_B}(c)[2c]\ \cong\ \Lambda_B,
$$

i.e. $Rz^{!}\Lambda_{\Aaf^c_B}\cong\Lambda_B(-c)[-2c]$, by a canonical
base-change compatible isomorphism whose generator is the fundamental class
of the zero section, the cup product with supports
$\partial\kappa(t_1)\cup\cdots\cup\partial\kappa(t_c)$ of the Kummer
boundaries of the coordinates. More generally, for a vector bundle
$\pi:E\to Z$ of rank $c$ with zero section $z$ there is a *Thom class*

$$
\mathrm{th}_E:\ \Lambda_Z\ \xrightarrow{\ \sim\ }\ Rz^{!}\Lambda_E(c)[2c],
$$

which restricts to the previous one in any étale trivialization of $E$.
- **(ii)** *The $R\pi^{!}$-form: affine-space and vector-bundle
purity.* For every $K\in D^b_{ctf}(B,\Lambda)$ there is a canonical
isomorphism

$$
\gamma_{\pi,K}:\ L\pi^{*}K(c)[2c]\ \xrightarrow{\ \sim\ }\ R\pi^{!}K,
$$

natural in $K$ and compatible with arbitrary base change in $B$; in
particular $\omega_\pi=R\pi^{!}\Lambda_B\cong\Lambda_{\Aaf^c_B}(c)[2c]$.
It is the transpose under $R\pi_!\dashv R\pi^{!}$ of the *integration
map*

$$
R\pi_!L\pi^{*}K(c)[2c]\ \cong\ K\otimes^{\mathbb L}R\pi_!\Lambda_{\Aaf^c_B}(c)[2c]
\ \xrightarrow{\ 1_K\otimes\int_\pi\ }\ K,
$$

where $\int_\pi:R\pi_!\Lambda_{\Aaf^c_B}(c)[2c]\xrightarrow{\sim}\Lambda_B$ is
the affine-space trace of Step 5 below and the first map is the projection
formula. Under $\Aaf^{c+e}_B=\Aaf^c_{\Aaf^e_B}$ it satisfies the composition
law
$\gamma_{p_{c+e},K}=c_{p_e,p_c}^{-1}\circ\gamma_{p_c,Rp_e^{!}K}\circ
Lp_c^{*}(\gamma_{p_e,K})(c)[2c]$, with $c_{g,f}:R(gf)^{!}\cong Rf^{!}Rg^{!}$
the composition isomorphism, and it is symmetric under permutations of the
coordinates (every Koszul sign is $+1$, all shifts being even). More
generally, for a vector bundle $\pi:E\to Z$ of rank $c$ there is a canonical
isomorphism $\gamma_{\pi,K}:L\pi^{*}K(c)[2c]\xrightarrow{\sim}R\pi^{!}K$,
compatible with base change, which is the affine-space one on every étale
trivialization of $E$; in particular $\omega_\pi\cong\Lambda_E(c)[2c]$
(*vector-bundle purity*).
- **(iii)** *Normalization: the two forms agree along the zero
section.* Since $\pi z=\mathrm{id}$, the composition isomorphism gives
$Rz^{!}R\pi^{!}\cong\mathrm{id}$, and for every vector bundle $\pi:E\to Z$
(with $Z=B$ for $E=\Aaf^c_B$) the composite

$$
\Lambda_Z\ \xrightarrow{\ \mathrm{th}_E\ }\ Rz^{!}\Lambda_E(c)[2c]
\ \xrightarrow{\ Rz^{!}(\gamma_{\pi,\Lambda})\ }\ Rz^{!}R\pi^{!}\Lambda_Z
\ \cong\ \Lambda_Z
$$

is the identity. Equivalently, $\int_\pi$ sends the *class of the zero
section* — the image of $\mathrm{th}_E$ under
$H^0(Z,Rz^{!}\Lambda_E(c)[2c])=H^{2c}_{z(Z)}(E,\Lambda(c))\to
H^0(Z,R\pi_!\Lambda_E(c)[2c])$, which for $E=\Aaf^c_B$ is
$\partial\kappa(t_1)\cup\cdots\cup\partial\kappa(t_c)$ — to $1$. Thus (i)
is what (ii) becomes along the zero section, and the generator of (i) is the
normalization of (ii).
