+++
kind = "proof"
of = "lem-weil-pbc-directed-colimit-base-change-elementwise"
+++
Restrict to the upper tail $J=\{i\in I\mid i\ge0\}$; it is nonempty, directed and cofinal in $I$, so $A=\varinjlim_{i\in J}A_i$ with the same coprojections. For $i\in J$ regard $A_i$ as an $A_0$-module via $\alpha_{i0}$; then the transition maps $\alpha_{i'i}$ and the coprojections $\alpha_i$ are $A_0$-linear and satisfy the identities of a directed system and of a cocone.

The ring colimit is also the module colimit. The compatible $A_0$-linear maps $\alpha_i$ induce an $A_0$-linear map $g:\varinjlim_{i\in J}A_i\to A$ from the direct limit of $A_0$-modules. It is surjective: every element of the filtered colimit of rings $A$ is $\alpha_i(a)$ for some $i\in I$ and $a\in A_i$, and moving $a$ to a later stage we may take $i\ge0$. It is injective: if two stage elements have the same image in $A$, they become equal at some later stage, so they define the same element of the module direct limit. Hence $g$ is an isomorphism.

Tensor products commute with direct limits, so $(\varinjlim_{i\in J}A_i)\otimes_{A_0}M_0\cong\varinjlim_{i\in J}(A_i\otimes_{A_0}M_0)=\varinjlim_{i\in J}M_i$, the transition maps being $\mu_{i'i}=\alpha_{i'i}\otimes\mathrm{id}$ (these satisfy the identities of a directed system, as one checks on pure tensors). Composing the inverse of this isomorphism with $g\otimes\mathrm{id}_{M_0}$ gives an isomorphism $e:\varinjlim_{i\in J}M_i\xrightarrow{\sim}A\otimes_{A_0}M_0=M$. On pure tensors one checks that $e$ sends the class of $t\in M_i$ to $\mu_i(t)=(\alpha_i\otimes\mathrm{id})(t)$; by linearity this holds for all $t\in M_i$.

Now (1) follows because every element of a direct limit of modules is the class of an element of some stage: for $x\in M$, $e^{-1}(x)$ is the class of some $t\in M_i$, and then $x=\mu_i(t)$. For (2), if $\mu_i(t)=0$ then, $e$ being injective, the class of $t$ in the direct limit is zero, and an element of a stage with zero class in a directed limit of modules vanishes at some later stage: $\mu_{i'i}(t)=0$ for some $i'\ge i$.
