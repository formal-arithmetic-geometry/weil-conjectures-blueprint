+++
id = "lem-pc-very-ample-ample"
kind = "lemma"
title = "Ample line bundles from projective embeddings"
lean = ["AlgebraicGeometry.IsVeryAmple.pullback_of_field", "AlgebraicGeometry.IsAmple.pullback_of_field"]
order = 688
uses = ["def-pc-morphism-conventions", "def-sc-ample", "def-sc-invertible-module", "lem-pc-closed-imm-base-change"]
+++
Let $k$ be a field, let $i:X\hookrightarrow\mathbf{P}^n_k$ be a closed immersion
and let $\mathcal{L}:=i^*\mathcal{O}_{\mathbf{P}^n}(1)$. Then $\mathcal{L}$ is
ample on $X$; in particular the base change
$\mathcal{L}\otimes_k K$ is ample on $X_K$ for every field extension $K/k$.
