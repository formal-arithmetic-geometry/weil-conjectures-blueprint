+++
kind = "proof"
of = "lem-weil-pbc-etale-section-localization"
+++
Proof: Give R its S-algebra structure through s. Since s(e)=1, each r is the
image of e*algebraMap R S r, so this algebra map is surjective. Its kernel is
(1-e), and e is idempotent. The Mathlib criterion
IsLocalization.away_of_isIdempotentElem therefore makes R a localization of S
away from e. Uniqueness of localization gives an S-algebra equivalence from
Localization.Away e to R, which sends the image of x to s(x). Its underlying
ring equivalence is an R-algebra equivalence: on an R-scalar r, the scalar-tower
formula expresses its image as the image of algebraMap R S r, and s sends that
element to r. This proves both the equivalence and the required extension formula.
