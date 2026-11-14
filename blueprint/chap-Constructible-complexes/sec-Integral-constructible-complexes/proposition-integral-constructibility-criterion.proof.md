+++
kind = "proof"
of = "proposition-integral-constructibility-criterion"
order = 248
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-exact-products", "proposition-milnor-sequence", "definition-classical-pro-etale-sheaves", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-constructible-sheaves", "corollary-finite-tor-amplitude-under-comparison", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-reduction-derived-nakayama", "lemma-local-constancy-finite-level", "lemma-integral-models", "lemma-acyclic-resolutions", "proposition-sp-unique-adjoint"]
+++
The substantial implication is (2)$\Rightarrow$(3), which is
Proposition [proposition-local-structure-integral-constructible-complexes]. The others hold because
the complexes $\mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet$ are complete, have finite Tor amplitude, and have
constructible reductions. These properties survive extension by zero
from strata. We prove (1)$\Rightarrow$(2)$\Rightarrow$(3)$\Rightarrow$(1) and
(3)$\Leftrightarrow$(4).

*(1) implies (2).*
We first treat a single constructible sheaf, locally on a stratum, then
extend by zero from the strata, and finally pass to complexes.

A finitely generated $\mathcal O_E$-module is a finite sum of copies of
$\mathcal O_E$ and of modules $\mathcal O_E/\pi_E^r$, so its sheaf has a
two-term finite free resolution. The coefficient sheaf
$\mathcal O_{E,U_i}$ on a member $U_i$ of the cover in
Definition [definition-constructible-sheaves](1) is derived complete. Indeed, it is
the limit of its finite quotients by Lemma [lemma-comparison-completed-coefficients],
and since the transition maps between these quotients are surjective, this
limit agrees with the derived limit by Proposition [proposition-milnor-sequence].
As completeness is preserved by finite sums and cones, the
modules $\mathcal O_{E,U_i}\otimes_{\mathcal O_E}P_i$ of
Definition [definition-constructible-sheaves](1) are complete, and their
reductions are bounded locally constant finite complexes. We may check
these assertions on a pro-étale cover, because restriction to an object
is a localization of the topos, and it preserves limits and the cones
defining the reductions.

For a constructible sheaf, choose a finite stratification as in the
definition. Then for a stratum $a:S\hookrightarrow X$, factored as
$a=i\circ j$ as in Section [sec-Derived-functors], the open immersion $j$ is
quasi-compact because $X$ is Noetherian. Extension by zero $a_!=i_*j_!$ preserves
completeness, because it is exact, commutes
with the cones defining the reductions, and preserves limits. Here, for $j_!$ the
last point is the assertion about limits in Proposition [proposition-extension-zero-restriction-closed-subscheme], see
[Stacks, [09BP](https://stacks.math.columbia.edu/tag/09BP)], while for $i_*$ it holds because $i_*$ is exact and
a right adjoint. Using
the finite filtration by open and closed pieces, we see that the whole
sheaf is complete with constructible finite reductions. Applying this to
the finitely many cohomology sheaves of $K$ and
using the bounded Postnikov triangles, we obtain (2).

*(2) implies (3).*
This is Proposition [proposition-local-structure-integral-constructible-complexes].

*(3) implies (1).*
Each of the finitely many strata is quasi-compact, so the local isomorphisms of (3)
can be taken on a finite covering by quasi-compact pro-étale objects,
and their bounds give a common cohomological interval. Since the map from
the constant sheaf with value the discrete ring $\mathcal O_E$ to
$\mathcal O_{E,S}$ is flat [Stacks, [099L](https://stacks.math.columbia.edu/tag/099L)], the cohomology of
$\mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet$ is
$\mathcal O_{E,S}\otimes_{\mathcal O_E}H^q(P^\bullet)$. Here
$H^q(P^\bullet)$ is finitely generated over $\mathcal O_E$, so these sheaves satisfy
the condition of Definition [definition-constructible-sheaves](1). This proves (1).

*(3) is equivalent to (4).*
The complexes $\mathcal O_{E,S}\otimes_{\mathcal O_E}P^\bullet$ have finite Tor
amplitude, and since the stratification is finite there is a common interval.
Since the restrictions to the strata are exact and jointly conservative, they
detect vanishing after tensoring with any sheaf of modules, and (3) implies (4).
Conversely, (4) implies (1) by definition of $D^b_{\mathrm{ctf}}$, and hence (3) by
the implications already proved.
