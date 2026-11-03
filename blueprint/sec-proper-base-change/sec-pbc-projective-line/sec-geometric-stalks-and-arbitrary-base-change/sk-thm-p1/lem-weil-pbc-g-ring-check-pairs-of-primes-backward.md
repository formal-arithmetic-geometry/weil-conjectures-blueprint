+++
id = "lem-weil-pbc-g-ring-check-pairs-of-primes-backward"
kind = "lemma"
title = "Backward implication of G-ring criterion"
uses = ["def-weil-pbc-g-ring"]
lean = ["isGRing_pairsOfPrimes_backward"]
order = 1921
+++
Let $R$ be a Noetherian ring. For prime ideals $\mathfrak q\subseteq\mathfrak p$ of $R$, write $\bar{\mathfrak p}=\mathfrak p/\mathfrak q$ for the image of $\mathfrak p$ in $R/\mathfrak q$, let $L=(R/\mathfrak q)_{\bar{\mathfrak p}}$, let $\hat L$ be its completion with respect to its maximal ideal, and let $F_{\mathfrak q,\mathfrak p}=\kappa(\mathfrak q)\otimes_{R/\mathfrak q}\hat L$ be the formal fibre of $\hat L$ over the generic point of $R/\mathfrak q$. If for every such pair $\mathfrak q\subseteq\mathfrak p$ the ring $F_{\mathfrak q,\mathfrak p}$ is Noetherian and geometrically regular over $\kappa(\mathfrak q)$, then $R$ is a G-ring [def-weil-pbc-g-ring].
