+++
kind = "proof"
of = "lemma-structure-integral-constructible-complexes"
order = 492
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "lemma-extremally-disconnected-covers", "theorem-existence-contractible-covers", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves"]
+++
The conditions of Proposition [proposition-integral-constructibility-criterion], [derived
completeness](@definition-derived-adic-completeness) and [constructible](@definition-constructible-sheaves) reduction, are stable under shifts and
cones, so [$\Dbc(X,\mathcal O_E)$](@definition-constructible-sheaves) is triangulated. By
Proposition [proposition-local-structure-integral-constructible-complexes], on the strata of a finite
stratification an object is pro-étale locally of the form
$\href{@lemma-comparison-completed-coefficients}{\mathcal O_{E,S}}\otimes P^\bullet$ with $P^\bullet$ a bounded complex
of finite free $\mathcal O_E$-modules. Since [$\mathcal O_{E,S}$](@lemma-comparison-completed-coefficients)
is flat over $\mathcal O_E$, we get
$H^i=\href{@lemma-comparison-completed-coefficients}{\mathcal O_{E,S}}\otimes H^i(P^\bullet)$ on such a stratum. This
local form of the cohomology sheaves shows that the truncations stay in
[$\Dbc$](@definition-constructible-sheaves). It also gives (2), and then the abelian part of (1). In (1), essential smallness holds because a [constructible sheaf](@definition-constructible-sheaves) is
determined up to isomorphism by a stratification, local presentations,
descent data and finitely many extension classes. Finally, for (3) we use that a finitely generated module over the discrete valuation ring $\mathcal O_E$ has a
free resolution $0\to\mathcal O_E^r\to\mathcal O_E^s\to P\to0$ of length
one.
