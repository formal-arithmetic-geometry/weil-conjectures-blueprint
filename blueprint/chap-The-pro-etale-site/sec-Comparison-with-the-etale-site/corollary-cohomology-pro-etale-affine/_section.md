+++
id = "corollary-cohomology-pro-etale-affine"
kind = "corollary"
title = "Cohomology of a pro-étale affine"
order = 126
lean = ["AlgebraicGeometry.ProEtale.exists_cohomologyRestrictOver_eq_of_isLimit", "AlgebraicGeometry.ProEtale.exists_cohomologyRestrictOver_eq_zero_of_isLimit"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image"]
+++
Let $K\in D^+(X_{\acute{e}t},\Lambda)$, and let $U=\varprojlim_iU_i$ be a
pro-étale affine with $U_i$ affine and étale over $X$. Then there is
an isomorphism

$$
R\Gamma(U_{\mathrm{pro}\acute{e}t},(\nu_X^*K)|_U)
\simeq \varinjlim_i R\Gamma((U_i)_{\acute{e}t},K|_{U_i}).
\tag{2.8}
$$
