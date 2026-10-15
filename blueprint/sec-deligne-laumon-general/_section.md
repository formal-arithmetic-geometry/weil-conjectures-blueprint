+++
id = "sec-deligne-laumon-general"
kind = "section"
title = "Deligne–Laumon: Reduction to the Affine Line"
order = 3153
uses = ["sec-algebraic-groups-lie-algebras", "sec-deligne-laumon-a1", "sec-proetale-coefficients", "sec-purity-real-sheaves", "sec-six-functors", "sec-smooth-purity", "sec-trace-formula"]
+++
**Content.** This section proves Deligne's main theorem of Weil II in
Laumon's form: for a separated finite-type morphism $f_0$ over
$\mathbf F_q$, compact-support direct images send sheaves mixed of
weights $\le w$ to sheaves whose $R^r f_{0!}$ are mixed of weights
$\le w+r$ [sk-d-dl-general-weights]. The route is a reduction to the
affine-line estimate of §[sec-deligne-laumon-a1]. First that estimate is
freed from its condition at infinity on any open curve
$C_0\subset\mathbf P^1$ [sk-l-dl-general-open-line]. Base change gives the
punctual bound for a relative open affine line, and a real envelope
$F_0\oplus(F_0^\vee\otimes T_w)$, together with the mixedness of real
sheaves on any base [sk-i-dl-general-real] (by curve slicing from
§[sec-purity-real-sheaves]), upgrades it to mixedness
[sk-p-dl-general-relative-line]. The formal lemmas (open–closed
excision [sk-l-dl-general-excision], quasi-finite maps
[sk-l-dl-general-quasifinite], composition [sk-l-dl-general-composition]
and generic relative Noether normalization
[sk-l-dl-general-normalization]) then assemble the general sheaf theorem,
and a hypercohomology spectral sequence gives the derived version.

**Key theorem.**

- Thm [sk-thm-dl-general-sheaf] (Deligne–Laumon direct-image bound): for
  separated finite-type $f_0:X_0\to Y_0$ and $F_0$ mixed of weights
  $\le w$, each $R^rf_{0!}F_0$ is mixed of weights $\le w+r$. Used in
  §[sec-zeta-weil].
- Cor [sk-cor-dl-general-complex] (derived direct-image bound): if a
  bounded constructible Weil complex $K_0$ has weights $\le w$, so does
  $Rf_{0!}K_0$. Used in §[sec-zeta-weil].

**References.**

- Complete notes (`weil_conjectures_complete_notes.pdf`): Theorem 12.1 and
  §§12.2–12.6 (Lemmas 12.2–12.6, Warning 12.7); §9.4, Theorem 9.8 and
  Lemma 9.9 (real sheaves); §§11.2–11.3; Definition 8.3, Proposition 8.5.
- F. Charles and B. Poonen, *Bertini irreducibility theorems over finite
  fields*, Corollary 1.9.
- R. Kiehl and R. Weissauer, *Weil conjectures, perverse sheaves and
  $\ell$-adic Fourier transform*, Appendix B, Theorem 1 (irreducibility-preserving Bertini).
