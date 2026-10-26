+++
id = "lem-pc-rf-base-change-flat-module"
kind = "lemma"
title = "Derived base change for a relatively flat module: the affine Čech form"
lean = ["AlgebraicGeometry.canonicalModuleBaseChange_isIso_affine_of_isFlatOver", "AlgebraicGeometry.Scheme.Modules.isIso_cechModuleComplexBaseChangeComparison"]
order = 730
uses = ["def-pc-base-change", "def-pc-derived-direct-image", "def-pc-derived-pullback", "def-pc-morphism-conventions", "lem-pc-cech-resolution", "lem-pc-flat-complex-derived-pullback"]
+++
Let $S=\operatorname{Spec}(A)$ be affine, let $f:X\to S$ be a separated
morphism, let $\mathcal U=(U_i)_{i\in I}$ be a finite cover of $X$ by affine
opens, and let $\mathcal G$ be a quasi-coherent $\mathcal O_X$-module flat
over $S$. By [lem-pc-cech-resolution] the Cech complex
$\check C^\bullet(\mathcal U,\mathcal G)$ represents $Rf_*\mathcal G$ in
$D(A)$; it is quasi-isomorphic to its truncation
$K=\tau^{\le |I|-1}\check C^\bullet(\mathcal U,\mathcal G)$, a bounded
complex of flat $A$-modules, so that for a morphism $g:T\to S$ from an
affine scheme $T=\operatorname{Spec}(B)$ the derived pullback
$Lg^*Rf_*\mathcal G$ is represented by $K\otimes_AB$. For every cartesian
square with bottom arrow such a $g$, with $f_T:X_T\to T$ and
$\mathcal G_T$ the pullback of $\mathcal G$, the canonical base-change map

$$
Lg^*Rf_*\mathcal G=K\otimes_AB\longrightarrow
\check C^\bullet(\mathcal U_T,\mathcal G_T)=Rf_{T,*}\mathcal G_T,
$$

induced by $K\to\check C^\bullet(\mathcal U,\mathcal G)$ and the
identification $\check C^\bullet(\mathcal U,\mathcal G)\otimes_AB=
\check C^\bullet(\mathcal U_T,\mathcal G_T)$ for the pulled back cover
$\mathcal U_T$, is an isomorphism in $D(B)$.
