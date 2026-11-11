+++
id = "lemma-normal-cones-contracting-ideals"
kind = "lemma"
title = "Normal cones and contracting ideals"
order = 1702
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.preimage_range_normalConeZeroSection", "AlgebraicGeometry.Scheme.IdealSheafData.range_normalConeMap_subset_range_normalConeZeroSection", "AlgebraicGeometry.Scheme.IdealSheafData.isPullback_normalConeZeroSection_normalConeMap"]
uses = ["definition-deformation-normal-bundle", "lemma-functoriality-deformation"]
+++
Let $c=(c_1,c_2):C\to X\times X$ be a correspondence, let
$Z\hookrightarrow X$ have ideal $I$,
and put

$$
I_1=c_1^{-1}(I)\mathcal O_C,\qquad
I_2=c_2^{-1}(I)\mathcal O_C,\qquad Z'=V(I_1).
$$

Assume that $I_2\subset I_1$ and $I_2^n\subset I_1^{n+1}$ for some $n\geq1$.
Over the trait $T=\operatorname{Spec}k[t]_{(t)}$, whose strict
henselization is the trait $S$ used for nearby cycles, the two legs
lift to the deformations to the normal cones,

$$
\widetilde c_i:\mathcal D_{Z'}C\longrightarrow\mathcal D_ZX,
\qquad
\mathcal D_ZX=
\operatorname{Spec}_{X_T}\mathcal O_{X_T}[I/t],
$$

where $\mathcal D_ZX$ is written over $T$ and $\mathcal D_{Z'}C$ is
defined in the same way from $I_1$. Their special fibres
$\gamma_i:N_{Z'}C\to N_ZX$ satisfy:

1. $\gamma_1^{-1}(Z)=Z'$ scheme-theoretically, where $Z$ and $Z'$
   are the zero sections of the two normal cones;
2. the image of $\gamma_2$ is set-theoretically contained in the
   zero section $Z\subset N_ZX$.
