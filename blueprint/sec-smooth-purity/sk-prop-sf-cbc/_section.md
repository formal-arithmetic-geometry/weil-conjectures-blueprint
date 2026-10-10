+++
id = "sk-prop-sf-cbc"
kind = "section"
title = "Compact-support base change"
order = 1517
uses = ["sk-def-av-jacobian"]
lean = ["AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekBaseChangeMap"]
+++
*Proposition (sketch).*

For $f:X\to Y$ admitting a compactification, $g:Y'\to Y$ arbitrary and a
Cartesian square whose base change $f':X'\to Y'$ is quasi-compact and admits a
compactification, the exchange transformation
$\operatorname{Ex}_!:Lg^*Rf_!\to Rf'_!Lg'^*$ of [sk-def-sf-exchanges] is an
isomorphism, natural in the coefficient complex and coherent for identity and
pasted squares, *with the following typing only*: (a) for a finite
commutative coefficient ring $\Lambda$ (in particular at a finite stage
$\Lambda=A_{E,n}$), on all of $D^+(X_{\Et},\Lambda)$, as functors
$D^+(X_{\Et},\Lambda)\to D^+(Y'_{\Et},\Lambda)$ on the small étale site,
and on the étale-origin complexes
$\nu_X^*D^+(X_{\Et},\Lambda)$ of the small pro-étale site
— hence in $\Dbc(Y',\Lambda)$ whenever
the two sides are bounded constructible; (b) at the stages $\mathcal O_E$,
$E$, $\Qlb$, only on $\Dbc$ of the pro-étale (adic) categories —
derived-complete $\mathcal O_E$-complexes whose reductions are of étale
origin, their rationalizations and the $\Qlb$-colimit, with
$\operatorname{Ex}_!$ the completed exchange
$\operatorname{Ex}^{\mathrm{comp}}_!$
— where it is an isomorphism in $\Dbc(Y',\Lambda)$, deduced from (a) by
derived limits over the finite reductions and then transported by
rationalization and scalar extension. No assertion is made for
the discrete non-torsion coefficients $\mathcal O_E,E,\Qlb$ on the small
étale site, where $\operatorname{Ex}_!$ is not an isomorphism in general
(for proper $f$ it is the exchange $\operatorname{Ex}_*$ of
[sk-prop-sf-comp-proper], for which [sk-thm-sf-package] (2) records the
same restriction). Whenever $\operatorname{Ex}_!$ is said to be an
isomorphism "at every coefficient stage", this typing is meant.

## Proof

The stages are proved separately. For finite coefficients on the étale site,
choose a compactification $f=rj$ with $j$ an open immersion and $r$ proper,
and base change it to a compactification $f'=r'j'$ of $f'$. Then
$\operatorname{Ex}_!$ is the exchange map computed with these
compactifications, followed by the comparison isomorphism identifying the
functor $Rr'_*j'_!$ with $Rf'_!$. The exchange for $j_!$ is an isomorphism
because extension by zero commutes with every base change, so the computed
exchange reduces to the base-change map $Lg^*Rr_*\to Rr'_*Lg''^*$ for the
proper morphism $r:Z\to Y$, where $g'':Z'=Z\times_YY'\to Z$ is the projection, which is an isomorphism on $D^+$ by proper base
change with torsion coefficients. The remaining stages are: the pro-étale site, for objects with an étale-origin witness;
derived-complete coefficients, with the completed exchange; $\Dbc(X,E)$; and
$\Dbc(X,\Qlb)$.
