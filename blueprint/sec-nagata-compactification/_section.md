+++
id = "sec-nagata-compactification"
kind = "section"
title = "Nagata Compactification"
order = 0
+++
**Content.** Every separated finite-type morphism $f\colon X\to S$ to a
qcqs scheme factors as a quasi-compact open immersion followed by a proper
morphism. The proof starts from a toolkit of admissible blow-ups, strict
transforms and scheme-theoretic closures [sk-lem-nagata-sketch-blowups],
[sk-lem-nagata-sketch-closure]. Deligne–Conrad elimination of indeterminacy
[sk-lem-nagata-sketch-elimination], resting on Zariski's Main Theorem, extends
partial maps after a blow-up. This yields common modifications and proper
graph extensions, and it lets one separate boundary closures. With these, two
compactifiable opens $U_1,U_2$ with dense overlap are prepared so that the
closure of $V_1\times_U V_2$ meets no bad boundary product, and a
dense-source valuative criterion then makes the glued scheme proper
[sk-thm-nagata-sketch-two-open]. Induction over a finite affine cover, with
ZMT giving compactifiable affine pieces [sk-lem-nagata-sketch-affine-cover],
gives the Noetherian case of [sk-thm-nagata-compactification]; absolute
approximation and a separated finite-presentation envelope remove the
Noetherian hypothesis. Chow's lemma over a qcqs base
[sk-thm-chow-projective] follows from the Noetherian one by the same
approximation. Finally the compactifications of $f$ form a cofiltered category,
compatible with base change [sk-prop-nagata-sketch-comp-category].

**Key theorem.**

- Thm [sk-thm-nagata-compactification] (Nagata compactification): for $S$
  qcqs, every separated finite-type $f\colon X\to S$ factors as
  $f=p\circ j$ with $j$ a quasi-compact, scheme-theoretically dense open
  immersion and $p$ proper. Used in §[sec-smooth-purity], §[sec-six-functors],
  §[sec-trace-formula], §[sec-purity-real-sheaves].
- Prop [sk-prop-nagata-sketch-comp-category] (compactification category): the
  compactifications of $f$ form a cofiltered category, with common refinements
  and equalizing refinements, and this structure is compatible with base
  change. Used in §[sec-abelian-varieties], §[sec-picard-framework],
  §[sec-smooth-purity], §[sec-six-functors], §[sec-trace-formula],
  §[sec-poincare-duality], §[sec-algebraic-groups-lie-algebras],
  §[sec-purity-real-sheaves], §[sec-deligne-laumon-a1],
  §[sec-deligne-laumon-general], §[sec-zeta-weil].
- Cor [sk-cor-nagata-sketch-proper-extension] (extension to a proper target):
  an $S$-map $U\to Y$ from a dense quasi-compact open $U\subseteq X$ to a
  proper $Y$ extends to $X'\to Y$ after a $U$-admissible blow-up. Used in
  §[sec-proper-base-change], §[sec-smooth-purity].
- Thm [sk-lem-nagata-sketch-elimination] (elimination of indeterminacy), with
  Zariski's Main Theorem among its ingredients: a separated, finite-type,
  quasi-finite morphism factors as a quasi-compact open immersion followed by
  a finite morphism, and a quasi-affine scheme over $S$ immerses into some
  $\mathbb A^n_S$. Used in §[sec-abelian-varieties],
  §[sec-proper-base-change], §[sec-deligne-laumon-general], §[sec-zeta-weil].

**References.**

- Stacks Project: `0F41` (Nagata compactification); `081S`, `0F3Y`, `0F3X`,
  `0F3Z`, `0F3W` (admissible blow-ups, strict transforms and the
  compactification lemmas); `0894` (valuative criterion with dense source).
- Stacks Project: `02LR`, `03GW`, `05F7`, `0F2N` (Zariski's Main Theorem);
  `04II` (quasi-affine schemes immerse into affine space).
- Stacks Project: `01ZX` (affine opens containing finitely many points);
  `01ZA`, `01ZM`, `01ZQ`, `01ZH`, `01ZJ`, `09ZQ` (absolute Noetherian
  approximation and limits of schemes).
- B. Conrad, *Deligne's notes on Nagata compactifications*, Thm 2.4
  (extension of a partial section after an admissible blow-up).
