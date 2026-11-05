+++
kind = "proof"
of = "lem-weil-pbc-killed-sheaf-module-lift"
uses = ["def-weil-pbc-etale-sheaves"]
+++
Evaluating $n\operatorname{id}_G=0$ at every object $U$ shows that $n$ kills every section group $G(U)$. An abelian group killed by $n$ is uniquely a $\mathbf Z/n\mathbf Z$-module, with $(k\bmod n)\cdot a=ka$. Every additive map between such groups is $\mathbf Z/n\mathbf Z$-linear, so the restriction maps of $G$ are linear, and the functor laws follow from those of $G$. This defines a presheaf $M$ of $\mathbf Z/n\mathbf Z$-modules; the argument is valid also for $n=0$, $n=1$ and for the zero sheaf.

The underlying abelian presheaf of $M$ is $G$ itself. The forgetful functor from $\mathbf Z/n\mathbf Z$-modules to abelian groups preserves and reflects limits, so $M$ satisfies the sheaf condition because $G$ does. The identity gives the claimed isomorphism of underlying abelian sheaves. ([def-weil-pbc-etale-sheaves]).
