+++
id = "prop-weil-pbc-algebraically-closed-extension"
kind = "theorem"
title = "Algebraically closed extension for proper curves"
order = 1716
uses = ["def-weil-pbc-eight-curve-assertions-detailed", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-curve-constructible-reduction", "lem-weil-pbc-curve-dense-open-localization", "lem-weil-pbc-curve-filtered-cohomology", "lem-weil-pbc-eight-curve-devissage", "lem-weil-pbc-finite-r-group-filtration", "lem-weil-pbc-locally-constant-reduction", "lem-weil-pbc-zero-dimensional-field-extension", "prop-weil-pbc-finite-pushforward-extension-zero-commute", "prop-weil-pbc-normalization-comparison", "thm-weil-pbc-smooth-curve-calculations"]
tags = ["latex:proposition"]
+++
Let $k\subset k'$ be algebraically closed, let $C$ be proper of dimension at
most one over $k$, and let $F$ be a torsion etale sheaf. Then

$$
 H^q(C,F)\xrightarrow{\sim}H^q(C_{k'},F|_{C_{k'}})
 \qquad(q\geq0).
$$

## Proof

The assertion is $\mathcal C_7(C,F)$ of
[def-weil-pbc-eight-curve-assertions-detailed]. By
[lem-weil-pbc-curve-constructible-reduction] the instances for reduced curves
with constructible $\mathbf F_r$-coefficients imply $\mathcal C_7(C,F)$. A
reduced scheme of finite type over $k$ with dimension at most one is the
disjoint union of its zero-dimensional irreducible components and its
one-dimensional components: there are finitely many components, and a
zero-dimensional irreducible component is a closed point contained in no other
component, so both unions are open and closed. The zero-dimensional union
satisfies the assertion by [lem-weil-pbc-zero-dimensional-field-extension].
Cohomology and pullback over a finite disjoint union are the products of those
on its components, so it remains to treat the pure one-dimensional union. Now
the dense-open localization of [lem-weil-pbc-curve-dense-open-localization]
and the extension-by-zero comparison of
[prop-weil-pbc-finite-pushforward-extension-zero-commute] reduce to the
sheaves $j_{a,!}\mathbf F_r$ on irreducible curves. On the normalization,
[prop-weil-pbc-normalization-comparison] transfers the assertion from the
smooth case, where [thm-weil-pbc-smooth-curve-calculations] supplies it for
the constant sheaf; the locally constant reduction of
[lem-weil-pbc-locally-constant-reduction], using the filtration of
[lem-weil-pbc-finite-r-group-filtration] and the trace splitting, passes from
the constant sheaf to finite locally constant sheaves. The short-exact
devissage of [lem-weil-pbc-eight-curve-devissage] and the filtered cohomology
of [lem-weil-pbc-curve-filtered-cohomology] assemble the assertion for
arbitrary torsion sheaves.
