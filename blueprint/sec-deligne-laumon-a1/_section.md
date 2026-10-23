+++
id = "sec-deligne-laumon-a1"
kind = "section"
title = "Deligne–Laumon on the Affine Line: Proof Sketch"
order = 3966
uses = ["sec-abelian-varieties", "sec-algebraic-groups-lie-algebras", "sec-curve-estimates", "sec-fourier-transform", "sec-nagata-compactification", "sec-picard-framework", "sec-poincare-duality", "sec-proetale-coefficients", "sec-proper-base-change", "sec-purity-real-sheaves", "sec-six-functors", "sec-six-functors-basics", "sec-smooth-base-change", "sec-smooth-purity", "sec-trace-formula", "sk-def-pbc-conventions", "sk-thm-br", "sk-thm-curveestimate"]
+++
**Content.** This section proves the bound
$\operatorname{wt}H_c^r(C,F)\le w+r$ for a pure lisse Weil sheaf $F$ of
weight $w$ on a smooth curve [sk-cor-wft-curve-upper]; on the affine
line it comes from the weight of the Fourier partner.

On a smooth curve the perverse t-structure has an elementary description
in terms of ordinary cohomology sheaves and punctual support
[sk-lem-wft-curve-heart], with simple objects the irreducible punctual
objects and the middle extensions $(j_*M)[1]$ [sk-lem-wft-curve-simples].
Using the extreme degrees of compact-support cohomology on an affine curve
[sk-l-dl-a1-endpoints], the Fourier transform on the affine line is
t-exact for it [sk-p-dl-a1-perverse]. Hence the transform of an
irreducible middle extension $(j_*M)[1]$ is again a middle extension
$(j'_*M')[1]$, provided $M$ is Fourier-generic, which holds when $M$ is
unramified at infinity and not geometrically constant
[sk-p-dl-a1-middle].

Let $M$ be Fourier-generic and pure of weight $w$. The Fourier transform
of the boundary sequence of $j_!M\subset j_*M$ [sk-p-dl-a1-correction]
realizes a twist of $M'$ as a quotient of a real sheaf, so $M'$ is pure
of some weight $v$ [sk-p-dl-a1-some-weight]. Plancherel and the boundary
correction for squared traces [sk-lem-wft-l2-middle] then determine
$v=w+1$ [sk-p-dl-a1-fourier-weight]. The stalk of the transform at the
origin is $H_c^1(\mathbf A^1,j_*M)$, which gives the bound in degree one
for one factor [sk-c-dl-a1-hc1]. Local boundary duality
[sk-i-dl-a1-local] makes the middle extension exact at a fixed pure
weight [sk-p-dl-a1-exact], so the bound passes through a composition
series, which proves the affine-line theorem [sk-thm-dl-a1-upper].

Constant extensions and a regular point moved to infinity
[sk-lem-wft-infinity-reduction], together with a finite generically
étale map to the line [sk-lem-wft-finite-map], extend the bound to
affine curves [sk-thm-wft-affine-curve-upper], to middle extensions on
curves [sk-thm-wft-curve-middle-upper] and to arbitrary smooth curves
[sk-cor-wft-curve-upper].

**Key theorems.**

- Thm [sk-thm-dl-a1-upper] (the weight bound on the affine line): for $F$
  lisse on a dense open $U_0\subset\mathbf A^1_{\mathbf F_q}$, pure of
  weight $w$ and unramified at infinity, $H_c^r(\mathbf A^1,j_*F)$ has
  weights at most $w+r$ for every $r$.
- Cor [sk-cor-wft-curve-upper] (the weight bound on a curve): for a pure
  lisse Weil sheaf $F$ of weight $w$ on a smooth geometrically connected
  curve $C_0$, $H_c^r(C,F)$ has weights at most $w+r$. Used in
  §[sec-deligne-laumon-general].

**References.**

- R. Kiehl and R. Weissauer, *Weil Conjectures, Perverse Sheaves and
  $\ell$-adic Fourier Transform* (the section follows its Deligne–Laumon
  argument for the affine line).
