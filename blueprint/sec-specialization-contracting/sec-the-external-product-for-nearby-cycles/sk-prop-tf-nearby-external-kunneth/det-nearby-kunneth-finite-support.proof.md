+++
kind = "proof"
of = "det-nearby-kunneth-finite-support"
uses = ["lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $u\colon T\hookrightarrow V$ be the inclusion of the finite closed reduced subscheme on the
support. Since $C$ is supported on $T$, the unit gives $C\simeq u_*u^*C$. Each point of $T$ is
closed in a finite-type $k$-scheme, so its residue field is a finite, hence purely inseparable,
extension of the separably closed field $k$, and its étale site is that of a point. Thus $u^*C$ is
the collection of the stalk complexes $C_t$, $t\in T$, and

$$
R\Gamma(V,C)\simeq R\Gamma(T,u^*C)\simeq\bigoplus_{t\in T}C_t
$$

is their finite direct sum. If it vanishes, every stalk complex at a point of $T$ vanishes, and the
stalks off $T$ vanish by hypothesis; geometric stalks detect vanishing
[lemma-weil-pbc-geometric-stalk-conservative], so $C=0$.
