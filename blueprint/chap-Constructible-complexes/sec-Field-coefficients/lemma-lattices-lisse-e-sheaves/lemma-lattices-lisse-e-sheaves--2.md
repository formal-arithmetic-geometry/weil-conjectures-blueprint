+++
id = "lemma-lattices-lisse-e-sheaves--2"
kind = "lemma"
title = "Étale-local integral lattices"
name_showing = false
order = 260002
aliases = ["bp-r077-2"]
lean = ["AlgebraicGeometry.ProEtale.exists_lisse_lattice_etale_local", "AlgebraicGeometry.ProEtale.CondensedRing.continuousLisse_etale_lattice"]
uses = ["definition-small-pro-etale-site", "definition-lisse-sheaves", "definition-lattice", "lemma-comparison-completed-coefficients", "proposition-topos-functoriality", "lemma-inverse-image-coefficient-sheaves"]
+++
Let $E/\mathbf Q_\ell$ be finite, let $X$ be a scheme, and let $L$ be an
$E_X$-module on $X_{\mathrm{pro}\acute{e}t}$ which is locally free of finite rank.
There is an étale covering $\{f_i:Y_i\to X\}_{i\in I}$ and, for every $i$,
a locally free $\mathcal O_{E,Y_i}$-module $M_i$ of finite rank with an
isomorphism

$$
M_i\otimes_{\mathcal O_{E,Y_i}}E_{Y_i}\simeq f_i^{-1}L.
$$

If the underlying topological space of $X$ is noetherian, there is a
surjective étale morphism $p:U\to X$ with $U$ quasi-compact and
quasi-separated, and a locally free $\mathcal O_{E,U}$-module $M$ of finite
rank such that

$$
M\otimes_{\mathcal O_{E,U}}E_U\simeq p^{-1}L.
$$

The ranks may vary, and rank zero and the empty scheme are allowed.
