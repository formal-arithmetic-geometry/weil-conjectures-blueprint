+++
id = "lem-pc-picard-functor-agrees-sc"
kind = "lemma"
title = "Agreement with the affine Picard functor of file 06"
lean = ["AlgebraicGeometry.algPicardFunctorIso", "AlgebraicGeometry.algPicardFunctorObjIso", "AlgebraicGeometry.picardFunctorAffineRestrictionIso"]
order = 811
uses = ["def-pc-fppf-site", "def-pc-picard-functor", "def-pc-picard-presheaf", "def-pc-scheme", "def-sc-picard-functor"]
+++
Let $k$ be a field and $X$ a
smooth projective curve over
$k$. The restriction of
$\operatorname{Pic}_{X/k}$ to affine $k$-schemes
$T=\operatorname{Spec}(R)$ is canonically the sheafification presented in
[def-sc-picard-functor], namely the fppf sheafification of
$R\mapsto\operatorname{Pic}(X\times_k\operatorname{Spec} R)$;
more precisely
$\operatorname{Pic}_{X/k}(\operatorname{Spec}(R))=\operatorname{Pic}_{X/k}^{\mathrm{sc}}(R)$ where
the right side is the value of the functor of [def-sc-picard-functor].
