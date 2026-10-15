+++
kind = "proof"
of = "det-sfb-coefficient-comparisons-direct-image"
+++
The comparison is natural in $K$, compatible with exact triangles and finite sums, and is the identity for
$\Lambda'=\Lambda$.

*$\mathcal O_E\to A$.* $A$ is a finitely generated $\mathcal O_E$-module killed by a power of $\pi_E$, so it has a
resolution $0\to\mathcal O_E^m\xrightarrow{\phi}\mathcal O_E^n\to A\to0$. Its condensed version is exact (a continuous map to a
finite quotient lifts on a finite clopen partition), and pullback to $X$ gives an exact sequence
$0\to\mathcal O_{E,X}^m\to\mathcal O_{E,X}^n\to A_X\to0$. Hence $K_A=\operatorname{cone}(K^m\xrightarrow{\phi}K^n)$
(restricted to $A$-modules), and similarly for $Rf_*K$. Since $Rf_*$ is exact and additive, it commutes with
this cone, and the comparison map is the induced map of cones, an isomorphism.

*$\mathcal O_E\to\mathcal O_F$, $E\to F$.* $F$ is finite free over $E$ (and $\mathcal O_F$ over $\mathcal O_E$), so $K_{F}\simeq K^{\oplus[F:E]}$
as $E$-modules, compatibly with $Rf_*$; restriction of scalars is conservative, so the comparison is an
isomorphism.

*$\mathcal O_E\to E$.* $K_E=K[1/\ell]=\varinjlim(K\xrightarrow{\ell}K\xrightarrow{\ell}\cdots)$, a filtered colimit of
complexes with a common lower bound (as $K$ is bounded). By [sk-lem-bounded-continuity],
$R^qf_*$ commutes with this colimit, so $\mathcal H^q(Rf_*(K_E))=\varinjlim\mathcal H^q(Rf_*K)=\mathcal H^q((Rf_*K)_E)$, via the
comparison map.

*$E\to\Qlb$.* $K_{\Qlb}=\varinjlim_{F}K_F$ over finite $F\supset E$, again a filtered system with a common lower
bound; combine [sk-lem-bounded-continuity] with the finite case $E\to F$.
