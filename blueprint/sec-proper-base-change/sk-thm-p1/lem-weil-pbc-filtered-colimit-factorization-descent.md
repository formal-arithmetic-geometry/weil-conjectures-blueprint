+++
id = "lem-weil-pbc-filtered-colimit-factorization-descent"
kind = "lemma"
title = "Finite monic factorization data descends in a filtered colimit of pairs"
lean = ["filteredColimit_factorization_descent"]
order = 1741
+++
Let $\Lambda$ be a nonempty directed preorder and $i\mapsto A_i$ a functor from $\Lambda$ to commutative rings with colimit $A=\varinjlim_iA_i$ and coprojections $\iota_i:A_i\to A$. Let $J_i\subseteq A_i$ be ideals with $A_i\to A_j$ mapping $J_i$ into $J_j$ for $i\le j$, and let $I\subseteq A$ be an ideal whose elements are exactly the elements $\iota_i(a)$ with $i\in\Lambda$ and $a\in J_i$. Let $f\in A[X]$ be monic and $g_0,h_0\in(A/I)[X]$ coprime monic polynomials with $f\bmod I=g_0h_0$. Then there are a stage $i$ and monic polynomials $f_i,g_i,h_i\in A_i[X]$ such that $\iota_i(f_i)=f$, the reductions of $g_i$ and $h_i$ modulo $J_i$ are coprime and their product is $f_i\bmod J_i$, and the images of $\iota_i(g_i)$ and $\iota_i(h_i)$ modulo $I$ are $g_0$ and $h_0$. No pair $(A_i,J_i)$ is assumed henselian.
