+++
kind = "proof"
of = "sk-prop-ind-heart"
uses = ["sk-lem-coefficient-heart", "sk-lem-constructible-ext-continuity"]
+++
The key point is that constructible sheaves are finitely presented in $\Mod(X_{\mathrm{proét}},\Lambda)$: by
[sk-lem-constructible-ext-continuity] in degree zero, $\Hom(C,-)$ commutes with filtered colimits for
$C$ constructible. The category $\Cons(X,\Lambda)$ is essentially small and abelian, and closed under
extensions (parts (1), (2) of [sk-lem-coefficient-heart]); fix a small skeleton.

*Full faithfulness.* For filtered diagrams $(C_\alpha)$ and $(D_\beta)$ of constructible sheaves, finite
presentation gives

$$
\Hom_{\Lambda}(\varinjlim_\alpha C_\alpha,\varinjlim_\beta D_\beta)
=\varprojlim_\alpha\varinjlim_\beta\Hom_{\Cons(X,\Lambda)}(C_\alpha,D_\beta),
$$

which is the definition of morphisms in the ind-category ([det-ind-heart-full-faithfulness]).

*Canonical presentations.* For $B\in\IndCons(X,\Lambda)$ let $J(B)$ be the category of constructible
sheaves $C$ with a map $C\to B$. It is filtered: two objects map to their direct sum, and two parallel
arrows are equalized by a cokernel in $\Cons(X,\Lambda)$. If $B=\varinjlim_\alpha C_\alpha$, finite
presentation says that every $C\to B$ factors through some $C_\alpha$, and two factorizations agree at a
later stage; so the given diagram is cofinal in $J(B)$ and $B=\varinjlim_{J(B)}C$
([det-ind-heart-canonical-presentation]).

*Filtered colimits and direct sums.* Let $B=\varinjlim_\lambda B_\lambda$ be a filtered colimit with
$B_\lambda\in\IndCons(X,\Lambda)$. The category of pairs $(\lambda,C\to B_\lambda)$, $C$ constructible,
is filtered (move finitely many indices to a common upper bound, then use direct sums and cokernels in
$J(B_\lambda)$), and the colimit of the $C$ over it is $\varinjlim_\lambda\varinjlim_{J(B_\lambda)}C=B$.
A direct sum is the filtered colimit of its finite subsums, so it lies in $\IndCons(X,\Lambda)$ too
([det-ind-heart-filtered-colimits]).

*Kernels and cokernels.* Let $f\colon B\to B'$ be a map in $\IndCons(X,\Lambda)$. We write $f$ as a
filtered colimit of maps of constructible sheaves. Let $P_f$ be the category of commutative squares

$$
\begin{matrix} C&\xrightarrow{v}&D\\ \downarrow&&\downarrow\\ B&\xrightarrow{f}&B',\end{matrix}
\qquad C,D\in\Cons(X,\Lambda).
$$

It is filtered, because finite colimits of such squares are formed by finite colimits of the arrows $v$
in the abelian category $\Cons(X,\Lambda)$. The functor $P_f\to J(B)$, $(v)\mapsto(C\to B)$, is cofinal:
given $C\to B$, the composite $C\to B'$ factors through some $D\in J(B')$ by finite presentation; two
such choices are dominated by their direct sum; and a compatibility along a map $C_0\to C$ that holds
over $B'$ holds at a finite stage, after passing to a cokernel. (Equivalently, two choices over $C_0$
are dominated by the square with source $C_1\amalg_{C_0}C_2$ and target the quotient of $D_1\oplus D_2$
by the two images of $C_0$; parallel choices are dominated by their cokernel.) The same operations,
starting from the square $0\to D$, show that $P_f\to J(B')$, $(v)\mapsto(D\to B')$, is cofinal. Hence
$f=\varinjlim_{P_f}v$, and since filtered colimits are exact,

$$
\ker f=\varinjlim_{P_f}\ker v,\qquad \coker f=\varinjlim_{P_f}\coker v,
$$

both of which lie in $\IndCons(X,\Lambda)$ ([det-ind-heart-kernels-cokernels]).

*Extensions.* Let $0\to N\to M\to B\to0$ be exact in $\Mod(X_{\mathrm{proét}},\Lambda)$, with
$N=\varinjlim_\beta D_\beta$ and $B=\varinjlim_\alpha C_\alpha$ ind-constructible. Pull the extension
back along $C_\alpha\to B$. By [sk-lem-constructible-ext-continuity],

$$
\Ext^1_{\Lambda}(C_\alpha,N)=\varinjlim_\beta\Ext^1_{\Lambda}(C_\alpha,D_\beta),
$$

so the pulled-back extension is pushed out from an extension $M_{\alpha\beta}$ of $C_\alpha$ by some
$D_\beta$. Each $M_{\alpha\beta}$, and each of its pushouts along $D_\beta\to D_{\beta'}$, is
constructible because $\Cons(X,\Lambda)$ is closed under extensions; their colimit over $\beta'$ is the
pullback of $M$ to $C_\alpha$, which is therefore ind-constructible. Since filtered colimits are exact,
$M$ is the colimit over $\alpha$ of these pullbacks, so $M\in\IndCons(X,\Lambda)$ by the closure under
filtered colimits ([det-ind-heart-extensions]).

*Grothendieck.* By the above, colimits in $\IndCons(X,\Lambda)$ exist and are computed in
$\Mod(X_{\mathrm{proét}},\Lambda)$, so filtered colimits are exact; and the direct sum of the objects of the
skeleton of $\Cons(X,\Lambda)$ is a generator. This is the definition (Stacks, Tag 079A)
([det-ind-heart-grothendieck]).
