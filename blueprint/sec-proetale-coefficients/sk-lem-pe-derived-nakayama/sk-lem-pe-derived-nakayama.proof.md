+++
kind = "proof"
of = "sk-lem-pe-derived-nakayama"
uses = ["det-pe-derived-nakayama-resolution", "det-pe-derived-nakayama-first-reduction", "lem-weil-pbc-standard-quotients-perfect"]
+++
The coefficient sequence is exact on the profinite point, hence after pullback,
and it supplies the two-term resolution ([lem-weil-pbc-standard-quotients-perfect],
[det-pe-derived-nakayama-resolution]). The short exact sequences between
successive powers of $\pi_E$ show inductively that $K_1=0$ implies $K_n=0$ for
all $n$, and completeness then gives $K=0$. Derived completeness is preserved by
cones, since both sides of the completion map are exact functors of $K$, so
applying this to the cone proves the last assertion
([det-pe-derived-nakayama-first-reduction]).

*After the lemma.* For derived complete $K$, derived global sections commute with the derived
limit, being a right adjoint, and therefore

$$
R\Gamma(X_{\Proet},K)\simeq R\varprojlim_nR\Gamma(X_{\Proet},K_n).
$$

When the $K_n$ are classical bounded-below complexes, each term on the right can be computed
on the étale site by [sk-prop-sf-comparison]. In this way the cohomology of $K$ is computed by
the normalized tower $(K_n)$.

Constructible complexes over $\mathcal O_E$ are defined in [sk-def-sfb-constructible], and for
Noetherian $X$ they are exactly the derived complete complexes $K$ whose reduction $K_1$ is
constructible ([sk-prop-integral-criterion]).

Derived complete complexes can equally be studied over the discrete coefficient ring. The map
from the constant sheaf with value the discrete ring $\mathcal O_E$ to $\mathcal O_{E,X}$ is
flat and an isomorphism modulo every $\pi_E^n$. It follows that restriction of scalars is an
equivalence between the derived complete objects of the derived categories of modules over
these two sheaves of rings
([Stacks, Tag 099I](https://stacks.math.columbia.edu/tag/099I)).

Inverting $\ell$ and passing to the colimit over $E$, we get the rational coefficient sheaves
$E_X\simeq\mathcal O_{E,X}[1/\ell]$ and $\Qlb_X\simeq\varinjlim_EE_X$
([sk-prop-sfb-qlbar-colimit-x]).
