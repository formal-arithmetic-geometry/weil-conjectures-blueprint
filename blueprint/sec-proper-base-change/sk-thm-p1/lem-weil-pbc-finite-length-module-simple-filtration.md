+++
id = "lem-weil-pbc-finite-length-module-simple-filtration"
kind = "lemma"
title = "A finite-length module has a filtration with simple quotients"
lean = ["Module.exists_simple_filtration_of_length_lt_top"]
order = 1782
+++
Let $R$ be a commutative ring and $M$ an $R$-module of finite length, i.e. $\mathrm{length}_R(M)<\infty$. Then there are an integer $r\ge0$ and $R$-submodules $0=M_0\subsetneq M_1\subsetneq\cdots\subsetneq M_r=M$ such that each quotient $M_i/M_{i-1}$ ($1\le i\le r$) is simple: it is nonzero and has no $R$-submodule other than $0$ and itself.
