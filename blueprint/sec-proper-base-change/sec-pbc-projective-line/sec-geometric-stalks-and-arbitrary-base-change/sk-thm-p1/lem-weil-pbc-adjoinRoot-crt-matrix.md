+++
id = "lem-weil-pbc-adjoinRoot-crt-matrix"
kind = "lemma"
title = "Simultaneous CRT coordinates for reduced root and idempotent-lift multiplication matrices"
lean = ["Polynomial.adjoinRoot_crt_matrix"]
order = 1783
+++
Let $A$ be a commutative ring, $I$ an ideal with $R=A/I\neq0$, $f\in A[X]$ monic, and $g,h\in R[X]$ monic and coprime with $\bar f=gh$, where $\bar f$ is the reduction of $f$ modulo $I$. Let $e\in A[X]/(f)$ have images $1$ in $R[X]/(g)$ and $0$ in $R[X]/(h)$ under the canonical coefficient-reduction quotient maps. Let $T,P$ be the matrices of multiplication by the class of $X$ and by $e$ on $A[X]/(f)$ in its power basis $1,X,\dots,X^{\deg f-1}$, and $T_g,T_h$ the matrices of multiplication by the class of $X$ on $R[X]/(g)$ and $R[X]/(h)$ in their power bases. There exist a bijection $d:\{0,\dots,\deg f-1\}\cong\{0,\dots,\deg g-1\}\sqcup\{0,\dots,\deg h-1\}$ and an invertible matrix $U$ over $R$ indexed by this disjoint union such that, writing $d_*$ for reindexing rows and columns along $d$ and $\bar T,\bar P$ for the reductions modulo $I$,
$$U\,d_*(\bar T)\,U^{-1}=\begin{pmatrix}T_g&0\\0&T_h\end{pmatrix},\qquad U\,d_*(\bar P)\,U^{-1}=\begin{pmatrix}1&0\\0&0\end{pmatrix}.$$
