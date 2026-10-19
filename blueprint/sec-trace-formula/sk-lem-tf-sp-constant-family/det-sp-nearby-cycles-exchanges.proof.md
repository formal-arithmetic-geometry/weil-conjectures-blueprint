+++
kind = "proof"
of = "det-sp-nearby-cycles-exchanges"
uses = ["thm-weil-pbc-bounded-below", "sbc-thm-bounded-derived-smooth-base-change"]
+++
The invertibility comes from two base change theorems for torsion coefficients.

For proper $f$, composition identifies the two generic direct images,
$R\bar f_*R\bar j'_*\simeq R(\bar f\bar j')_*=R(\bar j f_{\bar\eta})_*\simeq R\bar j_*Rf_{\bar\eta*}$.
Proper base change [thm-weil-pbc-bounded-below] for the proper map $\bar f$ and the closed
immersion $\bar i$ of the special fibre gives
$\bar i^*R\bar f_*\simeq Rf_{s*}\bar i'^*$ on complexes with torsion cohomology. Combining,

$$
Rf_{s*}R\Psi_{\mathcal Y'}L=Rf_{s*}\bar i'^*R\bar j'_*L_{\bar\eta}
\simeq\bar i^*R\bar f_*R\bar j'_*L_{\bar\eta}
\simeq\bar i^*R\bar j_*Rf_{\bar\eta*}L_{\bar\eta}=R\Psi_{\mathcal Y}Rf_{\eta*}L,
$$

where the last step uses that proper direct image commutes with the base change from $\eta$ to
$\bar\eta$ (proper base change again).

For smooth $f$, the square formed by $\bar f$, $\bar j$ and $\bar j'$ is cartesian, $\bar f$ is
smooth and $\bar j$ is quasi-compact and quasi-separated. Smooth base change
[sbc-thm-bounded-derived-smooth-base-change] makes $\bar f^*R\bar j_*\to R\bar j'_*f_{\bar\eta}^*$
an isomorphism on bounded constructible complexes; the coefficients are annihilated by a power of
$\ell$, which is invertible on $S$. Restricting to the special fibre gives the invertibility of
the pullback exchange.

Compatibility with composition holds because base-change maps paste along composite squares and
the composition identifications of direct images are associative. The same normalizations appear
in (SGA 7 II, XIII, (2.1.7.1)–(2.1.7.3)).
