+++
id = "lem-fd-character-orthogonality"
kind = "lemma"
title = "Orthogonality of additive characters"
order = 4144
lean = ["AddChar.sum_eq_ite"]
uses = ["def-fd-additive-character"]
+++
Let $k_0=\mathbf F_q$, let $\psi_a(x)=\psi(ax)$, and let $c\in\overline{\mathbf Q}_\ell$. Then

$$
\sum_{x\in k_0}c\ \psi_a(x)=\begin{cases}c\cdot q,&\psi_a=1,\\0,&\psi_a\neq1.\end{cases}
$$

In words: a nontrivial additive character sums to zero over the finite
field.
