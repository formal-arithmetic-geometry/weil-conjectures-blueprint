+++
id = "corollary-purity-cohomology-smooth-proper-variety"
kind = "corollary"
title = "Purity of the cohomology of a smooth proper variety"
order = 1372
lean = ["AlgebraicGeometry.WeilSheaf.isPureOfWeightOver_cohomology_adicConstant", "AlgebraicGeometry.WeilSheaf.deligne_purity"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-weights", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $X_0/\mathbf F_q$ be smooth proper of pure dimension $d$, put
$X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$, let $\ell\nmid q$
be a prime, and let
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$ be a field
embedding. Then every geometric Frobenius eigenvalue $\alpha$ on
$H^i(X_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)$ satisfies

$$
|\iota(\alpha)|=q^{i/2}.
$$
