+++
kind = "proof"
of = "lem-weil-pbc-cyclic-module-constant-reflection"
+++
*Forgetting is fully faithful.* Every additive map between $\mathbf Z/n$-modules is $\mathbf Z/n$-linear: a residue $r$ is the image of an integer $a$, and $f(ax)=af(x)$. So the functor $V$ forgetting the module structure is fully faithful on modules, and hence so is the induced functor on sheaves.

*A $\mathbf Z/n$-module value.* Let $E$ be an abelian group with $V(F)\cong\underline E$, and put $Q=E/nE=\operatorname{coker}(n\cdot\mathrm{id}_E)$; it is killed by $n$, hence a $\mathbf Z/n$-module. No finiteness and no point of the site is used.

*$\underline E\cong\underline Q$.* The constant abelian sheaf functor $L$ is a left adjoint (of global sections), so it preserves cokernels: $L(Q)=\operatorname{coker}(L(n\cdot\mathrm{id}_E))$. Every section of $V(F)$ is killed by $n$, because $n=0$ in $\mathbf Z/n$; transporting through $L(E)\cong V(F)$ gives $L(n\cdot\mathrm{id}_E)=0$, so the projection $L(E)\to L(Q)$ is an isomorphism.

*Conclusion.* Constant sheaves commute with forgetting the module structure, so $L(Q)$ is the underlying abelian sheaf of the constant sheaf of $\mathbf Z/n$-modules with value $Q$. Composing $V(F)\cong L(E)\cong L(Q)$ gives an isomorphism of underlying abelian sheaves, which lifts, by full faithfulness, to an isomorphism of sheaves of $\mathbf Z/n$-modules between $F$ and the constant sheaf with value $Q$. Hence $F$ is constant.
