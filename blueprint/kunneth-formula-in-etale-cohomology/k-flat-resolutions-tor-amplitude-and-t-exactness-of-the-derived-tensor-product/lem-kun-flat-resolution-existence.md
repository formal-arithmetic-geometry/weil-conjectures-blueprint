+++
id = "lem-kun-flat-resolution-existence"
kind = "lemma"
title = "Flat K-flat resolutions"
order = 6087
lean = ["AlgebraicGeometry.Etale.exists_kflat_flat_resolution"]
uses = ["def-kun-derived-tensor", "def-kun-truncations", "lem-kun-kflat-criteria", "lem-kun-bounded-flat-replacement", "lem-kun-hocolim-truncations", "lem-kun-complex-colimit-hocolim"]
+++
Let $\Lambda$ be a commutative ring and $T$ a scheme. Every complex
$\mathcal G^\bullet$ of $\Lambda_T$-module sheaves on the small étale site
of $T$ admits a quasi-isomorphism
$\mathcal K^\bullet\to\mathcal G^\bullet$ from a K-flat
[def-kun-derived-tensor] complex whose terms are flat $\Lambda_T$-module
sheaves.

(*Source:* the argument is the one of Stacks Project, [Lemma 21.17.11, Tag
06YS](https://stacks.math.columbia.edu/tag/06YS), with the successive
approximations replaced by the functorial replacement
[lem-kun-bounded-flat-replacement].)

## Proof

Choose a K-injective resolution $I^\bullet$ of $\mathcal G^\bullet$, and for
every $N$ let $\mathcal F_N^\bullet=\tau_{\le N}I^\bullet$ be the truncation
of [def-kun-truncations], a complex vanishing above $N$. Applying the
functorial replacement $\Phi$ of [lem-kun-bounded-flat-replacement] to
$\mathcal F_N^\bullet$ with the bound $N+1$ produces a bounded-above complex
$\mathcal E_N^\bullet=\Phi(\mathcal F_N^\bullet)$ of flat sheaves with a
termwise surjective quasi-isomorphism
$\mathcal E_N^\bullet\to\mathcal F_N^\bullet$; since
$\mathcal F_N^\bullet\to\mathcal F_{N+1}^\bullet$ is a map between complexes
vanishing above $N+1$, functoriality gives compatible maps
$\mathcal E_N^\bullet\to\mathcal E_{N+1}^\bullet$.

Each $\mathcal E_N^\bullet$ is a bounded-above complex of flat sheaves,
hence K-flat by [lem-kun-kflat-criteria](1); therefore the homotopy colimit
$\mathcal K^\bullet=\operatorname{hocolim}_N\mathcal E_N^\bullet$, which is
the cone of a map between countable direct sums of the
$\mathcal E_N^\bullet$, is K-flat and has flat terms by
[lem-kun-kflat-criteria](2) (direct sums and cones of K-flat complexes are
K-flat, and direct sums of flat sheaves are flat).

The homotopy colimit of the compatible quasi-isomorphisms
$\mathcal E_N^\bullet\to\mathcal F_N^\bullet$ is the termwise colimit of a
filtered system of quasi-isomorphisms by
[lem-kun-complex-colimit-hocolim], hence a quasi-isomorphism because
homology commutes with filtered colimits; and
$\operatorname{hocolim}_N\mathcal F_N^\bullet\cong I^\bullet$ by
[lem-kun-hocolim-truncations], since $I^\bullet$ represents
$\mathcal G^\bullet$ in $D(T_{\Et},\Lambda)$. The composite
$\mathcal K^\bullet\to\mathcal G^\bullet$ is therefore the required
quasi-isomorphism.

Unresolved dependencies: def:weil-pbc-etale-site, prop:weil-pbc-kinjective-resolutions-exist, def:weil-pbc-derived-categories
