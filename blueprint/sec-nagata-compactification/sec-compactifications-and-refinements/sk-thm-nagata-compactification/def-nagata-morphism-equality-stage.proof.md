+++
kind  = "proof"
of    = "def-nagata-morphism-equality-stage"
+++
We show that such a stage exists. On a finite affine target cover, the
inverse-image opens of the two morphisms have equal inverse images over
$S$, so they agree past the stage of [def-nagata-qc-open-equality-stage].
On a finite affine cover of each common inverse image, the induced ring
maps agree over $S$ on a finite generator list, so by
[lemma-nagata-filtered-colimit-finite-data] they agree on it at some
stage and at every later stage. A common upper bound of these finitely many
stages (for instance the selected upper bound of
[def-nagata-directed-finite-upper-bound] for a directed index set) has the
required property: past it the local maps agree, and the local equalities
glue.
