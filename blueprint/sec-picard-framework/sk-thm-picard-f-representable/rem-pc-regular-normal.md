+++
id = "rem-pc-regular-normal"
kind = "lemma"
title = "Regular schemes are normal; the normal decomposition"
lean = ["AlgebraicGeometry.IsRegular.irreducibleSpace", "AlgebraicGeometry.IsRegular.exists_isClopen_isIntegral", "AlgebraicGeometry.IsRegular.isIntegrallyClosed_stalk", "AlgebraicGeometry.Scheme.exists_isClopen_isIntegral_of_isIntegrallyClosed_stalk"]
order = 782
uses = ["def-pc-scheme"]
+++
We use the following two facts of the Stacks Project:

- *regular schemes are normal* (Properties of Schemes,
Lemma 28.9.4, Tag [0569](https://stacks.math.columbia.edu/tag/0569);
see also Lemma 28.9.2, Tag [02IT](https://stacks.math.columbia.edu/tag/02IT)),
and
- *Noetherian normal schemes decompose*: a Noetherian normal
scheme is a finite disjoint union of normal integral schemes (Properties
of Schemes, Lemma 28.7.6, Tag [033M](https://stacks.math.columbia.edu/tag/033M)).

In particular a regular, connected, Noetherian scheme is irreducible.
(These are the scheme-level regularity-normal facts, in contrast with
[rem-pc-regularity-sc] which works with smooth curves.)
