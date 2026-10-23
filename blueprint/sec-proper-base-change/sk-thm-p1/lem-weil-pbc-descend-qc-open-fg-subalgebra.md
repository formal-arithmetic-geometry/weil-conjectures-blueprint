+++
id = "lem-weil-pbc-descend-qc-open-fg-subalgebra"
kind = "lemma"
title = "A quasi-compact open of a base change X_A is defined over a finitely generated subalgebra"
uses = ["def-pc-base-change"]
lean = ["AlgebraicGeometry.descend_qc_open_fg_subalgebra"]
order = 1715
+++
Let $k$ be a field, let $X$ be a scheme over $k$ and let $A$ be a commutative $k$-algebra. For a $k$-subalgebra $A'\subseteq A$ write $X_{A'}=X\times_{\operatorname{Spec}k}\operatorname{Spec}A'$ and $X_A=X\times_{\operatorname{Spec}k}\operatorname{Spec}A$ for the base changes [def-pc-base-change], and $\pi:X_A\to X_{A'}$ for the morphism $\mathrm{id}_X\times\operatorname{Spec}(A'\hookrightarrow A)$ induced by the inclusion. Let $V\subseteq X_A$ be a quasi-compact open subset. Then there are a $k$-subalgebra $A'\subseteq A$ that is finitely generated as a $k$-algebra and a quasi-compact open subset $V'\subseteq X_{A'}$ such that $V=\pi^{-1}(V')$. (No separatedness or quasi-separatedness of $X$ is assumed.)
