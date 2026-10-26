+++
id = "sec-purity-real-sheaves"
kind = "section"
title = "Purity of Real Sheaves on Curves"
order = 3761
uses = ["sec-abelian-varieties", "sec-algebraic-groups-lie-algebras", "sec-curve-estimates", "sec-nagata-compactification", "sec-picard-framework", "sec-poincare-duality", "sec-proetale-coefficients", "sec-proper-base-change", "sec-six-functors", "sec-six-functors-basics", "sec-smooth-base-change", "sec-smooth-purity", "sec-trace-formula", "sk-def-picard-pic", "sk-thm-picard-main", "sk-prop-av-tate-rank", "sk-lem-curve-normalization", "sk-prop-curve-affine-kummer", "sk-thm-br", "sk-thm-curveestimate"]
+++
**Content.** For a smooth geometrically connected curve $C_0/\mathbf F_q$ and
an $\iota$-real lisse Weil $\overline{\mathbf Q}_\ell$-sheaf $\mathcal F$
(all local Frobenius polynomials real under $\iota$), every irreducible
constituent is punctually $\iota$-pure, of weight its determinant weight
$\operatorname{wt}_\iota(\det V)/\operatorname{rank}V$. This is Deligne's key
estimate from Weil II, here following Kiehl–Weissauer and the tex chapters
"Weil sheaves, weights and rank-one characters" and "Real sheaves and the first
weight estimate". After lattices and representations on a regular scheme
[sk-p-real-integral], the Weil-sheaf convention [sk-d-real-weil], weights
[sk-d-real-weights] and their elementary operations [sk-r-real-linear], the
route is: (1) the Jacobian shows that Frobenius has no fixed class in $H^1$
[sk-prop-wrp-h1-no-fixed], so invariant additive characters vanish
[sk-lem-wrp-additive], a rank-one character has finite geometric image
[sk-p-real-rankone] and is pure [sk-cor-wrp-rankone-pure], and determinants
have weights [sk-d-real-detweights], [sk-cor-walg-curve-calculus]; (2) the
determinant upper bound [sk-p-real-rankin]: the $L$-functions of even tensor
powers, controlled by $H^2_c$ as coinvariants [sk-lem-wrp-hc2] and by positive
Euler factors [sk-lem-wrp-positive-euler], bound all local weights by the
largest determinant weight; (3) applying this on an affine neighbourhood of
each point to exterior powers of the semisimplification and of its dual gives
purity [sk-p-real-purity]. The chapter ends with the boundary bound
[sk-p-real-semi] and the $L^2$ dictionary [sk-thm-wrp-l2-dictionary] used by
the Fourier argument.

**Key theorem.**

- Thm [sk-p-real-purity] (purity of real sheaves): every irreducible
  constituent $V$ of an $\iota$-real lisse Weil sheaf on a smooth
  geometrically connected curve over $\mathbf F_q$ is punctually $\iota$-pure
  of weight $\operatorname{wt}_\iota(\det V)/\operatorname{rank}V$, and every
  $\iota$-real lisse Weil sheaf is mixed.
- Thm [sk-p-real-rankone] and Cor [sk-cor-wrp-rankone-pure] (rank one): a
  rank-one lisse Weil sheaf has finite geometric image and is punctually
  $\iota$-pure of weight $2\log_q|\iota\chi(s)|$.
- Prop [sk-p-real-semi] (boundary semicontinuity): a punctual bound on $U_0$
  passes to $j_*\mathcal F$ on $X_0$; Cor [sk-cor-wrp-unramified-purity]: a
  lisse sheaf pure on a dense open is pure everywhere.
- Thm [sk-thm-wrp-l2-dictionary]: the growth of squared traces of a pure lisse
  sheaf on an affine curve equals its weight.

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
