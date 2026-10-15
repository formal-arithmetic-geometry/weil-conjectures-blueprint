+++
kind = "proof"
of = "det-sp-field-extension-towers"
+++
(1) $\mathcal O_F$ is a finite free $\mathcal O_E$-module (also when $F/E$ is
ramified), so $\mathcal O_{F,T}\simeq\mathcal O_{E,T}^{\oplus r}$ as
$\mathcal O_{E,T}$-modules locally, and $-\otimes\mathcal O_{F,T}$ is exact and commutes
with derived limits (finite direct sums do). Its reductions are
$(K\otimes\mathcal O_F)/\ell^n=(K/\ell^n)\otimes_{\mathcal O_E/\ell^n}\mathcal O_F/\ell^n$ by
associativity. A finite free extension preserves Tor bounds and
constructibility levelwise, so by the reconstruction of normalized towers the
result lies in $\Dbc(-,\mathcal O_F)$.

(2) By [det-sp-reduction-compatibilities] (2), for the commutative square of
rings $\mathcal O_E/\ell^n\to\mathcal O_F/\ell^n$, $\mathcal O_E/\ell^n\to\mathcal O_E/\ell^m$,
$\mathcal O_F/\ell^n\to\mathcal O_F/\ell^m$, the two composite comparisons
$\mathcal O_E/\ell^n\to\mathcal O_F/\ell^m$ both equal the comparison for the composite
ring map; hence the level-$n$ comparisons commute with the reduction maps and
form a map of towers, for $b$ and for $c$. They are levelwise isomorphisms,
hence isomorphisms of towers; their $R\varprojlim$, combined with (1) and the
tower descriptions of $Rf_{!,\mathcal O_E}$ and $f^!_{\mathcal O_E}=H_{f,\mathcal O_E}$
([det-sp-integral-adjunction-bijection]), are the stated integral comparisons.
The unit, counit and purity compatibilities are proved in the tower category
by the same transposition arguments as at finite level
([det-sp-reduction-compatibilities] (1),(3) and the defining counit identity):
the tower comparison for $c$ is defined as the transpose of the scalar-extended
tower counit composed with $b^{-1}$, the tower unit, counit and
$\gamma_{f,\bullet}$ are morphisms in $D(\operatorname{Tow})$, and the arguments use only
the triangle identities and the orientation comparison of rank-one tower
sheaves (checked levelwise). Applying $R\varprojlim$ gives the integral
identities. Composition for
$E\subset F\subset L$ likewise follows levelwise from (2) of
[det-sp-reduction-compatibilities].

(3) Inverting $\ell$ is the scalar extension $-\otimes_{\mathcal O}E$ applied to
integral models, which commutes with $Rf_!$, $f^*$, twists and with the
extension $\mathcal O_E\to\mathcal O_F$ ($F=\mathcal O_F\otimes_{\mathcal O_E}E$), by
[det-sp-rational-localized-hom]. Since the unit and counit over $E$ and over
$F$ are the scalar extensions of the integral ones, the integral compatibilities
of (2) give the rational ones.
