+++
kind  = "proof"
of    = "prop-weil-pbc-algebraically-closed-extension"
+++
The assertion is $\mathcal C_7(C,F)$ of
[def-weil-pbc-eight-curve-assertions]. By
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
[lemma-weil-pbc-finite-pushforward-extension-zero] reduce to the
sheaves $j_{a,!}\mathbf F_r$ on irreducible curves. On the normalization,
[lemma-weil-pbc-normalization-exact-sequence] transfers the assertion from the
smooth case, where [thm-sc-main] supplies it for
the constant sheaf; the locally constant reduction of
[lemma-weil-pbc-curve-locally-constant-reduction], using the filtration of
[lemma-weil-pbc-finite-l-group-filtration] and the trace splitting, passes from
the constant sheaf to finite locally constant sheaves. The short-exact
devissage of [lemma-weil-pbc-eight-curve-devissage] and the filtered cohomology
of [lemma-weil-pbc-curve-filtered-cohomology] assemble the assertion for
arbitrary torsion sheaves.
