+++
kind = "proof"
of = "sk-lem-pe-derived-nakayama"
uses = ["det-pe-derived-nakayama-resolution", "det-pe-derived-nakayama-first-reduction", "lem-weil-pbc-standard-quotients-perfect"]
+++
The sequence
$0\to\underline{\mathcal O_E}\xrightarrow{\pi_E^n}\underline{\mathcal O_E}\to\underline{\mathcal O_E/\pi_E^n}\to0$
is exact on the point, hence also after the exact pullback $p_X^*$, and it
provides the two-term resolution. Tensoring $K$ with the short exact
sequence $0\to\pi_E^n\mathcal O_E/\pi_E^{n+1}\to\mathcal O_E/\pi_E^{n+1}\to \mathcal O_E/\pi_E^n\to0$, whose first term is isomorphic to
$\mathcal O_E/\pi_E$, gives a triangle $K_1\to K_{n+1}\to K_n$. By
induction $K_1=0$ implies $K_n=0$ for all $n$, and then $K=0$ by
completeness.
Derived completeness is preserved by cones, since both sides of the
completion map are exact functors of $K$. The last assertion follows by
applying the previous one to the cone.
