+++
id = "lem-pc-picard-functor-agrees-sc"
kind = "lemma"
title = "Agreement with the affine Picard functor of file 06"
lean = ["AlgebraicGeometry.algPicardFunctorIso", "AlgebraicGeometry.algPicardFunctorObjIso", "AlgebraicGeometry.picardFunctorAffineRestrictionIso"]
order = 636
uses = ["def-pc-fppf-site", "def-pc-picard-functor", "def-pc-picard-presheaf", "def-pc-scheme", "def-sc-picard-functor"]
+++
Let $k$ be a commutative ring and $X$ a scheme over $k$ (for instance a smooth
projective curve over a field $k$). The restriction of
$\operatorname{Pic}_{X/k}$ to affine $k$-schemes
$T=\operatorname{Spec}(R)$ is canonically the fppf sheafification, on the
category of $k$-algebras, of
$R\mapsto\operatorname{Pic}(X\times_k\operatorname{Spec} R)$;
more precisely
$\operatorname{Pic}_{X/k}(\operatorname{Spec}(R))=\operatorname{Pic}_{X/k}^{\mathrm{sc}}(R)$
naturally in $R$, where the right side is the value of this sheafification,
which for a curve over a field is the functor presented in
[def-sc-picard-functor]. More generally, for any morphism $f:X\to S$, the
restriction of $\operatorname{Pic}_{X/S}$ to affine $S$-schemes is the fppf
sheafification of the restriction of the Picard presheaf.
