+++
id = "def-nagata-relative-gluing-valid-stage"
kind = "definition"
title = "Cocycle-valid stage for the relative datum"
order = 367
lean = ["AlgebraicGeometry.RelativeAffinePresentation.ChartModels.relStage", "AlgebraicGeometry.RelativeAffinePresentation.ChartModels.validDatum"]
uses = ["def-nagata-directed-finite-upper-bound", "def-nagata-morphism-equality-stage", "def-nagata-qc-open-equality-stage", "def-nagata-relative-gluing-datum-descent", "lemma-nagata-filtered-colimit-finite-data"]
+++
For the raw datum, form the finite list of required gluing equalities, in
two rounds. First the open conditions: each chart's overlap with itself is
the whole chart, and the overlap map $a\to b$ carries
$V_{ab}\cap V_{ac}$ into $V_{bc}$. Each holds after base change to $S$,
hence past a selected equality stage; let the first-round stage be a common
bound of these stages and $\lambda_{\mathrm{raw}}(X/S)$. Then, for the
datum transported to that stage, the identity equations
$\psi_{aa}=\mathrm{id}$ and the triple-overlap cocycle equations, which
make sense once the open conditions hold, again hold past selected equality
stages. Define $\lambda_{\mathrm{rel}}(X/S)$ to be a common bound of these
and the first-round stage, and let $\mathsf R_{X,\lambda_{\mathrm{rel}}}$
be the raw datum transported to this stage.
