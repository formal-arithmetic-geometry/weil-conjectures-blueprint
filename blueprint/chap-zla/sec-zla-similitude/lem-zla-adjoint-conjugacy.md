+++
id = "lem-zla-adjoint-conjugacy"
kind = "lemma"
title = "Adjoint conjugacy"
order = 1031
uses = ["def-zla-similitude-pairing"]
+++
Let $B:V\times W\to E$ be a perfect similitude pairing of multiplier $\mu$ for
the automorphisms $F_V,F_W$. Then

$$
\phi_BF_W=\mu\,(F_V^{-1})^\vee\phi_B,
$$

so $F_W$ is conjugate to $\mu\,(F_V^{-1})^\vee$.

## Proof

Evaluate both sides at $w\in W$ and then at $v\in V$: the left side gives
$B(v,F_Ww)$ and the right side gives $\mu B(F_V^{-1}v,w)$, and these agree by
the similitude identity applied to the pair $(F_V^{-1}v,w)$. Since $\phi_B$
is an isomorphism, the displayed identity exhibits the conjugacy.
