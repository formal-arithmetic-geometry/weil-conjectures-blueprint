+++
id = "lem-weil-rationalization-idempotent-complete"
kind = "lemma"
title = "Idempotent completeness of the rationalized category"
lean = ["AlgebraicGeometry.Etale.DerivedCategory.isIdempotentComplete_boundedConstructibleRational"]
order = 2458
uses = ["def-weil-derived-complete-integral-detailed", "def-weil-karoubi-envelope", "def-weil-rationalization-karoubi", "thm-weil-karoubian-bounded-t", "thm-weil-pbc-finite-stage-karoubian"]
+++
Let $E/\Ql$ be a finite extension with valuation ring $\mathcal O_E$, let $Y$
be a scheme, and let $D^b_c(Y,E)$ be the rationalized category of
[def-weil-rationalization-karoubi]. Then $D^b_c(Y,E)$ is idempotent
complete, and the canonical functor

$$
 D^b_c(Y,E)\longrightarrow\Kar\bigl(D^b_c(Y,E)\bigr)
$$

into its Karoubi envelope is an exact equivalence.
