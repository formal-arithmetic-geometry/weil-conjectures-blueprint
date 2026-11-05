+++
kind = "proof"
of = "lemma-change-coefficients-direct-image--2"
order = 635005
uses = ["lemma-inverse-image-coefficient-sheaves"]
+++
Choose a uniformizer $\varpi$ of $\mathcal O_E$ and an integer $n$ with $K\in D^{\geq n}$. The inclusion $\mathcal O_{E,X}\to E_X$ is a monomorphism into a flat module on which $\varpi$ acts invertibly. The identification of this module with the pullback of $E_Y$ uses [lemma-inverse-image-coefficient-sheaves]. These facts give a representative $J$ of $K$, vanishing below $n-1$, whose terms are $f_*$-acyclic and on which $\varpi$ acts injectively.

The same injectivity holds on $f_*J$. The two-term resolution of $\mathbf F_E$ by multiplication by $\varpi$ therefore computes derived reduction of both $J$ and $f_*J$ term by term. The short exact sequences
$$
0\longrightarrow J^i\xrightarrow{\varpi}J^i\longrightarrow J^i/\varpi J^i\longrightarrow0
$$
show that $J^i/\varpi J^i$ is $f_*$-acyclic and that the underived comparison is an isomorphism on $J^i$. The factorization of the derived comparison through these termwise comparisons and the derived-functor units and counits now proves the assertion.
