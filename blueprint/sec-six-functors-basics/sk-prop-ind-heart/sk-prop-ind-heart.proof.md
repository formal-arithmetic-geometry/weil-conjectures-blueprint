+++
kind = "proof"
of = "sk-prop-ind-heart"
uses = ["sk-lem-constructible-ext-continuity", "sk-lem-coefficient-heart"]
+++
Constructible sheaves are finitely presented in $\Mod(X_{\mathrm{proét}},\Lambda)$: by
[sk-lem-constructible-ext-continuity] in degree zero, $\Hom(C,-)$ commutes with filtered colimits for
$C$ constructible. The category $\Cons(X,\Lambda)$ is essentially small and abelian, and it is closed
under extensions (parts (1), (2) of [sk-lem-coefficient-heart]). We fix a small skeleton. Part (1)
follows from finite presentation. For part (2), we reduce each closure property to the same property of
$\Cons(X,\Lambda)$ by writing the objects and maps involved as filtered colimits of constructible sheaves
and maps between them.

*Full faithfulness.* For filtered diagrams $(C_\alpha)$ and $(D_\beta)$ of constructible sheaves, finite
presentation implies

$$
\Hom(\varinjlim_\alpha C_\alpha,\varinjlim_\beta D_\beta)
=\varprojlim_\alpha\varinjlim_\beta\Hom_{\Cons(X,\Lambda)}(C_\alpha,D_\beta),
$$

which is the Hom set in the ind-category ([det-ind-heart-full-faithfulness]).

*Canonical presentations.* For $B\in\IndCons(X,\Lambda)$, let $J(B)$ be the category of constructible
sheaves $C$ with a map $C\to B$. This category is filtered, since two objects map to their direct sum,
and two parallel arrows are equalized by a cokernel in $\Cons(X,\Lambda)$. If
$B=\varinjlim_\alpha C_\alpha$, then by finite presentation every $C\to B$ factors through some
$C_\alpha$, and two factorizations agree at a later stage. Hence the given diagram is cofinal in $J(B)$
and $B=\varinjlim_{J(B)}C$ ([det-ind-heart-canonical-presentation]).

*Filtered colimits and direct sums.* Let $B=\varinjlim_\lambda B_\lambda$ be a filtered colimit with
$B_\lambda\in\IndCons(X,\Lambda)$. The category of pairs $(\lambda,C\to B_\lambda)$, $C$ constructible,
is filtered (move finitely many indices to a common upper bound, then use direct sums and cokernels in
$J(B_\lambda)$), and the colimit of the $C$ over it is $\varinjlim_\lambda\varinjlim_{J(B_\lambda)}C=B$.
A direct sum is the filtered colimit of its finite subsums, so it lies in $\IndCons(X,\Lambda)$ as well
([det-ind-heart-filtered-colimits]).

*Kernels and cokernels.* Let $f\colon B\to B'$ be a map in $\IndCons(X,\Lambda)$. We write $f$ as a
filtered colimit of maps of constructible sheaves. Let $P_f$ be the category of commutative squares

$$
\begin{matrix} C&\xrightarrow{v}&D\\ \downarrow&&\downarrow\\ B&\xrightarrow{f}&B',\end{matrix}
\qquad C,D\in\Cons(X,\Lambda).
$$

This category is filtered, because finite colimits of such squares are formed by finite colimits of the
arrows $v$ in the abelian category $\Cons(X,\Lambda)$. We claim that the functor $P_f\to J(B)$,
$(v)\mapsto(C\to B)$, is cofinal. Every $C\to B$ is the source of a square, namely $v=\mathrm{id}_C$
with $C\to B'$ the composite. If $C\to C_1\xrightarrow{v_1}D_1$ and $C\to C_2\xrightarrow{v_2}D_2$ are
two squares under the same $C\to B$, then both map to the square with source $C_1\amalg_CC_2$ and
target $D_1\amalg_CD_2$. The pushouts are taken in $\Cons(X,\Lambda)$, and they map to $B$ and $B'$
because the two maps from $C$ to $B$, and the two maps from $C$ to $B'$, agree.

Similarly, the functor $P_f\to J(B')$, $(v)\mapsto(D\to B')$, is cofinal. Every $D\to B'$ is the target
of a square, namely $v\colon0\to D$. If $C_1\xrightarrow{v_1}D_1$ and $C_2\xrightarrow{v_2}D_2$ are two
squares under the same $D\to B'$, then both map to the square with source $C_1\oplus C_2$ and target
$D_1\amalg_DD_2$. Hence $f=\varinjlim_{P_f}v$, and since filtered colimits are exact,

$$
\ker f=\varinjlim_{P_f}\ker v,\qquad \coker f=\varinjlim_{P_f}\coker v,
$$

both of which lie in $\IndCons(X,\Lambda)$ ([det-ind-heart-kernels-cokernels]).

*Extensions.* Let $0\to N\to M\to B\to0$ be exact in $\Mod(X_{\mathrm{proét}},\Lambda)$, with
$N=\varinjlim_\beta D_\beta$ and $B=\varinjlim_\alpha C_\alpha$ ind-constructible. Pull the extension
back along $C_\alpha\to B$. By [sk-lem-constructible-ext-continuity], we have

$$
\Ext^1(C_\alpha,N)=\varinjlim_\beta\Ext^1(C_\alpha,D_\beta),
$$

and hence the pulled-back extension is pushed out from an extension $M_{\alpha\beta}$ of $C_\alpha$ by
some $D_\beta$. Each $M_{\alpha\beta}$, and each of its pushouts along $D_\beta\to D_{\beta'}$, is
constructible because $\Cons(X,\Lambda)$ is closed under extensions. Their colimit over $\beta'$ is the
pullback of $M$ to $C_\alpha$, which is therefore ind-constructible. Since filtered colimits are exact,
$M$ is the colimit over $\alpha$ of these pullbacks, and hence $M\in\IndCons(X,\Lambda)$ by closure under
filtered colimits ([det-ind-heart-extensions]).

*Grothendieck.* By the above, colimits in $\IndCons(X,\Lambda)$ exist and are computed in
$\Mod(X_{\mathrm{proét}},\Lambda)$, and hence filtered colimits are exact. Moreover, the direct sum of the
objects of the skeleton of $\Cons(X,\Lambda)$ is a generator. By definition
([Stacks, Tag 079A](https://stacks.math.columbia.edu/tag/079A)), this means that $\IndCons(X,\Lambda)$ is
a Grothendieck abelian category ([det-ind-heart-grothendieck]).
