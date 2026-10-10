+++
id = "lem-wf-envelope-real"
kind = "lemma"
title = "The envelope is real"
order = 2765
uses = ["def-weil-punctual-weights", "def-wf-iota-real", "def-wf-normalized-real-envelope"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.isReal_realEnvelope", "AlgebraicGeometry.LAdicWeilSheaf.IsLisse.realEnvelope"]
+++
Let $\mathcal F$ be a Weil sheaf, punctually $\iota$-pure of weight $w$,
and let $b\in\Qlb^\times$ with $|\iota(b)|=q^{-w/2}$ (for instance
$b=\iota^{-1}(q^{-w/2})$). Then the envelope
$\operatorname{Env}_\iota(\mathcal F;b)$ of
[def-wf-normalized-real-envelope] is $\iota$-real in the sense of
[def-wf-iota-real]. If $\mathcal F$ is lisse, so is
$\operatorname{Env}_\iota(\mathcal F;b)$.

## Proof

At a closed point $y$, the local characteristic factor of the
envelope is the product of the local factors of the two summands, with
eigenvalues $\beta_j$ (of $\mathcal F^0_{\bar y}$) and
$\beta_j^{-1}$ (of its dual), where
$|\iota(\beta_j)|=1$: if $y$ has degree $m$, each $\beta_j$ is
$b^m\alpha$ for an eigenvalue $\alpha$ of $F_y$ on $\mathcal F_{\bar y}$,
and $|\iota(b^m\alpha)|=q^{-mw/2}\,q_y^{w/2}=1$ by the punctual purity of
[def-weil-punctual-weights] and the normalization of $b$. Hence

$$
\iota\bigl(\beta_j^{-1}\bigr)=\overline{\iota(\beta_j)}
$$

($\overline z=|z|^2z^{-1}=z^{-1}$ for $|z|=1$), so the local
eigenvalue multiset is stable under complex conjugation; by
[def-wf-iota-real] the envelope is $\iota$-real.

If $\mathcal F$ is lisse, then $\mathcal F^0$, which has the same
underlying étale sheaf, is lisse, and so are its dual and the finite
direct sum $\mathcal F^0\oplus(\mathcal F^0)^\vee$, duals and finite
direct sums of locally constant sheaves of finite rank being locally
constant of finite rank.
