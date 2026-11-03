+++
id = "def-weil-pbc-formally-smooth-adic"
kind = "definition"
title = "Formally smooth for an adic topology on the target"
lean = ["Algebra.FormallySmoothAdic"]
order = 1755
+++
Let $\varphi:R\to S$ be a homomorphism of commutative rings, making $S$ an $R$-algebra, and $\mathfrak n\subseteq S$ an ideal. $S$ is *formally smooth over $R$ for the $\mathfrak n$-adic topology* (also: $\varphi$ is formally smooth for the $\mathfrak n$-adic topology) if the following lifting property holds: for every commutative $R$-algebra $D$, every ideal $J\subseteq D$ with $J^2=0$, with quotient map $q:D\to D/J$, and every homomorphism of $R$-algebras $g:S\to D/J$ with $g(\mathfrak n^k)=0$ for some $k\ge1$, there is a homomorphism of $R$-algebras $f:S\to D$ with $q\circ f=g$. (Compare Stacks Project, More on Algebra, Definition 07NI.)
