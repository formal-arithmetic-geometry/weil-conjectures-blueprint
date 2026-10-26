+++
id = "lem-weil-pbc-henselization-completion-data"
kind = "lemma"
title = "Canonical completion comparison from quotient-power isomorphisms"
lean = ["RingTheory.pair_henselization_completion_data"]
order = 1806
+++
Let $f:A\to B$ be a homomorphism of commutative rings and $I\subset A$ an ideal. Suppose the induced maps $q_n:A/I^n\to B/I^nB$ are bijective for every $n\geq1$. Put $J=IB$. For the adic completions $\widehat A_I=\varprojlim_nA/I^n$ and $\widehat B_J=\varprojlim_nB/J^n$, there is a ring isomorphism $\theta:\widehat A_I\xrightarrow{\sim}\widehat B_J$ such that, for every $n\geq0$, $x\in\widehat A_I$ and $a\in A$, if $x_n=a\bmod I^n$ then $(\theta x)_n=f(a)\bmod J^n$. If $c_A:A\to\widehat A_I$ and $c_B:B\to\widehat B_J$ are the completion maps, then $\theta^{-1}\circ c_B\circ f=c_A$.
