+++
id = "lem-pc-projection-formula"
kind = "lemma"
title = "The projection formula"
lean = ["AlgebraicGeometry.Scheme.Modules.higherDirectImageTensorObjPullbackIso", "AlgebraicGeometry.Scheme.Modules.nonempty_higherDirectImage_tensorObj_pullback_iso"]
order = 836
uses = ["def-pc-base-change", "def-pc-derived-direct-image", "def-sc-invertible-module"]
+++
Let $f:X\to Y$ be a morphism of schemes, let $\mathcal{F}$ be an
$\mathcal{O}_X$-module and let $\mathcal{N}$ be an invertible
$\mathcal{O}_Y$-module. Then for every $q\ge0$ there is an isomorphism of
$\mathcal{O}_Y$-modules

$$
R^qf_*\bigl(\mathcal{F}\otimes_{\mathcal{O}_X}f^*\mathcal{N}\bigr)\;\cong\;
R^qf_*(\mathcal{F})\otimes_{\mathcal{O}_Y}\mathcal{N}.
$$
