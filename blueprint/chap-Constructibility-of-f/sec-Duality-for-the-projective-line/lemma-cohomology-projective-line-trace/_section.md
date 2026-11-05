+++
id = "lemma-cohomology-projective-line-trace"
kind = "lemma"
title = "Cohomology of the projective line and the trace"
order = 545
lean = ["AlgebraicGeometry.ProEtale.geoP1Cohomology", "AlgebraicGeometry.ProEtale.geoP1DecompositionMap", "AlgebraicGeometry.ProEtale.geoP1Trace"]
uses = ["definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-pro-etale-base-change-map"]
+++
Let $\Lambda$ be a finite commutative $\ell$-primary ring, let $S$ be a
Noetherian scheme on which $\ell$ is invertible, and let
$p:\mathbf P^1_S\to S$ be the projection. The unit
$\Lambda_S\to Rp_*\Lambda_{\mathbf P^1_S}$ and the class
$c_1(\mathcal O_{\mathbf P^1_S}(1))$ define an isomorphism

$$
\sigma_S:\Lambda_S\oplus\Lambda_S(-1)[-2]
\ \xrightarrow{\ \sim\ }\ Rp_*\Lambda_{\mathbf P^1_S}
\quad\text{in }D^+(S_{\acute{e}t},\Lambda),
\tag{6.2}
$$

compatible with base change in the sense that for $g:S'\to S$ with $S'$
Noetherian, the base change map $g^*Rp_*\Lambda\to Rp'_*\Lambda$ carries $g^*\sigma_S$ to $\sigma_{S'}$. Let

$$
\operatorname{Tr}_p:Rp_*\Lambda_{\mathbf P^1_S}(1)[2]\longrightarrow\Lambda_S
\tag{6.3}
$$

be the morphism given by the projection
onto the summand $\Lambda_S$ of the twist of $\sigma_S$.
Then $\operatorname{Tr}_p$ is compatible with every Noetherian base
change.
