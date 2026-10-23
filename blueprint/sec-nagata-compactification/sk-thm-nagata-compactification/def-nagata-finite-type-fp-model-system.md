+++
id = "def-nagata-finite-type-fp-model-system"
kind = "definition"
title = "Finite-presentation model system of a finite-type morphism"
order = 86
lean = ["AlgebraicGeometry.Scheme.Hom.FinitePresentationApproximation", "AlgebraicGeometry.Scheme.Hom.FinitePresentationApproximation.ofIsClosedImmersion", "AlgebraicGeometry.Scheme.Hom.closedModel", "AlgebraicGeometry.Scheme.Hom.finitePresentationApproximation"]
uses = ["def-nagata-closed-subscheme-fp-system", "def-nagata-immersion-into-fp-model", "def-nagata-immersion-shrink-to-closed"]
+++
A *finite-presentation approximation* of a morphism $f\colon X\to S$
consists of a cofiltered index category $A$, a system $(X_\alpha)_{\alpha\in A}$
of quasi-compact quasi-separated schemes of finite presentation over $S$
whose transition maps are closed immersions over $S$, and closed immersions
$i_\alpha\colon X\to X_\alpha$ compatible with the transition maps and with
$f$ (that is, $X_\alpha\to S$ composed with $i_\alpha$ is $f$), such that
the $i_\alpha$ exhibit $X$ as $\varprojlim_\alpha X_\alpha$.

For $X\to S$ locally of finite type with $X$ qcqs and $S$ qcqs, one such
system is obtained as follows: form
$i^{\mathrm{imm}}\colon X\to Y^{\mathrm{imm}}$, set
$Y^\circ=Y^{\mathrm{cl}}(i^{\mathrm{imm}})$, and apply
[def-nagata-closed-subscheme-fp-system] to
$X\hookrightarrow Y^\circ$. Denote the resulting system by

$$
\mathsf{FP}(X/S)=(A_{X/S},(X_\alpha)_\alpha),
$$

with structural maps $i_\alpha\colon X\to X_\alpha$.
