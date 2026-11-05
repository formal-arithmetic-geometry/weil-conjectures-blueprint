+++
kind = "proof"
of = "lemma-change-coefficients-exceptional-inverse-image--7"
order = 640015
uses = ["lemma-change-coefficients-exceptional-inverse-image--1", "lemma-change-coefficients-exceptional-inverse-image--2", "lemma-change-coefficients-exceptional-inverse-image--3", "lemma-change-coefficients-exceptional-inverse-image--4", "lemma-change-coefficients-exceptional-inverse-image--5", "lemma-change-coefficients-exceptional-inverse-image--6"]
+++
The original argument uses compatibility of the comparison maps with composition
of coefficient maps: once every elementary comparison is known to be invertible,
their composite is the comparison of (7.1). The restricted statements recorded
in the preceding details do not supply all those elementary cases. This general
composition argument is therefore not a proof supplied by the Lean mainline.
For its passage from $\mathcal O_E$ to $\overline{\mathbf Q}_\ell$, Lean instead
composes the particular comparisons of
[lemma-change-coefficients-exceptional-inverse-image--5] and
[lemma-change-coefficients-exceptional-inverse-image--6].
