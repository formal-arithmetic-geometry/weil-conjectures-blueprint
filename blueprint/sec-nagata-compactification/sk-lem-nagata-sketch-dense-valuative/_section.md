+++
id = "sk-lem-nagata-sketch-dense-valuative"
kind = "section"
title = "Dense-source valuative criterion"
order = 273
lean = ["AlgebraicGeometry.UniversallyClosed.of_valuativeCriterion_of_isDominant", "AlgebraicGeometry.IsSeparated.of_valuativeCriterion_of_isDominant"]
+++
*Lemma (sketch).*

Let $f\colon W\to S$ be a morphism and let $h\colon D\to W$ be
quasi-compact with dense image (for instance a dense quasi-compact open
$D\subseteq W$). Suppose every valuation diagram over $S$ whose generic
point maps into $D$ has a unique lift to $W$. If $f$ is quasi-compact,
it is universally closed; if $f$ is quasi-separated, it is separated. In
particular, if $f$ is moreover of finite type and quasi-separated, then
$f$ is proper; see 0894.

## Proof

For universal closedness of a quasi-compact $f$, test the existence part of
the valuative criterion. Replace $W$ by the scheme-theoretic image of $h$,
which has the same points and receives every map from a reduced scheme, so
that $h$ becomes scheme-theoretically dense; this survives flat base change.
A valuation probe through the dense source, centred at the given field
point, together with an extension of valuation rings along the residue
field extension and the composite valuation ring, turns the given square
into one whose generic point maps into $D$; its unique lift descends to the
required lift. For separatedness of a quasi-separated $f$, the uniqueness
hypothesis shows that the quasi-compact diagonal satisfies the same
criterion, so it is universally closed, hence a closed immersion. Universal
closedness together with finite type and separatedness gives properness.
