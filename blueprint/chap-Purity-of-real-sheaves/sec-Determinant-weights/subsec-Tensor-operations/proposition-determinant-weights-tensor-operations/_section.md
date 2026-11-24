+++
id = "proposition-determinant-weights-tensor-operations"
kind = "proposition"
title = "Determinant weights of tensor operations"
order = 1148
uses = ["definition-determinant-weight", "definition-weil-representation"]
+++
Let $V$ and $V'$ be nonzero [Weil representations](@definition-weil-representation), let $A_1,\ldots,A_t$ be
the composition factors of $V$, and put $\gamma_a=\href{@definition-determinant-weight}{\operatorname{dw}_\iota(A_a)}$.

1. $\href{@definition-determinant-weight}{\operatorname{DW}(V\otimes V')}=\href{@definition-determinant-weight}{\operatorname{DW}(V)}+\href{@definition-determinant-weight}{\operatorname{DW}(V')}$.
2. $\href{@definition-determinant-weight}{\operatorname{DW}(\bigwedge^rV)}=\bigl\{\sum_an_a\gamma_a :
      0\le n_a\le\dim A_a,\ \sum_an_a=r\bigr\}$ for $0\le r\le\dim V$.
3. $\href{@definition-determinant-weight}{\operatorname{DW}(V^\vee)}=-\operatorname{DW}(V)$.
