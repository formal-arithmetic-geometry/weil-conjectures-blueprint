+++
kind  = "proof"
of    = "rem-pd-scope"
+++
The comparison of scopes is immediate from the statements:
[rem-sc-jacobian-scope] asserts that representability over a general
ground field is not proved in that chapter and would require a descent from a
finite separable extension, while
[thm-pd-jacobian-general-field] supplies exactly that descent, with the
two ingredients named in that remark replaced by
[thm-pd-effective-descent] (Stacks Project, Lemma 39.25.3, Tag
[0CCJ](https://stacks.math.columbia.edu/tag/0CCJ)) and
[thm-pd-spreading-out] (Stacks Project, Lemma 32.10.1, Tag
[01ZM](https://stacks.math.columbia.edu/tag/01ZM)). That the separable
closedness of the two cited theorems serves only to produce a rational point
is visible in the proof of [thm-pc-picard-representable], which obtains
$\sigma$ from [lem-pc-rational-points-dense] and then applies
[lem-pc-rational-hyp]; the rational point is what
[thm-pd-geometric-pic0] supplies geometrically and what the descent of
[thm-pd-jacobian-general-field] replaces, the two theorems
[thm-sc-jacobian-representability] and [thm-pd-geometric-pic0] being
the separably closed statement and its geometric consequence.
