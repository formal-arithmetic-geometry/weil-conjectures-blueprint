+++
id = "lem-pc-rf-perfect-base-change"
kind = "lemma"
title = "Perfectness of $Rf_*\\mathcal{G}$ and base change"
order = 681
uses = ["def-pc-base-change", "def-pc-derived-category", "def-pc-derived-direct-image", "def-pc-derived-pullback", "def-pc-morphism-conventions", "def-pc-perfect-complex", "lem-pc-projective-noetherian-rf-perfect", "lem-pc-rf-base-change-flat-module"]
+++
Let $S$ be a scheme, $f:X\to S$ a proper morphism of finite
presentation, and let $\mathcal{G}$ be an $\mathcal{O}_X$-module of finite presentation
and flat over $S$. Then $Rf_*\mathcal{G}$ is a perfect object of $D(\mathcal{O}_S)$,
and its formation commutes with arbitrary base change: for every
morphism $g:T\to S$ the canonical map

$$
Lg^*(Rf_*\mathcal{G})\;\longrightarrow\;Rf_{T,*}\mathcal{G}_T
$$

is an isomorphism in $D(\mathcal{O}_T)$.
