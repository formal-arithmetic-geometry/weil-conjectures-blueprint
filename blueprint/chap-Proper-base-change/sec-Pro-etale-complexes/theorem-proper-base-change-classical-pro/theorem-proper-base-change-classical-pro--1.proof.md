+++
kind = "proof"
of = "theorem-proper-base-change-classical-pro--1"
order = 402002
uses = ["definition-torsion-pbc-property", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "definition-torsion-sheaves"]
+++
By Proposition [proposition-proper-base-change-projective-line],
$\mathrm{PBC}_{\Lambda}(\mathbf P^1_S\to S)$ holds for every scheme $S$.
Proposition [proposition-proper-base-change-etale-site] therefore gives
$\mathrm{PBC}_{\Lambda}(f)$. Applying the property of
Definition [definition-torsion-pbc-property] to the given cartesian
square and to $K$ proves the first assertion. These propositions apply
to an arbitrary commutative ring $\Lambda$ with torsion cohomology
sheaves.

If the additive group of $\Lambda$ is torsion, some positive integer
annihilates $1\in\Lambda$, and hence every $\Lambda$-module. Thus every
cohomology sheaf of every $K\in D^+(X_{\acute{e}t},\Lambda)$ is torsion.
The first assertion shows that every component of the base change
transformation is an isomorphism, so the transformation itself is an
isomorphism.
