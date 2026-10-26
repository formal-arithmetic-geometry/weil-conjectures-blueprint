+++
id = "sec-deligne-laumon-general"
kind = "section"
title = "Deligne–Laumon: Reduction to the Affine Line"
order = 4052
uses = ["sec-abelian-varieties", "sec-algebraic-groups-lie-algebras", "sec-curve-estimates", "sec-deligne-laumon-a1", "sec-nagata-compactification", "sec-proetale-coefficients", "sec-proper-base-change", "sec-purity-real-sheaves", "sec-six-functors", "sec-six-functors-basics", "sec-smooth-base-change", "sec-smooth-purity", "sec-trace-formula"]
+++
**Content.** This section proves that $Rf_!$ does not increase
weights (Deligne's main theorem of Weil II in Laumon's form): for a
separated finite-type morphism $f_0$ over $\mathbf F_q$, compact-support
direct images send $D_{\le w}$ to $D_{\le w}$, in the weight conventions
of [sk-d-real-weights]. It extends the bound on curves
[sk-cor-wft-curve-upper] to arbitrary separated morphisms of finite
type. The curve bound controls the eigenvalues on each fibre; a finite
mixed filtration of the direct image comes from reality. Finite and
quasi-finite direct images are exact and preserve weights
[sk-l-dl-general-quasifinite]. A finite matrix witness for absolute
irreducibility [sk-lem-wgen-finite-witness] and a Bertini curve through
prescribed points preserving a finite cover [sk-lem-wgen-bertini-cover]
give curves on which given geometrically irreducible sheaves stay
irreducible [sk-cor-wgen-bertini-irreducible]; with the geometric
constituents of [sk-lem-wgen-geometric-constituents] and real purity on
curves from §[sec-purity-real-sheaves], every real constructible sheaf
is mixed [sk-i-dl-general-real]. For a relative affine curve, the trace
formula separates the two cohomological factors of the real envelope of
a pure sheaf; hence each direct-image sheaf is real, therefore mixed,
and the fibrewise bound with [sk-lem-wgen-punctual-cutoff] bounds its
weights [sk-p-dl-general-relative-line]. Localization for open and
closed pieces gives the relative affine line
[sk-prop-wgen-relative-line], and relative Noether normalization
[sk-l-dl-general-normalization] reduces the general sheaf theorem to it.
A hypercohomology spectral sequence gives the derived version.

**Key theorem.**

- Thm [sk-thm-dl-general-sheaf] (direct image of a mixed sheaf): for
  separated finite-type $f_0:X_0\to Y_0$ and $F_0$ mixed of weights
  $\le w$, each $R^rf_{0!}F_0$ is mixed of weights $\le w+r$. Used in
  §[sec-zeta-weil].
- Thm [sk-cor-dl-general-complex] (weights of $Rf_!$):
  $Rf_!D_{\le w}(X_0)\subset D_{\le w}(Y_0)$; in particular
  $H_c^n(X,K)$ has weights $\le w+n$ for $K\in D_{\le w}(X_0)$. Used in
  §[sec-zeta-weil].

**References.**

- Complete notes (`weil_conjectures_complete_notes.pdf`): Theorem 12.1 and
  §§12.2–12.6 (Lemmas 12.2–12.6, Warning 12.7); §9.4, Theorem 9.8 and
  Lemma 9.9 (real sheaves); §§11.2–11.3; Definition 8.3, Proposition 8.5.
