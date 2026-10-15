+++
kind = "proof"
of = "det-pe-derived-nakayama-resolution"
+++
*On the point.* For a profinite set $S$ the sequence
$0\to C(S,\mathcal O_E)\xrightarrow{\pi_E^n}C(S,\mathcal O_E)\to
C(S,\mathcal O_E/\pi_E^n)\to0$ is exact: $\pi_E^n$ is injective on
$\mathcal O_E$; a continuous function divisible by $\pi_E^n$ pointwise has a
continuous quotient, since division by $\pi_E^n$ is a homeomorphism
$\pi_E^n\mathcal O_E\to\mathcal O_E$; and a continuous, i.e. locally constant,
function $S\to\mathcal O_E/\pi_E^n$ lifts to a locally constant function to
$\mathcal O_E$ by lifting its finitely many values. So the sequence of condensed
$\underline{\mathcal O_E}$-modules is exact ([sk-def-sfb-condensed-ring]).

*On $X$.* The pullback $p_X^*$ of module objects is exact
([sk-prop-sfb-module-pullback-exact]) and carries
$\underline{\mathcal O_E}$, $\underline{\mathcal O_E/\pi_E^n}$ to $\mathcal O_{E,X}$,
$(\mathcal O_E/\pi_E^n)_X$ ([sk-def-sfb-pulled-back-coefficients]), so the
displayed sequence is exact. It is a resolution of $(\mathcal O_E/\pi_E^n)_X$ by
free modules of rank one, hence K-flat; this is the sheaf version of
[lem-weil-pbc-standard-quotients-perfect]. Tensoring $K$ with it gives
$K_n\simeq\operatorname{cone}(\pi_E^n\colon K\to K)$, naturally in $K$.

*Triangles.* The sequence
$0\to\mathcal O_E/\pi_E^m\xrightarrow{\pi_E^n}\mathcal O_E/\pi_E^{n+m}\to
\mathcal O_E/\pi_E^n\to0$ is exact (multiplication by $\pi_E^n$ is injective modulo
$\pi_E^{n+m}$ on $\mathcal O_E/\pi_E^m$ because $\mathcal O_E$ is a discrete
valuation ring), and after pullback it is an exact sequence of
$\mathcal O_{E,X}$-modules, by the same argument on the point. Applying the
triangulated functor $K\otimes^{\mathbf L}_{\mathcal O_{E,X}}-$ gives the
triangle $K_m\to K_{n+m}\to K_n\to$.
