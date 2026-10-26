+++
id = "lem-pc-kbar-pure-insep"
kind = "lemma"
title = "The algebraic closure over a separably closed field"
lean = ["IsSepClosed.exists_isSeparable_pow_and_isPurelyInseparable"]
order = 808
uses = ["def-pc-field-tower", "def-pc-separably-closed", "lem-pc-sepclosed-finite-sep-trivial"]
+++
Let $k$ be a separably closed field
of exponential characteristic $p$ (so $p=1$ if $\operatorname{char}k=0$),
and let $K/k$ be an algebraic field extension, for instance $K=\bar k$.
Then every $\alpha\in K$ has an $n\ge0$ with $\alpha^{p^n}$ separable over
$k$; hence $K/k$ is purely inseparable.
