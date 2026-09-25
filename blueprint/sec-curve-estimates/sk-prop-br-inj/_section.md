+++
id = "sk-prop-br-inj"
kind = "section"
title = "Generic-point injection for the Brauer group"
order = 900
uses = ["sk-def-br", "sk-prop-divisor-gen"]
+++
*Proposition (sketch).*

Let $X$ be as in [sk-prop-divisor-gen] with function field
$k(X)$. Then (Grothendieck's residue sequence) the base change map
is injective:

$$
\Br(X)=H^2(X,\mathbb G_m)\hookrightarrow
H^2(\eta,\mathbb G_m)=\Br(k(X)).
$$

In particular this holds for $C$ a smooth curve.

## Proof

Take the long exact cohomology sequence of [sk-prop-divisor-gen].
The third term is a direct sum of the sheaves $i_{x*}\Z$, and
$H^1\big(X,i_{x*}\Z\big)=0$ for each $x$: in low degrees the Leray
spectral sequence for $i_x$ reduces this to
$H^1(\kappa(x),\Z)=\mathrm{Hom}_{\mathrm{cont}}(\mathrm{Gal} (\kappa(x)^{\mathrm{sep}}/\kappa(x)),\Z)$, which vanishes because a
continuous homomorphism from a profinite group to the discrete
torsion-free group $\Z$ has finite — hence trivial — image.
Cohomology commutes with the direct sum here (each point of $X$ has
a neighbourhood meeting only finitely many of the
$\overline{\{x\}}$, $x\in X^{(1)}$). Hence

$$
0=H^1\Big(X,\bigoplus_xi_{x*}\Z\Big)\to H^2(X,\mathbb G_m)
\to H^2(X,i_*\mathbb G_{m,\eta})
$$

is exact, so $H^2(X,\mathbb G_m)\hookrightarrow H^2(X,i_*\mathbb G_{m,\eta})$, and the Leray spectral sequence for
$i$ with $R^qi_*\mathbb G_{m,\eta}$ concentrated in degree $0$ in
the relevant range identifies the target with
$H^2(\eta,\mathbb G_m)=\Br(k(X))$. (In degrees $0$ and $1$ the same
sequence gives $H^0(X,\mathbb G_m)=k^\times$ for $X$ proper
connected over algebraically closed $k$ and
$H^1(X,\mathbb G_m)=\Pic(X)=\mathrm{Div}(X)/\mathrm{Princ}(X)$,
which is (P1) of [sk-def-pic].)

Uses: [sk-def-br], [sk-prop-divisor-gen]
