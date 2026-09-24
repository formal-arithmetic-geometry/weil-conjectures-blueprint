+++
id = "the-general-kunneth-formula"
kind = "section"
title = "The general Kunneth formula"
order = 3110
uses = ["def-compact-support-direct-image-detailed", "def-kun-kunneth-map", "def-kun-separably-closed", "def-kun-unbounded-exchange", "def-weil-extension-by-zero", "lem-kun-03qu-sep-closed", "lem-kun-0f10", "lem-kun-0f12", "lem-kun-0f14a", "lem-kun-0f14b", "lem-kun-0f1h", "lem-kun-0f1i", "lem-kun-0f1j", "lem-kun-0f1n", "lem-kun-cd-sep-closed-point", "lem-kun-inverse-image-monoidal", "lem-kun-leray-unbdd"]
+++
This section decomposes Lemma 59.97.9 of the Stacks project
([Tag `0F1P`](https://stacks.math.columbia.edu/tag/0F1P)),
the final goal of this chapter.

**Status.** The Kunneth theorem [thm-kun-0f1p] is now stated and
proved, without any properness hypothesis on $X$ or $Y$, with
bounded coefficients $\kunZn$ for $n$ invertible in the
separably closed ground field. The proof follows the Stacks route
([lem-kun-0f14b] with one proper factor, the open-immersion base
change [lem-kun-0f1h], the field-base change
[lem-kun-0f1i], the projection-formula variant
[lem-kun-0f1j] and its unbounded form
[lem-kun-0f1n]); every external input is a decomposed statement
with its Stacks tag, and the Kunneth-specific proofs are decomposed
in full. This is the ingredient of the Weil-conjectures blueprint
that supplies multiplicativity of cohomology in products; its uses in
the later chapters (trace formula, weight machinery) are recorded
there by citing [thm-kun-0f1p] and the one-proper-factor form
[lem-kun-0f14b].
