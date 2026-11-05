+++
id = "prose-A-23"
kind = "hidden"
title = "Proof of Nagata's theorem (1)"
order = 1464
+++
Over a Noetherian base, the theorem follows from
Proposition [proposition-compactifying-union-two-opens] by induction over an affine cover
whose members overlap densely. Each affine piece is compactified by its
closure in a projective space. The proposition then compactifies the
union of the first $r$ pieces with the next one. It requires the
overlap to be dense, because its valuative criterion only tests maps
from spectra of valuation rings whose generic point maps into the
overlap. Lemma [lemma-affine-covers-dense-intersection] provides a
cover whose total intersection contains all generic points of $X$.

Over a general qcqs base we use Noetherian approximation. This works because a morphism of finite presentation is the base change of one over a Noetherian scheme,
and compactifications are stable under base change. A morphism that is only of finite type, however, need not descend in this way. We therefore first
embed $X$ as a closed subscheme of a scheme of finite presentation over
$S$, and take the closure of $X$ in a compactification of the latter.
