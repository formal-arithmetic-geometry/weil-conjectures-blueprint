+++
kind = "proof"
of = "lemma-stability--6"
order = 32014
+++
Write $B=\varinjlim_iB_i$ with each $B_i$ étale over $R$. Base
change preserves this filtered colimit, giving
$$
R'\otimes_RB=\varinjlim_i(R'\otimes_RB_i).
$$
Each term is étale over $R'$ because étale ring maps are stable under
base change. Lean first identifies ind-étale maps with filtered
colimits of étale maps, applies the general stability of such a
property under pushout, and translates back to ring maps.
