+++
kind  = "proof"
of    = "sk-prop-integral-criterion"
uses = ["sk-prop-integral-local-structure", "sk-def-sfb-constructible", "sk-prop-sf-open-closed-triangle"]
+++
The substantial implication is (2)$\Rightarrow$(3), which is [sk-prop-integral-local-structure].
The others hold because local models are complete, have finite Tor amplitude, and have
constructible reductions, and these properties survive extension by zero from strata. We prove
(1)$\Rightarrow$(2)$\Rightarrow$(3)$\Rightarrow$(1) and (3)$\Leftrightarrow$(4).

*(1) implies (2).* A finitely generated $\cO_E$-module is a finite sum of copies of $\cO_E$
and of modules $\cO_E/\pi_E^r$, so its sheaf has a two-term finite free resolution. The
coefficient sheaf $\cO_{E,U_i}$ on a chart $U_i$ of a local model is derived complete by its
profinite description and the surjectivity of the transition maps between its finite
quotients. Completeness is preserved by finite sums and cones, and therefore the finite
constant local models of [sk-def-sfb-constructible] are complete, and their reductions are
bounded locally constant finite complexes. These assertions can be checked on a pro-étale
cover, since restriction to an object is a localization of the topos and preserves limits and
the cones defining the reductions.

For a constructible sheaf, choose a finite stratification as in the definition. Let
$a=i\circ j$ be a locally closed immersion, with $j$ a quasi-compact open and $i$ a closed
immersion. Then $a_!=i_*j_!$ is exact, commutes with the cones defining the reductions, and
preserves limits. For $j$ this is the assertion about limits in
[sk-prop-sf-open-closed-triangle], see (Stacks Project, Tag 09BP). For $i$ it follows from
exactness of $i_*$ and the fact that it is a right adjoint. Hence extension by zero preserves
completeness. Using the finite filtration by open and closed pieces, we see that the whole
sheaf is complete with constructible finite reductions. Finally, (2) follows by applying this
to the finitely many cohomology sheaves of $K$ and using the bounded Postnikov triangles.

*(2) implies (3).* This is [sk-prop-integral-local-structure].

*(3) implies (1).* Each of the finitely many strata is quasi-compact, so its local models can
be checked on a finite covering by quasi-compact pro-étale objects, and their bounds give a
common cohomological interval. Since the map from the constant sheaf with value the discrete
ring $\cO_E$ to $\cO_{E,S}$ is flat (Stacks Project, Tag 099L), the cohomology of a local model
is $\cO_{E,S}\otimes_{\cO_E}H^q(P^\bullet)$ with $H^q(P^\bullet)$ finitely generated over
$\cO_E$. These are the finite constant local models of [sk-def-sfb-constructible], which proves
(1).

*(3) is equivalent to (4).* The local bounded finite free models have finite Tor amplitude.
Since the stratification is finite, there is a common interval, and the restrictions to the
strata are exact and jointly conservative, so they detect vanishing after tensoring with any
sheaf of modules. This shows that (3) implies (4). Conversely, (4) implies (1) by definition of
$\Dctf$, and hence (3) by the implications already proved.
