+++
id = "prose-A1-01"
kind = "hidden"
title = "Overview of the appendices and of Nagata"
order = 4
+++
Appendices “Nagata compactification and Chow's lemma”–“Cohomology of curves”
prove results from algebraic geometry that the main text uses:
Nagata's compactification theorem and Chow's lemma, which define
$Rf_!$ and reduce proper base change to projective morphisms
(Appendix “Nagata compactification and Chow's lemma”); multiplication and Tate modules
of abelian varieties (Appendix “Abelian varieties and Tate modules”); the Picard scheme and
the Jacobian of a curve (Appendix “Picard schemes and Jacobians”); and the cohomology of
curves with torsion coefficients (Appendix “Cohomology of curves”); see
also (GeoBP). Appendix “Specialization and contracting correspondences”
gives a second approach, by specialization, to the local terms of
contracting correspondences; Section “The Grothendieck–Lefschetz trace formula” does not
depend on it. Appendix “Algebraic groups and Lie algebras in characteristic zero” proves the facts on
algebraic groups and Lie algebras in characteristic zero used in
Section “Monodromy and determinant weights”.

The direct image with proper support is defined through
compactifications and their common refinements, and proper base change
is reduced to projective morphisms by Chow's lemma. Nagata's theorem
says that every separated morphism of finite type $X\to S$ with $S$
quasi-compact and quasi-separated factors as a quasi-compact open
immersion $X\to\overline X$ followed by a proper morphism
$\overline X\to S$. Chow's lemma says that for a proper morphism $X\to S$ there is a
proper surjection $\widetilde X\to X$ with $\widetilde X$ projective
over $S$ (Theorem [sk-thm-chow-projective]). We prove Nagata's
compactification theorem using only schemes, schematic closures,
blow-ups and valuation rings, and we deduce the projective form of
Chow's lemma above from the version in [Stacks, Tag 0202](https://stacks.math.columbia.edu/tag/0202). The only result from the main text that we use is
Proposition [sk-prop-sf-open-closed-triangle], in the proof of
Lemma [sk-lem-nagata-density-normalization]. Besides Chow's lemma, we quote two
results: flattening by blow-up, in
the form of its consequence, the elimination of indeterminacy
(Theorem [sk-lem-nagata-sketch-elimination]), and Noetherian approximation.

Locally a compactification is easy to find: if $S$ and $X$ are affine,
then $X$ embeds in affine space over $S$, and we take its closure in
projective space.
The whole difficulty is to glue. Compactifications of two opens
$M_1,M_2$ of $X$ need not glue along their overlap, because the glued scheme
need not be separated: a specialization can approach different
boundary points on the two sides. A blow-up whose center avoids the
given opens separates the closures of the two boundaries and removes
this obstruction, and induction over an affine cover then gives the
theorem over a Noetherian base. The general case follows by Noetherian
approximation.
