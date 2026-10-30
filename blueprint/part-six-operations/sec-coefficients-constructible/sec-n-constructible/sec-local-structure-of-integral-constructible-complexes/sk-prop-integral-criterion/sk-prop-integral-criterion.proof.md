+++
kind = "proof"
of = "sk-prop-integral-criterion"
uses = ["sk-prop-integral-local-structure", "sk-def-sfb-constructible", "sk-prop-sf-open-closed-triangle"]
+++
The substantial implication is (2)$\Rightarrow$(3), which is
Proposition [sk-prop-integral-local-structure]. The others hold because
the complexes $\mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet$ are complete, have finite Tor amplitude, and have
constructible reductions, and these properties survive extension by zero
from strata. We prove (1)$\Rightarrow$(2)$\Rightarrow$(3)$\Rightarrow$(1) and
(3)$\Leftrightarrow$(4).

*(1) implies (2).*
A finitely generated $\mathcal O_E$-module is a finite sum of copies of
$\mathcal O_E$ and of modules $\mathcal O_E/\pi_E^r$, so its sheaf has a
two-term finite free resolution. The coefficient sheaf
$\mathcal O_{E,U_i}$ on a member $U_i$ of the cover in Definition [sk-def-sfb-constructible](1) is derived complete by its profinite description and
the surjectivity of the transition maps between its finite quotients.
Completeness is preserved by finite sums and cones, and therefore the
modules $\mathcal O_{E,U_i}\otimes_{\mathcal O_E}P_i$ of Definition [sk-def-sfb-constructible](1) are complete,
and their reductions are bounded locally constant finite complexes. These
assertions can be checked on a pro-étale cover, since restriction to
an object is a localization of the topos and preserves limits and the
cones defining the reductions.

For a constructible sheaf, choose a finite stratification as in the
definition. Let
$a=i\circ j$ be a locally closed immersion, with $j$ a quasi-compact
open and $i$ a closed immersion. Then $a_!=i_*j_!$ is exact, commutes
with the cones defining the reductions, and preserves limits. For $j$ this
is the assertion about limits in Proposition [sk-prop-sf-open-closed-triangle], see
[Stacks, Tag 09BP](https://stacks.math.columbia.edu/tag/09BP). For $i$ it follows from exactness of $i_*$ and the fact that
it is a right adjoint. Hence extension by zero preserves completeness. Using
the finite filtration by open and closed pieces, we see that the whole
sheaf is complete with constructible finite reductions. Finally, (2)
follows by applying this to the finitely many cohomology sheaves of $K$ and
using the bounded Postnikov triangles.

*(2) implies (3).*
This is Proposition [sk-prop-integral-local-structure].

*(3) implies (1).*
Each of the finitely many strata is quasi-compact, so the local isomorphisms of (3)
can be taken on a finite covering by quasi-compact pro-étale objects,
and their bounds give a common cohomological interval. Since the map from
the constant sheaf with value the discrete ring $\mathcal O_E$ to
$\mathcal O_{E,S}$ is flat [Stacks, Tag 099L](https://stacks.math.columbia.edu/tag/099L), the cohomology of
$\mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet$ is
$\mathcal O_{E,S}\otimes_{\mathcal O_E}H^q(P^\bullet)$ with
$H^q(P^\bullet)$ finitely generated over $\mathcal O_E$. These sheaves satisfy
the condition of Definition [sk-def-sfb-constructible](1),
which proves (1).

*(3) is equivalent to (4).*
The complexes $\mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet$ have finite Tor amplitude. Since the
stratification is finite, there is a common interval, and the restrictions
to the strata are exact and jointly conservative, so they detect
vanishing after tensoring with any sheaf of modules. This shows that (3) implies (4).
Conversely, (4) implies (1) by definition of $D^b_{\mathrm{ctf}}$, and hence (3) by
the implications already proved.
