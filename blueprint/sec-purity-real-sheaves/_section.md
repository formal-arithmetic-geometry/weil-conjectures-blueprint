+++
id = "sec-purity-real-sheaves"
kind = "section"
title = "Purity of Real Sheaves on Curves"
order = 2574
uses = ["sec-abelian-varieties", "sec-algebraic-groups-lie-algebras", "sec-curve-estimates", "sec-nagata-compactification", "sec-picard-framework", "sec-poincare-duality", "sec-six-functors", "sec-smooth-purity", "sec-trace-formula", "sk-def-av-jacobian", "sk-def-av-pic", "sk-thm-av-final"]
+++
**Content.** For a smooth geometrically connected curve $C_0/\mathbf F_q$ and
an $\iota$-real lisse Weil $\overline{\mathbf Q}_\ell$-sheaf $\mathcal F$
(all local Frobenius polynomials real under $\iota$), every irreducible
constituent is punctually $\iota$-pure, of weight its determinant weight
$\operatorname{wt}_\iota(\det V)/\operatorname{rank}V$. This is Deligne's key
estimate from Weil II, here following Kiehl–Weissauer. After setting up Weil
sheaves as representations of $W(C_0)$ [sk-i-real-sheaves] and local weights
[sk-d-real-weights], the route is: (1) rank-one purity [sk-p-real-rankone]: a
rank-one character has finite geometric image (via the Jacobian on proper
curves and a logarithm argument on open ones), hence is pure; (2) the
Rankin–Selberg bound [sk-p-real-rankin]: the $L$-functions of
$\mathcal F^{\otimes 2m}$, controlled by $H^2_c$ as coinvariants, show all
local weights are at most the largest determinant weight; (3) applying this
to exterior powers of the semisimplification, block by block in
[sk-d-real-detweights], plus the pure-determinant identity, gives purity on an
affine open [sk-p-real-purity]; (4) semi-continuity [sk-p-real-semi] extends
purity over the missing points.

**Key theorem.**

- Prop [sk-p-real-purity] (purity of real sheaves): every irreducible
  constituent $V$ of an $\iota$-real lisse Weil sheaf on a smooth
  geometrically connected curve over $\mathbf F_q$ is punctually $\iota$-pure
  of weight $\operatorname{wt}_\iota(\det V)/\operatorname{rank}V$. Used in
  §[sec-deligne-laumon-a1], §[sec-deligne-laumon-general], §[sec-zeta-weil].
- Prop [sk-p-real-rankone] (rank-one purity): a rank-one lisse Weil sheaf
  has finite geometric image and is punctually $\iota$-pure of weight
  $2\log|\iota\chi(\gamma)|/\log q$. Used in §[sec-deligne-laumon-a1],
  §[sec-deligne-laumon-general].
- Prop [sk-p-real-semi] (semi-continuity of weights): if $\mathcal F$ has
  weights $\le w$ on $U_0$ then so does $j_*\mathcal F$ on $C_0$; hence a
  lisse sheaf pure of weight $w$ on a dense open is pure of weight $w$
  everywhere. Used in §[sec-deligne-laumon-a1],
  §[sec-deligne-laumon-general], §[sec-zeta-weil].

**References.**

- P. Deligne, *La conjecture de Weil. II*, Publ. Math. IHES 52 (1980):
  1.3.4–1.3.13 (rank one and monodromy), 1.4.1–1.4.7 (top cohomology),
  1.5.1–1.5.3 (Rankin–Selberg and real purity), 1.8.1 (semi-continuity).
- R. Kiehl, R. Weissauer, *Weil Conjectures, Perverse Sheaves and $\ell$-adic
  Fourier Transform* (the main source of the section's argument).
- SGA 1, Exposé V, §§4–7 (Galois categories, étale fundamental group);
  SGA 4 (cohomology and duality); SGA 4½ (trace formula).
- J. S. Milne, *Jacobian Varieties*; *Algebraic Groups* (2017).
- Stacks Project: `00TV` (regular implies smooth over a perfect field);
  `033C` (normality ascends along étale maps); `00OY`, `00OX`, `051M`, `00OK`
  (Noether normalization and dimension of integral extensions).
