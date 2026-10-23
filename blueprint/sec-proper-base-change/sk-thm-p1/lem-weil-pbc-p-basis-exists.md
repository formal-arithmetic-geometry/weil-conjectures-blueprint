+++
id = "lem-weil-pbc-p-basis-exists"
kind = "lemma"
title = "Every field of characteristic p has a p-basis"
uses = ["def-weil-field"]
lean = ["Field.exists_p_basis"]
order = 1908
+++
Let $p$ be a prime number, $k$ a field [def-weil-field] of characteristic $p$, and $k^p=\{a^p:a\in k\}$, a subfield of $k$. Then there is a family $(t_i)_{i\in I}$ of elements of $k$ (a $p$-basis of $k$) such that the monomials $t^E=\prod_{i\in I}t_i^{e_i}$, where $E=(e_i)_{i\in I}$ runs over the families of integers $0\le e_i<p$ with $e_i=0$ for all but finitely many $i$, form a basis of $k$ as a vector space over $k^p$.
