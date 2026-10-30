+++
kind = "proof"
of = "sk-lem-finite"
uses = ["sk-thm-sf-ctf-stability", "sk-cor-sf-direct-image-ctf", "sk-prop-scalar-six", "sk-prop-integral-criterion", "sk-lem-integral-models", "sk-thm-sfb-qlbar-two-colimit"]
+++
By the comparisons of Section [sec-pe-coefficient-bridge], taking global
sections identifies $D^b_{\mathrm{ctf}}(s,\Lambda)$ with the full subcategory of
$D(\Lambda)$ of complexes with bounded finitely generated cohomology and
finite Tor dimension. It remains to see that these complexes are perfect.
A constructible complex with finite coefficients has
bounded finite cohomology, and since it has finite Tor amplitude, it is perfect.
To see this, take a bounded-above resolution by finite free modules and
truncate it below the Tor bound. The last syzygy that remains is finitely
presented and flat, hence projective. With integral coefficients the
constructible complexes on the point are those with bounded finitely
generated $\mathcal O_E$-cohomology. Since a discrete valuation ring has
global dimension one, these complexes are perfect. With field
coefficients, bounded complexes with finite-dimensional cohomology are perfect.

Proposition [sk-thm-sf-ctf-stability] applies to the two direct images of
$a_X$, so both lie in $D^b_{\mathrm{ctf}}(s,\Lambda)$. If we represent such a
complex by a bounded complex of finite projective modules, its termwise
dual is again of this form, and the double evaluation map is termwise
an isomorphism. The stalk $K_{\bar x}$ is the global sections of
$\bar x^*K\in D^b_{\mathrm{ctf}}(s,\Lambda)$ (Proposition [sk-thm-sf-ctf-stability]), so it
is perfect as well. This proves all the assertions.
