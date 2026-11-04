+++
kind = "proof"
of = "proposition-ind-constructible-sheaves"
order = 449
uses = ["definition-lisse-sheaves", "lemma-constructible-sheaves", "lemma-continuity-ext-out-constructible-complex", "definition-ind-constructible-sheaves"]
+++
The proof uses one property of constructible sheaves: maps out of them
commute with filtered colimits. Because of this, the formal colimits of
the ind-category behave like actual colimits. Each closure property in (2)
then reduces to the same property of $\Cons(X,\Lambda)$, once the objects
and maps involved are written as filtered colimits of constructible
sheaves and maps between them.

*Finite presentation.* Constructible sheaves are finitely
presented in $\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$. Indeed,
Lemma [lemma-continuity-ext-out-constructible-complex] in degree zero
shows that $\Hom(C,-)$ commutes with filtered colimits for $C$ constructible.
By Lemma [lemma-constructible-sheaves](1),(2), the
category $\Cons(X,\Lambda)$ is essentially small, abelian, and closed
under extensions. We fix a small skeleton. Part (1) follows from finite
presentation.

*Full faithfulness.* For filtered diagrams $(C_\alpha)$ and
$(D_\beta)$ of constructible sheaves, finite presentation implies

$$
\Hom(\varinjlim_\alpha C_\alpha,\varinjlim_\beta D_\beta)
=\varprojlim_\alpha\varinjlim_\beta\Hom_{\Cons(X,\Lambda)}(C_\alpha,D_\beta),
$$

which is the Hom set in the ind-category.

*Canonical presentations.* The closure properties below involve
several ind-constructible sheaves at once. To compare their
presentations we use a presentation that involves no choices. For $B\in\IndCons(X,\Lambda)$, let $J(B)$ be
the category of constructible sheaves $C$ with a map $C\to B$. We show that
$B=\varinjlim_{J(B)}C$.

The category $J(B)$ is filtered. Two objects $C_1\to B$ and $C_2\to B$
both map to $C_1\oplus C_2\to B$. Two parallel arrows $C\rightrightarrows C'$
over $B$ are equalized by the cokernel of their difference, which is
constructible and still maps to $B$. Now write
$B=\varinjlim_\alpha C_\alpha$. By finite presentation, every
$C\to B$ factors through some $C_\alpha$, and two factorizations agree at
a later stage. This means that the given diagram is cofinal in $J(B)$, and
hence $B=\varinjlim_{J(B)}C$.

*Filtered colimits and direct sums.* Let $B=\varinjlim_\lambda B_\lambda$
be a filtered colimit with $B_\lambda\in\IndCons(X,\Lambda)$. Consider the category
of pairs $(\lambda,C\to B_\lambda)$ with $C$ constructible. It is filtered:
we move finitely many indices to a common upper bound, and then use direct
sums and cokernels in $J(B_\lambda)$. The colimit of the $C$ over this
category is $\varinjlim_\lambda\varinjlim_{J(B_\lambda)}C=B$. A direct sum is the
filtered colimit of its finite subsums, so it lies in $\IndCons(X,\Lambda)$
as well.

*Kernels and cokernels.* Let $f:B\to B'$ be a map in
$\IndCons(X,\Lambda)$. It suffices to write $f$ as a filtered colimit of maps $v$ of
constructible sheaves. Since filtered colimits are exact, $\ker f$
and $\coker f$ are then the filtered colimits of the constructible sheaves
$\ker v$ and $\coker v$. Let $P_f$ be the category of commutative squares

$$
\begin{matrix} C&\xrightarrow{v}&D\\
\downarrow&&\downarrow\\ B&\xrightarrow{f}&B',\end{matrix}
\qquad C,D\in\Cons(X,\Lambda).
$$

This category is filtered, because finite colimits of such squares are
formed by finite colimits of the arrows $v$ in the abelian category
$\Cons(X,\Lambda)$. We claim that the functor $P_f\to J(B)$,
$(v)\mapsto(C\to B)$, is cofinal. Every $C\to B$ is the source of a
square, namely $v=\mathrm{id}_C$ with $C\to B'$ the composite. If
$C\to C_1\xrightarrow{v_1}D_1$ and $C\to C_2\xrightarrow{v_2}D_2$ are two
squares under the same $C\to B$, then both map to the square with source
$C_1\amalg_CC_2$ and target $D_1\amalg_CD_2$. The pushouts are taken in
$\Cons(X,\Lambda)$, and they map to $B$ and $B'$ because the two maps
from $C$ to $B$, and the two maps from $C$ to $B'$, agree.

Similarly, the functor $P_f\to J(B')$, $(v)\mapsto(D\to B')$, is cofinal.
Every $D\to B'$ is the target of a square, namely $v:0\to D$. If
$C_1\xrightarrow{v_1}D_1$ and $C_2\xrightarrow{v_2}D_2$ are two squares
under the same $D\to B'$, then both map to the square with source
$C_1\oplus C_2$ and target $D_1\amalg_DD_2$. The two cofinality statements give
$f=\varinjlim_{P_f}v$, and exactness of filtered colimits gives

$$
\ker f=\varinjlim_{P_f}\ker v,\qquad
\coker f=\varinjlim_{P_f}\coker v,
$$

both of which lie in $\IndCons(X,\Lambda)$.

*Extensions.* Let $0\to N\to M\to B\to0$ be exact in
$\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$, with $N=\varinjlim_\beta D_\beta$ and
$B=\varinjlim_\alpha C_\alpha$ ind-constructible. We show that $M$ is a
filtered colimit of extensions of constructible sheaves. First, the pullback
of the extension along $C_\alpha\to B$ is ind-constructible. Its class lies in
$\Ext^1(C_\alpha,N)$, and
Lemma [lemma-continuity-ext-out-constructible-complex] gives

$$
\Ext^1(C_\alpha,N)
=\varinjlim_\beta\Ext^1(C_\alpha,D_\beta).
$$

So the pulled-back extension is pushed out from an extension $M_{\alpha\beta}$
of $C_\alpha$ by some $D_\beta$. Since
$\Cons(X,\Lambda)$ is closed under extensions, $M_{\alpha\beta}$ and each of its
pushouts along $D_\beta\to D_{\beta'}$ are constructible. Their colimit over
$\beta'$ is the pullback of $M$ to $C_\alpha$. Second, since filtered
colimits are exact, $M$ is the colimit over $\alpha$ of these pullbacks.
By closure under filtered colimits, $M\in\IndCons(X,\Lambda)$.

*Grothendieck.* The category $\IndCons(X,\Lambda)$ is Grothendieck abelian
in the sense of [Stacks, [079A](https://stacks.math.columbia.edu/tag/079A)]. Indeed, by the above its colimits
exist and are computed in $\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$, so filtered
colimits are exact. The direct sum of the objects of the skeleton of
$\Cons(X,\Lambda)$ is a generator.
