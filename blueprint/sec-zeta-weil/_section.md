+++
id = "sec-zeta-weil"
kind = "section"
title = "Zeta Functions and the Weil Conjectures"
order = 3190
uses = ["sec-deligne-laumon-a1", "sec-deligne-laumon-general", "sec-poincare-duality", "sec-proper-base-change", "sec-purity-real-sheaves", "sec-six-functors", "sec-smooth-base-change", "sec-smooth-purity", "sec-trace-formula"]
+++
**Content.** For a smooth, proper, geometrically connected $X_0/\Fq$ of
dimension $d$, this section turns three cohomological inputs — the
Grothendieck–Lefschetz trace formula (§[sec-trace-formula]), Poincaré duality
(§[sec-poincare-duality]) and Deligne's weight estimate — into the Weil
conjectures for the zeta series $Z(X_0,T)$ of [sk-def-zeta]. The trace
formula gives the factorization $Z=\prod_i P_{i,\ell}^{(-1)^{i+1}}$ over
$\Ql$ ([sk-thm-tracetodeterminant]); the Euler product makes the
coefficients integral ([sk-prop-euler]), so the Hankel-rank criterion
[sk-prop-criterion] descends rationality from $\Ql$ to $\Q$
([sk-thm-rationality]). The upper bound on weights from
§[sec-deligne-laumon-general] becomes purity via duality
([sk-prop-smooth-proper-purity], [sk-input-weights]); root purity and weight
separation ([sk-prop-rootpurity], [sk-prop-separation]) together with
Fatou's lemma yield integral, $\ell$-independent factors
$P_i\in\Z[T]$ ([sk-thm-intfactors]) and the Riemann hypothesis
([sk-thm-rh]). Poincaré duality gives reciprocity of the factors
([sk-prop-reciprocity]), hence Betti symmetry ([sk-thm-betti]) and the
functional equation ([sk-thm-fe]).

**Key theorem.**

- Thm [sk-thm-weil1] (rationality): $Z(X_0,T)\in 1+T\Z[[T]]\cap\Q(T)$ and
  $Z(X_0,T)=\prod_{x\in|X_0|}(1-T^{\deg(x)})^{-1}$. Final result.
- Thm [sk-thm-weil2], [sk-thm-weil4] (integral factors and Betti numbers):
  there are unique $P_i\in\Z[T]$ with $P_i(0)=1$ equal to
  $\det(1-TF\mid H^i(X,\Ql))$ for every $\ell\ne p$ and
  $Z=\prod_{i=0}^{2d}P_i^{(-1)^{i+1}}$; their degrees $b_i=\dim H^i(X,\Ql)$
  satisfy $b_i=b_{2d-i}$, $b_0=b_{2d}=1$. Final results.
- Thm [sk-thm-weil3] and Cor [sk-cor-hasse] (Riemann hypothesis and
  Hasse–Weil bound): every reciprocal root $\alpha$ of $P_i$ is an algebraic
  integer with $|\tau(\alpha)|=q^{i/2}$ for all complex embeddings, hence
  $|N_1(X_0)-(q^d+1)|\le\sum_{i=1}^{2d-1}b_iq^{i/2}$ (for a curve of genus
  $g$, $|N_1-(q+1)|\le2g\sqrt q$). Final results.
- Thm [sk-thm-weil5] (functional equation):
  $Z(X_0,q^{-d}T^{-1})=\pm\,q^{d\chi/2}T^{\chi}Z(X_0,T)$ with
  $\chi=\sum_i(-1)^ib_i$. Final result.

**References.**

- None cited beyond the blueprint itself; the zeta-side arguments are
  formal power-series and linear algebra (Hankel-rank criterion, Fatou's
  lemma), with the geometric input taken from §[sec-trace-formula],
  §[sec-poincare-duality] and §[sec-deligne-laumon-general].
