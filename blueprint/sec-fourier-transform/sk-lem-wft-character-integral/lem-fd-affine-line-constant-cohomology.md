+++
id = "lem-fd-affine-line-constant-cohomology"
kind = "lemma"
title = "Constant cohomology of the affine line"
lean = ["AlgebraicGeometry.WeilSheaf.subsingleton_cohomology_adicConstant_affineLine"]
order = 3940
uses = ["def-fd-additive-character", "lem-sc-pic-affine", "sbc-thm-cohomological-dimension-of-an-affine-curve", "thm-sc-affine-cohomology", "def-sf-setting", "sk-prop-sfb-qlbar-colimit-x", "sk-prop-pe-continuous-cohomology", "sk-prop-scalar-six"]
+++
For $k$ finite or algebraically closed, with cohomology of the pro-étale
site and the coefficient sheaf $\overline{\mathbf Q}_{\ell}=p^*\underline{\overline{\mathbf Q}}_\ell$ of [def-sf-setting],

$$
H^q(\mathbf A^1_{\bar k},\overline{\mathbf Q}_\ell)=\begin{cases}\overline{\mathbf Q}_\ell,&q=0,\\0,&q>0.\end{cases}
$$
