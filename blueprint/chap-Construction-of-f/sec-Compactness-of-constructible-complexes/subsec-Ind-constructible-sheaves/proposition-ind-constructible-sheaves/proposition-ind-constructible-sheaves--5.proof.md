+++
kind = "proof"
of = "proposition-ind-constructible-sheaves--5"
order = 453011
+++
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

*Source:* the proof of Proposition [proposition-ind-constructible-sheaves].
