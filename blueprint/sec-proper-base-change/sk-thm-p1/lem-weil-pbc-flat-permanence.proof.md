+++
kind = "proof"
of = "lem-weil-pbc-flat-permanence"
+++
Let $u:N_1\to N_2$ be an injective $R$-linear map. By the definition of a flat ring map it suffices to show that $u\otimes1_S:N_1\otimes_RS\to N_2\otimes_RS$ is injective; by the symmetry isomorphisms $N_i\otimes_RS\cong S\otimes_RN_i$, $n\otimes s\mapsto s\otimes n$, which commute with $u\otimes1_S$ and $1_S\otimes u$, it is equivalent to show that $1_S\otimes u:S\otimes_RN_1\to S\otimes_RN_2$ is injective. (Stacks argues with an exact sequence $N_1\to N_2\to N_3$; with the definition of flatness used here, by injective maps, the case $0\to N_1\to N_2$ is the one needed.)

$M$ is a flat $R$-module (via $R\to S$), so $u\otimes1_M:N_1\otimes_RM\to N_2\otimes_RM$ is injective, hence, composing with the symmetry isomorphisms $N_i\otimes_RM\cong M\otimes_RN_i$, so is $1_M\otimes_Ru:M\otimes_RN_1\to M\otimes_RN_2$.

By the natural isomorphisms $c_{N_i}:M\otimes_S(S\otimes_RN_i)\xrightarrow{\sim}M\otimes_RN_i$ (cancellation of the base change), $(1_M\otimes_Ru)\circ c_{N_1}=c_{N_2}\circ(1_M\otimes_S(1_S\otimes u))$, so $1_M\otimes_S(1_S\otimes u)=c_{N_2}^{-1}\circ(1_M\otimes_Ru)\circ c_{N_1}$ is injective by step 2.

Consider the complex of $S$-modules $0\to S\otimes_RN_1\xrightarrow{1_S\otimes u}S\otimes_RN_2$ (composite zero). Applying $M\otimes_S-$ gives $0=M\otimes_S0\to M\otimes_S(S\otimes_RN_1)\to M\otimes_S(S\otimes_RN_2)$, which is exact by step 3. As $M$ is a faithfully flat $S$-module, the definition (a complex is exact if and only if its tensor product with $M$ is) shows that $0\to S\otimes_RN_1\to S\otimes_RN_2$ is exact, i.e. $1_S\otimes u$ is injective. By step 1, $R\to S$ is flat.
