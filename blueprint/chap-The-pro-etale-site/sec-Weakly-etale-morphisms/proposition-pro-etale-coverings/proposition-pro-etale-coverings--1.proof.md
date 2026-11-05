+++
kind = "proof"
of = "proposition-pro-etale-coverings--1"
order = 36004
uses = ["definition-small-pro-etale-site", "lemma-stability"]
+++
A covering sieve contains a covering family
$\{Z_j\to U\}_{j\in J}$ for the precoverage of
[definition-small-pro-etale-site]. Since $U$ is quasi-compact, the
quasi-compact covering condition gives finitely many affine opens
$V_i\subset Z_{j_i}$ whose images cover $U$. Each $V_i$ is again an
object of the site by [lemma-stability]. The composites $V_i\to U$
belong to $R$, since a sieve is closed under precomposition.

These composites are weakly étale and jointly surjective. They are
quasi-compact morphisms because their sources are affine and their
target is quasi-separated. A finite jointly surjective family of
quasi-compact morphisms satisfies the quasi-compact covering condition,
so this family belongs to the pro-étale precoverage. Its generated
sieve is therefore covering.
