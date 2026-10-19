+++
kind = "proof"
of = "sk-lem-pe-derived-nakayama"
uses = ["det-pe-derived-nakayama-resolution", "det-pe-derived-nakayama-first-reduction", "lem-weil-pbc-standard-quotients-perfect"]
+++
The coefficient sequence is exact on the profinite point, hence after pullback,
and it supplies the two-term resolution ([lem-weil-pbc-standard-quotients-perfect],
[det-pe-derived-nakayama-resolution]). The short exact sequences between
successive powers of $\pi_E$ show inductively that $K_1=0$ implies $K_n=0$ for
all $n$, and completeness then gives $K=0$. Derived completeness is closed under
cones, so applying this to the cone proves the last assertion
([det-pe-derived-nakayama-first-reduction]).
