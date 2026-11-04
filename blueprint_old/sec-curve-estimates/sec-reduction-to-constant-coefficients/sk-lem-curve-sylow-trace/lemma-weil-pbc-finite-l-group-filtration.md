+++
id = "lemma-weil-pbc-finite-l-group-filtration"
kind = "lemma"
title = "Finite $\\ell$-group representation filtration"
lean = ["Representation.invariants_ne_bot_and_exists_filtration_of_isPGroup"]
order = 1613
+++
Let $H$ be an $\ell$-group (every element has $\ell$-power order; $H$ need
not be finite) and $V$ a finite-dimensional $\mathbf F_\ell$-linear
representation of $H$, of dimension $n$. If $V\neq0$ then $V^H\ne0$. Moreover
there is a flag $0=F_0\subseteq F_1\subseteq\cdots\subseteq F_n=V$ of
$H$-stable subspaces with $\dim F_i=i$ such that $H$ acts trivially on each
$F_{i+1}/F_i$, i.e. $hx-x\in F_i$ for $h\in H$ and $x\in F_{i+1}$; its
successive quotients are the trivial one-dimensional representation.
