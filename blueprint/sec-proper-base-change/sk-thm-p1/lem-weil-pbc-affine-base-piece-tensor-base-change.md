+++
id = "lem-weil-pbc-affine-base-piece-tensor-base-change"
kind = "lemma"
title = "Tensor base change of a compatible spectrum model"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.affine_base_piece_tensor_base_change"]
order = 1656
+++
Let $d:T\to S$ be a morphism of schemes [def-pc-scheme], $X_0,Y_0$ schemes over $S$, and $f_0:X_0\to Y_0$ an $S$-morphism. Define $X_T,Y_T,f_T$ by base change. Let $V\subset Y_0$, $W\subset S$ be opens, $V_T=p_Y^{-1}(V)$, $U_T=f_T^{-1}(V_T)$ and $W_T=d^{-1}(W)$. Let $R,B,C$ be commutative rings with maps $a_B:R\to B$, $a_C:R\to C$ and an $R$-algebra map $\varphi:B\to C$. Suppose given $e_0:W_T\cong\operatorname{Spec}R$, $q:V_T\to W_T$ with $q\circ\iota_{W_T}=p_T\circ\iota_{V_T}$, $e_B:V_T\cong\operatorname{Spec}B$ and $e_C:U_T\cong\operatorname{Spec}C$. Assume $\operatorname{Spec}(a_B)\circ e_B=e_0\circ q$ and $\operatorname{Spec}(\varphi)\circ e_C=e_B\circ(f_T|_{V_T})$. Then for every $t:L\to T$, commutative $R$-algebra $A$, and $e:t^{-1}(W_T)\cong\operatorname{Spec}A$ satisfying $e_0\circ(t|_{W_T})=\operatorname{Spec}(R\to A)\circ e$, the base change of $f_0$ along $t\circ d$, restricted to the inverse image of $V$ under its target first projection, is isomorphic as an arrow to $\operatorname{Spec}(\mathrm{id}_A\otimes_R\varphi)$. No finite-type or limit hypothesis is needed.
