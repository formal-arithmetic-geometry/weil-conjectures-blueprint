+++
id = "sec-zeta-weil"
kind = "section"
title = "Zeta Functions and the Weil Conjectures"
order = 4095
uses = ["sec-abelian-varieties", "sec-curve-estimates", "sec-deligne-laumon-general", "sec-nagata-compactification", "sec-picard-framework", "sec-poincare-duality", "sec-proetale-coefficients", "sec-proper-base-change", "sec-purity-real-sheaves", "sec-six-functors", "sec-six-functors-basics", "sec-smooth-base-change", "sec-smooth-purity", "sec-trace-formula", "sk-thm-br", "sk-thm-curveestimate"]
+++
**Content.** For a smooth proper $X_0/\Fq$ of pure dimension $d$, this
section proves the purity of its cohomology and the Weil conjectures. For
purity, the weight bound for $Rf_!$ (§[sec-deligne-laumon-general]) and
Frobenius-equivariant Poincaré duality (§[sec-poincare-duality]) give opposite
inequalities for each eigenvalue ([sk-prop-smooth-proper-purity],
[sk-input-weights]). Rationality of the zeta function and the determinant
formula over $\Ql$ come from the trace formula ([sk-cor-tf-point-counting]),
and the functional equation from Poincaré duality
([sk-cor-tf-functional-equation]), both in §[sec-trace-formula]. Since the
Taylor coefficients of $Z(X_0,T)$ are integers, it has a unique reduced
fraction of integral polynomials with constant coefficients one
([sk-prop-criterion], [sk-lem-wweil-integer-rationality]), and purity
separates the cohomological factors by degree, which yields integral,
$\ell$-independent factors $P_i\in\Z[T]$ whose reciprocal roots are
$q$-Weil numbers ([sk-thm-intfactors]).

**Key theorem.**

- Thm [sk-thm-weil-final] (the Weil conjectures): for geometrically connected
  $X_0$, $Z(X_0,T)=\prod_{i=0}^{2d}P_i^{(-1)^{i+1}}$
  with $P_i\in\Z[T]$, $P_i(0)=1$; every reciprocal root $\alpha$ of $P_i$ has
  $|\tau(\alpha)|=q^{i/2}$ for all complex embeddings; $b_i=\deg P_i$
  satisfies $b_i=b_{2d-i}$ and is independent of $\ell$, $P_0=1-T$ and
  $P_{2d}=1-q^dT$; and
  $Z(X_0,q^{-d}T^{-1})=\pm\,q^{d\chi/2}T^{\chi}Z(X_0,T)$ with
  $\chi=\sum_i(-1)^ib_i$. Final result.
- Cor [sk-cor-hasse] (point-count estimates): for geometrically connected
  $X_0$ and $d\ge1$,
  $|\#X_0(\mathbf F_{q^m})-(1+q^{dm})|\le\sum_{i=1}^{2d-1}b_iq^{mi/2}$; for a
  curve of genus $g$, $|\#X_0(\mathbf F_{q^m})-(1+q^m)|\le2gq^{m/2}$. Final
  result.

**References.**

- None cited beyond the blueprint itself; the zeta-side arguments are
  formal power-series and linear algebra (Hankel rank, the integral reduced
  fraction), with the geometric input taken from §[sec-trace-formula],
  §[sec-poincare-duality] and §[sec-deligne-laumon-general].
