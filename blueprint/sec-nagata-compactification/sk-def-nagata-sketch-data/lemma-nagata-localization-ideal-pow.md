+++
id = "lemma-nagata-localization-ideal-pow"
kind = "lemma"
title = "Localization commutes with powers of an ideal"
order = 37
lean = ["Ideal.map_pow"]
+++
Let $\varphi\colon A\to B$ be a ring homomorphism and $I\subseteq A$ an
ideal. For every $n$,

$$
(I^n)B=(IB)^n.
$$

In particular $(I^n)A_s=(IA_s)^n$ for $s\in A$.

## Proof

Extension of ideals along a ring homomorphism preserves products and the
unit ideal. Induct on $n$.
