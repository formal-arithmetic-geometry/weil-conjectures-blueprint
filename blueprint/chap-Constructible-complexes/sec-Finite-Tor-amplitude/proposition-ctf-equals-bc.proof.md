+++
kind = "proof"
of = "proposition-ctf-equals-bc"
order = 253
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "lemma-extremally-disconnected-covers", "proposition-pro-etale-affines-form-basis", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "proposition-comparison-etale-derived-category", "definition-compactification-refinement"]
+++
For $\mathcal O_E$, and hence for $\mathbf Z_\ell$, this is the equivalence of (1)
and (4) in the criterion above. For the fields we show that every
[constructible sheaf](@definition-constructible-sheaves) is flat, which bounds the [Tor amplitude](@definition-constructible-sheaves) of a bounded
complex by its cohomological amplitude.

For a field $\Lambda(*)$, a [constructible sheaf](@definition-constructible-sheaves) $M$ is, on each stratum and locally on
a cover $\{U_i\}$, of the form $\Lambda_{U_i}\otimes_{\Lambda(*)}P_i$
with $P_i$ a finite-dimensional vector space, so it is locally a finite free
$\Lambda_{U_i}$-module. Restriction to the strata is exact and the restrictions
are jointly conservative, as in the proof of the criterion. Hence every
[constructible sheaf](@definition-constructible-sheaves) has [Tor amplitude](@definition-constructible-sheaves) in $[0,0]$. Finally, a bounded complex whose finitely many cohomology
sheaves have [finite Tor amplitude](@definition-constructible-sheaves) has [finite Tor amplitude](@definition-constructible-sheaves), by the
triangles of its canonical filtration.
