+++
id = "lem-weil-pbc-scheme-coproduct-copies"
kind = "lemma"
title = "Coproduct of copies of a scheme is etale over it"
uses = ["def-pc-scheme", "def-weil-open-immersion", "def-pc-fibre-product", "def-weil-etale-morphism", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.sigmaOpenCover, AlgebraicGeometry.isEmpty_pullback_sigmaι_of_ne, AlgebraicGeometry.IsZariskiLocalAtSource.sigmaDesc, AlgebraicGeometry.IsOpenImmersion.mono"]
tags = ["sheaf-dag", "mathlib", "stacks-01JA"]
+++
Let $T$ be a scheme [def-pc-scheme] and $I$ a countable set. The coproduct $U=\coprod_{i\in I}T$ exists in the category of schemes; each coprojection $\iota_i:T\to U$ is an open immersion [def-weil-open-immersion], in particular a monomorphism, so $T\times_{\iota_i,U,\iota_i}T=T$; the images of the $\iota_i$ cover $U$; for $i\ne j$ the fibre product $T\times_{\iota_i,U,\iota_j}T$ [def-pc-fibre-product] is the empty scheme; and the codiagonal $\nabla:U\to T$ (the morphism with $\nabla\circ\iota_i=\mathrm{id}_T$ for all $i$) is etale [def-weil-etale-morphism], so $(U,\nabla)$ is an object of the small etale site $T_{\Et}$ and $\{\iota_i:T\to U\}_{i\in I}$ is a covering of $U$ in $T_{\Et}$ [def-weil-pbc-etale-site].
