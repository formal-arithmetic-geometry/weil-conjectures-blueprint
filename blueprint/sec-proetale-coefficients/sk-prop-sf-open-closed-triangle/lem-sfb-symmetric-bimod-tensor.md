+++
id = "lem-sfb-symmetric-bimod-tensor"
kind = "lemma"
title = "Tensor products of symmetric bimodules are symmetric"
order = 1148
uses = ["lem-sfb-modobj-symmetric-bimodules"]
lean = ["Bimod.IsSymmetric.tensorBimod"]
+++
Let $\mathcal C$ be a braided monoidal category with coequalizers such that $X\otimes-$ and
$-\otimes X$ preserve colimits for every $X$, and let $A$ be a monoid object. For
$A$-$A$-bimodules $P$ and $Q$ with actions $\gamma_P,\rho_P,\gamma_Q,\rho_Q$, the tensor
product over $A$ is the coequalizer
$$
P\otimes_AQ=\operatorname{coeq}\bigl(P\otimes A\otimes Q\rightrightarrows P\otimes Q\bigr)
$$
of $\rho_P\otimes Q$ and $(P\otimes\gamma_Q)\alpha_{P,A,Q}$. Here $A$ acts on the left
through $P$ and on the right through $Q$. If $P$ and $Q$ are symmetric in the sense of
[lem-sfb-modobj-symmetric-bimodules], then so is $P\otimes_AQ$.
