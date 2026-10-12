+++
id = "lem-weil-pbc-change-ideal-completion"
kind = "lemma"
title = "Completions along two ideals each containing a power of the other agree"
lean = ["changeIdealCompletion"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma Tag 0319 (lemma-change-ideal-completion, line 22806); proof: the systems of maps M/I^nM -> M/J^{floor(n/c)}M and M/J^mM -> M/I^{floor(m/d)}M give mutually inverse maps of the completions"
+++
Let $A$ be a commutative ring, $I,J\subseteq A$ ideals and $c,d\ge1$ integers with $I^c\subseteq J$ and $J^d\subseteq I$. Let $M$ be an $A$-module, $M^\wedge_I=\varprojlim_nM/I^nM$ and $M^\wedge_J=\varprojlim_nM/J^nM$ (compatible sequences, componentwise $A$-module structure), with canonical maps $\iota_I:M\to M^\wedge_I$, $\iota_J:M\to M^\wedge_J$, $x\mapsto(x\bmod I^nM)_n$ resp. $(x\bmod J^nM)_n$. Then the map $\theta:M^\wedge_J\to M^\wedge_I$, $(x_n)_n\mapsto(x_{dk}\bmod I^kM)_k$ (well defined since $J^{dk}M\subseteq I^kM$) is an isomorphism of $A$-modules with inverse $(y_k)_k\mapsto(y_{cn}\bmod J^nM)_n$ (well defined since $I^{cn}M\subseteq J^nM$), and $\theta\circ\iota_J=\iota_I$. In particular $M$ is $I$-adically complete ($\iota_I$ bijective) if and only if it is $J$-adically complete. For $M=A$ (where $M^\wedge_I=\varprojlim_nA/I^n$ with componentwise multiplication) $\theta$ is an isomorphism of rings.
