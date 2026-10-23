+++
id = "def-nagata-immersion-into-fp-model"
kind = "definition"
title = "Finite-presentation immersion model"
lean = ["AlgebraicGeometry.Scheme.Hom.immersionModel", "AlgebraicGeometry.Scheme.Hom.immersionModelHom", "AlgebraicGeometry.Scheme.Hom.toImmersionModel", "AlgebraicGeometry.Scheme.Hom.immersionModel_spec"]
order = 79
uses = ["def-nagata-relative-stage-morphism-data", "lemma-nagata-relative-stage-morphism-data-exists"]
+++
Let $S$ be qcqs and let $X\to S$ be locally of finite type with $X$
quasi-compact and quasi-separated. Choose a finite-stage datum from
[lemma-nagata-relative-stage-morphism-data-exists], including indices
$\lambda_X$ and $\lambda_S$ and the descended morphism
$\varphi_{\lambda_X,\lambda_S}$. Define

$$
Y^{\mathrm{imm}}(X/S)
=X_{\lambda_X}\times_{S_{\lambda_S}}S
$$

using $\varphi_{\lambda_X,\lambda_S}$ and the comparison map
$S\to S_{\lambda_S}$. The compatibility equality in the finite-stage
datum induces the map $i^{\mathrm{imm}}\colon X\to Y^{\mathrm{imm}}(X/S)$
over $S$.
