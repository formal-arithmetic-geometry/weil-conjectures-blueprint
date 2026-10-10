+++
id = "lemma-nagata-conrad-dense-in-admissible-blowup"
kind = "lemma"
title = "Density in an admissible blow-up"
order = 175
lean = ["AlgebraicGeometry.IsAdmissible.dense_coe_preimage_blowupMap", "AlgebraicGeometry.IsAdmissible.dense_preimage_blowupMap_of_qcqs", "AlgebraicGeometry.Scheme.IdealSheafData.isSchemeTheoreticallyDominant_blowupMap_preimage_compl_support"]
uses = ["def-nagata-admissible-blowup", "def-nagata-dense-compactification", "def-nagata-global-blowup", "def-nagata-scheme-theoretically-dense-open", "lemma-nagata-admissible-blowup-preserves-density", "lemma-nagata-blowup-proper", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-global-blowup-complement", "thm-nagata-global-blowup-proper"]
+++
Let $X$ be qcqs, let $U\subseteq X$ be an open subscheme, and let
$\pi\colon\widetilde X=\operatorname{Bl}_{\mathcal I}(X)\to X$ be a
$U$-admissible blow-up. If $D\subseteq X$ is a dense subset, then
$\pi^{-1}(D)$ is dense in $\widetilde X$; in particular, if $D$ is a dense
open subset of $X$, then $\pi^{-1}(D)$ is a dense open subset of
$\widetilde X$. If moreover $V(\mathcal I)=X\setminus U$, then
$\pi^{-1}(U)$ is scheme-theoretically dense in $\widetilde X$.
