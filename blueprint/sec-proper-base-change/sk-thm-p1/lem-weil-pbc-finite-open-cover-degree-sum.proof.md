+++
kind = "proof"
of = "lem-weil-pbc-finite-open-cover-degree-sum"
uses = ["def-pc-scheme"]
+++
*Step 1.* Put $B_i=\Gamma(W_i,\mathcal O_{W_i})$, a $k$-algebra via $t|_{W_i}$. Since $W_i$ is finite over $k$, it is affine and $B_i$ is a finite $k$-module; a finite algebra over a field has a finite discrete spectrum, so $W_i$ is a finite discrete space.

*Step 2.* As $T=\bigcup_iW_i$, the space $T$ is finite. Each point $x\in T$ lies in some $W_i$, where $\{x\}$ is open; since $W_i$ is open in $T$, $\{x\}$ is open in $T$. Hence $T$ is a finite discrete space (empty if $m=0$) [def-pc-scheme].

*Step 3 ($T$ is affine).* A scheme whose underlying space is finite and discrete is a finite disjoint union of local schemes $\operatorname{Spec}\mathcal O_{T,x}$, hence affine: with $A=\Gamma(T,\mathcal O_T)$ the canonical morphism $T\to\operatorname{Spec}A$ is an isomorphism. Make $A$ a $k$-algebra via $t$.

*Step 4.* The restriction maps $A\to B_i$ are $k$-algebra homomorphisms, and the $k$-linear map $A\to\prod_iB_i$ is injective because the $W_i$ cover $T$ and $\mathcal O_T$ is a sheaf. Since $\prod_iB_i$ is a finite $k$-module, so is $A$, and $\dim_kA\le\sum_i\dim_kB_i\le\sum_in_i$. The empty cover gives $A=0$.

*Step 5.* A morphism to an affine scheme from an affine scheme is finite if and only if the ring map on global sections is finite. By steps 3 and 4, $t$ is finite, with the stated dimension bound.
