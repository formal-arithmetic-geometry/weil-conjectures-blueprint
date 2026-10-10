+++
id = "sec-abelian-varieties"
kind = "section"
title = "Abelian Varieties"
order = 416
uses = ["sec-nagata-compactification"]
+++
**Content.** For an abelian variety $A$ of dimension $g$ over a field $k$
of characteristic $p$, the section proves that $[n]$ is an isogeny of degree
$n^{2g}$ and derives the structure of torsion points and of the $\ell$-adic
Tate module. Projectivity gives an ample module, which is symmetrized to an
ample $\cN$ with $[-1]^*\cN\cong\cN$ ([sk-prop-av-symmetric-ample]); the
theorem of the cube ([sk-prop-av-cube]) then yields
$[n]^*\cN\cong\cN^{\otimes n^2}$ ([sk-prop-av-mult-n-pullback]). The rigidity
lemma ([sk-prop-av-rigidity]) makes $A$ commutative, so $[n]$ is a
homomorphism; it has finite fibres and is surjective, hence finite flat, and
comparing Hilbert degrees gives $\deg[n]=n^{2g}=\lvert A[n]\rvert$
([sk-prop-av-isogeny]). Since a connected finite group scheme has $p$-power
order, $A[n]$ is étale for $n$ prime to $p$ ([sk-prop-av-ntorsion-etale]);
with divisibility of $A(k)$ this gives $A[n](k)\cong(\Z/n\Z)^{2g}$ and
$T_\ell A\cong\Z_\ell^{2g}$ ([sk-prop-av-tate-rank]). The section also
records $p$-linear algebra in characteristic $p$ (Lang–Steinberg, fixed
points), used for Artin–Schreier arguments. The Jacobian itself is
constructed later, in §[sec-picard-framework].

**Key theorem.**

- Thm [sk-thm-av-final] (abelian-variety estimate): $[n]$ is a finite flat
  isogeny of degree $n^{2g}$, $A[n]$ is finite étale for $n$ prime to $p$
  with $A[n](\bar k)\cong(\Z/n\Z)^{2g}$ invariant under algebraically closed
  extension, $A(\bar k)$ is divisible, and $T_\ell A\cong\Z_\ell^{2g}$ for
  $\ell\ne p$. Used in §[sec-curve-estimates], §[sec-purity-real-sheaves],
  §[sec-fourier-transform].
- Prop [sk-prop-av-lang-steinberg] (Lang–Steinberg): for a $p$-linear
  $F$ on a finite-dimensional vector space over an algebraically closed
  field of characteristic $p$, $F-1$ is surjective. Used in
  §[sec-curve-estimates], §[sec-proper-base-change].
- Prop [sk-prop-av-pqf-finite] (proper and quasi-finite implies finite): a
  proper quasi-finite morphism of schemes is finite. Used in
  §[sec-picard-framework], §[sec-curve-estimates], §[sec-proper-base-change],
  §[sec-smooth-purity], §[sec-six-functors], §[sec-purity-real-sheaves],
  §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general].

**References.**

- Stacks Project, abelian varieties and group schemes: `03RO`, `0H2U`,
  `0B7Q`, `0BFC` (characterization); `0BF7`, `0B45` (projectivity); `0BF4`,
  `0BFE`, `0BFF` (theorem of the cube, $[n]^*$ of symmetric modules);
  `0BFD` (commutativity); `03RP`, `0BFG`, `0BFH` ($[n]$ is an isogeny,
  divisibility); `047N` (Cartier's theorem).
- Stacks Project, general inputs: `01UA` (flat morphisms are open), `0AH8`
  (finite-image locus), `0BUG` (global functions on proper geometrically
  connected reduced schemes), `04KV` (geometric connectedness), `02OG`
  (proper and quasi-finite implies finite); `0890`, `0BEV`, `0BEX`, `0B5X`
  (ampleness and degrees); `0ASV` ($p$-linear maps).
- J. Milne, *Abelian Varieties*, §I; D. Mumford, *Abelian Varieties*, §II.6
  (rigidity lemma).
- W. Waterhouse, *Introduction to Affine Group Schemes*, Ch. 11, and the
  Milnor–Moore structure theorem (connected finite group schemes have
  $p$-power order).
