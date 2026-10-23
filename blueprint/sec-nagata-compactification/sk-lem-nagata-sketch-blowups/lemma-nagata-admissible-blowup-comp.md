+++
id = "lemma-nagata-admissible-blowup-comp"
kind = "lemma"
title = "Composition of admissible blow-ups, [stacks-project]"
order = 280
lean = ["AlgebraicGeometry.IsAdmissible.exists_comp"]
uses = ["def-nagata-admissible-blowup", "def-nagata-global-blowup", "lemma-nagata-admissible-blowup-over-open", "prop-nagata-global-blowup-cover-independent"]
+++
Let $X$ be quasi-compact and quasi-separated and let $U\subseteq X$ be an
open subscheme. Let $b_1\colon X_1=\operatorname{Bl}_{\mathcal I_1}(X)\to X$
be a $U$-admissible blow-up and let
$X_2=\operatorname{Bl}_{\mathcal I_2}(X_1)\to X_1$ be a
$b_1^{-1}(U)$-admissible blow-up. Then there are a finite type
quasi-coherent ideal $\mathcal K$ on $X$ with
$V(\mathcal K)\cap U=\varnothing$ and an isomorphism
$X_2\cong\operatorname{Bl}_{\mathcal K}(X)$ over $X$. In particular, the
composite $X_2\to X_1\to X$ is a $U$-admissible blow-up.
