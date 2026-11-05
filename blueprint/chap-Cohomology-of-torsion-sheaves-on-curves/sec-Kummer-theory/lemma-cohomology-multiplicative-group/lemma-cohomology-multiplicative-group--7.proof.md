+++
kind = "proof"
of = "lemma-cohomology-multiplicative-group--7"
uses = []
+++
Choose a nonempty affine open $U\subseteq C$. Its ring of functions is a
finitely generated $k$-domain of dimension at most one, and its fraction
field is $k(C)$. Noether normalization identifies the transcendence
degree with the dimension, giving $\operatorname{trdeg}_k k(C)\leq1$.
Apply `IsQuasiAlgClosed.of_trdeg_le_one`: in transcendence degree zero
the field is $k$, and otherwise it is algebraic over a rational function
field $k(t)$. The latter is $C_1$ by a count of the coefficients of
polynomial unknowns, and the $C_1$ property passes to algebraic extensions.

Finally apply `IsQuasiAlgClosed.subsingleton_cohomologicalBrauerGroup`.
It computes degree-two cohomology on finite Galois covers by Čech
cohomology. Hilbert 90 supplies the required exactness on sections,
and the crossed-product argument for a $C_1$ field kills the second
Galois Čech cohomology.
