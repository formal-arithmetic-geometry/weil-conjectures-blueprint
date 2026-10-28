+++
id = "lemma-nagata-admissible-blowup-preserves-density"
kind = "lemma"
title = "Density is preserved by an admissible blow-up"
order = 123
lean = ["AlgebraicGeometry.IsAdmissible.isSchemeTheoreticallyDominant_preimage_ι", "AlgebraicGeometry.Scheme.IdealSheafData.isSchemeTheoreticallyDominant_blowupMap_preimage_compl_support"]
uses = ["def-nagata-admissible-blowup", "def-nagata-dense-compactification", "def-nagata-global-blowup", "def-nagata-scheme-theoretically-dense-open", "prop-nagata-global-blowup-cover-independent"]
+++
Let $\mathcal I$ be a quasi-coherent ideal on a scheme $X$. Then the inverse
image of $X\setminus V(\mathcal I)$ is scheme-theoretically dense in
$\operatorname{Bl}_{\mathcal I}(X)$. Moreover, let $U\subseteq X$ be an open
subscheme such that $U\hookrightarrow X$ is quasi-compact and
scheme-theoretically dense, and let $\operatorname{Bl}_{\mathcal I}(X)\to X$
be a $U$-admissible blow-up (so $\mathcal I$ is of finite type and
$V(\mathcal I)\cap U=\varnothing$). Then the inverse image of $U$ is
scheme-theoretically dense in $\operatorname{Bl}_{\mathcal I}(X)$.
