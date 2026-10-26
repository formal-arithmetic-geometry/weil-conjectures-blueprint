+++
id = "sec-curve-estimates"
kind = "section"
title = "Curve Estimates"
order = 1243
uses = ["sec-abelian-varieties", "sec-nagata-compactification", "sec-picard-framework", "sec-proetale-coefficients", "sk-thm-picard-main", "sk-lem-abelian-seesaw", "sk-prop-av-isogeny", "sk-def-picard-pic", "sk-prop-av-tate-rank"]
+++
**Content.** For a smooth proper connected curve $C$ of genus $g$ over an
algebraically closed field $k$ and $n$ prime to $\operatorname{char}k$, this
section computes $H^*(C,\Z/n)$: it is $\Z/n$, $(\Z/n)^{2g}$, $\Z/n$ in degrees
$0,1,2$ and vanishes above. This is the curve input to proper base change. The
route: Tsen's theorem [lem-sc-tsen] makes $k(C)$ a $C_1$ field, so
$\Br(k(C))=0$; the divisor sequence [lem-sc-divisor-sequence-general] gives an injection
$\Br(C)\hookrightarrow\Br(k(C))$ [lem-sc-brauer-injectivity], hence $\Br(C)=0$
[sk-thm-br]. The Kummer sequence $0\to\mu_n\to\mathbb G_m\to\mathbb G_m\to0$
(exact by [lem-sc-kummer-exact]), with Hilbert 90 ($H^1(C,\mathbb G_m)=\Pic(C)$),
then gives $H^1(C,\mu_n)=\Pic(C)[n]$ [det-prop-h1] and
$H^2(C,\mu_n)=\Pic(C)/n$ [lem-sc-second-kummer-divisors]. The Jacobian and the structure of
torsion in abelian varieties turn these into $(\Z/n)^{2g}$ and $\Z/n$. A
generic-point argument based on Tsen bounds the cohomological dimension by $2$
[lem-sc-arbitrary-curve-cd], and by $1$ for affine curves [lem-sc-arbitrary-curve-cd]. Finally,
[sbc-thm-algebraically-closed-invariance] shows these groups do not change under extension of
the algebraically closed base field.

**Key theorem.**

- Thm [sk-thm-curveestimate] (curve estimate): for $C$ smooth proper connected
  of genus $g$ over $k=\bar k$ and $n$ prime to $\operatorname{char}k$,
  $H^0(C,\Z/n)=\Z/n$, $H^1(C,\Z/n)=(\Z/n)^{2g}$, $H^2(C,\Z/n)=\Z/n$, and
  $H^q(C,\Z/n)=0$ for $q\ge3$. Used in §[sec-proper-base-change],
  §[sec-smooth-purity], §[sec-purity-real-sheaves], §[sec-zeta-weil].
- Thm [sk-thm-br] ($\Br(C)=0$): a smooth proper curve over an algebraically
  closed field has trivial Brauer group $H^2(C_{\Et},\mathbb G_m)$. Used in
  §[sec-proper-base-change], §[sec-smooth-purity], §[sec-trace-formula],
  §[sec-purity-real-sheaves], §[sec-deligne-laumon-a1].
- Prop [lem-sc-arbitrary-curve-cd] (vanishing in high degrees): for any curve $C$ over
  $k=\bar k$ and any torsion sheaf with torsion prime to $\operatorname{char}k$,
  $H^q(C,F)=0$ for $q\ge3$. Used in §[sec-proper-base-change],
  §[sec-smooth-base-change], §[sec-smooth-purity], §[sec-six-functors],
  §[sec-trace-formula], §[sec-purity-real-sheaves], §[sec-fourier-transform],
  §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general].
- Prop [lem-sc-arbitrary-curve-cd] (affine-curve cohomological dimension): for an
  affine curve $C$ over $k=\bar k$ and every torsion sheaf $F$,
  $H^q(C_{\Et},F)=0$ for $q>1$. Used in §[sec-proper-base-change],
  §[sec-smooth-base-change], §[sec-smooth-purity], §[sec-purity-real-sheaves],
  §[sec-fourier-transform].

**References.**

- Stacks Project: `03RQ` (cohomology of curves, the curve estimate); `03SC`
  (cohomological dimension of affine curves, Theorem 59.83.10(2)).
- Stacks Project: `03P8`, `040M`, `040D` (Hilbert 90, $\mathbb G_m$-torsors and
  invertible modules); `03PK` (fppf Kummer sequence); `0A3J` (Artin–Schreier
  sequence).
- Stacks Project: `0BFL`, `02R3`, `0AZ0` (degree of principal divisors, degree
  under pullback and pushforward); `03QO` (cohomology of strictly local schemes).
