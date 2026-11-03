+++
kind = "proof"
of = "lem-pbc-q1-dense-irreducible-opens"
+++
*The opens.* Since $X$ is of finite type over a field and quasi-compact, it is Noetherian; let $C_1,\dots,C_n$ be its finitely many irreducible components. Let $O_a$ be the complement of the union of the components other than $C_a$; it is open and its closure is $C_a$. Put $U_a=V\cap O_a$. Density of $V$ makes $U_a$ nonempty; it is an open subset of the irreducible space $C_a$, hence irreducible, with closure $C_a$. The sets $U_a$ are pairwise disjoint, since a point of $U_a$ lies on no other component.

*Density and dimension.* Every point lies in some $C_a=\overline{U_a}$, so the union $W$ is dense. Let $w\in X\setminus W$ and let $z$ be the generic point of a component $C_a$ containing $w$. As $z$ specializes to every point of $U_a$ and $U_a$ is open, $z\in U_a\subseteq W$. So every point of $X\setminus W$ is a proper specialization of a point outside $X\setminus W$, and since $\dim X\le1$, every chain of specializations inside $X\setminus W$ has length zero: $\dim(X\setminus W)\le0$.

*Connected components.* For $x\in U_a$, the sets $U_a$ and $\bigcup_{b\ne a}U_b$ are disjoint opens covering $W$, so the connected component of $x$ in $W$ lies in $U_a$. Conversely $U_a$ is irreducible, hence connected, so it lies in that component. Thus the component is $U_a$, which is irreducible. If $X$ is empty there are no components and $n=0$.
