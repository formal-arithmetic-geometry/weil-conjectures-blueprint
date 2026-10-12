+++
kind  = "proof"
of    = "cor-fin-projective-curve-finite-group"
+++
A finite abelian group has a finite filtration with successive
quotients $\mathbf F_\ell$, for primes $\ell$ dividing its order.
Taking constant sheaves is exact, as may be checked on every stalk.
Proceed by induction along this filtration, starting from
[thm-fin-projective-curve-constant].
For $0\to M'\to M\to M''\to0$, the long exact sequence identifies
$R^qf_*\underline M$ in a short exact sequence with left term

$$
\operatorname{coker}(R^{q-1}f_*\underline {M''}
\to R^qf_*\underline {M'})
\quad\hbox{and right term}\quad
\ker(R^qf_*\underline {M''}\to R^{q+1}f_*\underline {M'}).
$$

All four sheaves are constructible by induction, with the
negative-degree term zero. The kernel, cokernel and extension
clauses of [thm-constructible-serre] finish the induction.
