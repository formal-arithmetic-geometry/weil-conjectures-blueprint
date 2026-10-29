+++
id = "lem-weil-pbc-intersection-subfields-subspace"
kind = "lemma"
title = "A subspace meeting K_alpha^n for a directed family with intersection k meets k^n"
lean = ["IntermediateField.exists_ne_zero_mem_base_iff_forall_mem_intermediateField"]
order = 1945
+++
Let $K/k$ be a field extension, $k$ regarded as a subfield of $K$. Let $(K_\alpha)_{\alpha\in\mathcal A}$ be a family of subfields of $K$, indexed by a nonempty set $\mathcal A$, such that (1) $k\subseteq K_\alpha$ for all $\alpha\in\mathcal A$; (2) $k=\bigcap_{\alpha\in\mathcal A}K_\alpha$; (3) for $\alpha,\alpha'\in\mathcal A$ there is $\alpha''\in\mathcal A$ with $K_{\alpha''}\subseteq K_\alpha\cap K_{\alpha'}$. For a subfield $F\subseteq K$ and $n\ge1$ write $F^{\oplus n}\subseteq K^{\oplus n}$ for the set of vectors all of whose coordinates lie in $F$. Then for every $n\ge1$ and every $K$-linear subspace $V\subseteq K^{\oplus n}$ we have $V\cap k^{\oplus n}\ne0$ if and only if $V\cap K_\alpha^{\oplus n}\ne0$ for every $\alpha\in\mathcal A$.
