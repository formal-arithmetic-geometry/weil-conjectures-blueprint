+++
id = "prop-av-kummer-tate"
kind = "theorem"
title = "Kummer identifies curve cohomology with the Jacobian Tate module"
order = 600
uses = ["def-av-pic", "def-sc-jacobian", "def-wf-abelian-tate-module", "lem-sc-ntorsion-etale", "prop-av-jacobian"]
tags = ["latex:proposition"]
+++
Let $C$ be a smooth projective geometrically connected curve over a
field $k$, let $\bar k$ be an algebraic closure, let $J$ be the
Jacobian of $C_{\bar k}$ ([prop-av-jacobian]) and let
$\ell\ne\operatorname{char}k$. Then there are natural,
$\operatorname{Gal}(\bar k/k)$-equivariant, transition-compatible
isomorphisms

$$
H^1(C_{\bar k},\mu_{\ell^n})\xrightarrow{\ \sim\ }J[\ell^n](\bar k)
\qquad(n\ge1),
$$

and passing to the inverse limit, with the degree-one Poincaré
pairing ([sec-poincare-duality]),

$$
\varprojlim_nH^1_{\Et}(C_{\bar k},\Z/\ell^n)
\xrightarrow{\ \sim\ }\Hom_{\Z_\ell}(T_\ell J,\Z_\ell).
$$

## Proof

The Kummer sequence $1\to\mu_{\ell^n}\to\gm\xrightarrow{\ell^n}\gm\to1$
on $C_{\bar k}$ has long exact cohomology beginning
$H^0(\gm)\xrightarrow{\ell^n}H^0(\gm)\to H^1(\mu_{\ell^n})\to H^1(\gm)\xrightarrow{\ell^n}H^1(\gm)$; since
$H^0(C_{\bar k},\gm)=\bar k^\times$ is divisible and
$H^1(C_{\bar k},\gm)=\Pic(C_{\bar k})$, this gives
$H^1(C_{\bar k},\mu_{\ell^n})\cong\Pic(C_{\bar k})[\ell^n]$. An
$\ell^n$-torsion invertible module has degree $0$
($\ell^n\deg\cL=0$), so the right side is $\Pic^0(C_{\bar k})[\ell^n] =J[\ell^n](\bar k)$ by [prop-av-jacobian]; the identification is
induced by the representing isomorphism, hence canonical and Galois
equivariant. The transition $\mu_{\ell^{n+1}}\to\mu_{\ell^n}$,
$z\mapsto z^\ell$, corresponds to multiplication by $\ell$ on
$J[\ell^n]$, so the finite-level isomorphisms form the inverse system
defining $T_\ell J$ ([def-wf-abelian-tate-module]); by [lem-sc-ntorsion-etale]
each level is $(\Z/\ell^n\Z)^{2g}$, and the dual form
$\varprojlim H^1(C_{\bar k},\Z/\ell^n)\cong \Hom_{\Z_\ell}(T_\ell J,\Z_\ell)$ follows from the perfect degree-one
pairing $H^1(C_{\bar k},\Z/\ell^n)\times H^1(C_{\bar k},\Z/\ell^n(1))\to\Z/\ell^n$ ([sec-poincare-duality]).

Uses: [def-sc-jacobian], [def-av-pic], [def-wf-abelian-tate-module], [prop-av-jacobian], [lem-sc-ntorsion-etale]
