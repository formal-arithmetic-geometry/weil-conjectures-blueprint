+++
kind  = "proof"
of    = "sk-lem-walg-trace-criterion"
+++
Put $\mathfrak d=[\mathfrak a,\mathfrak a]$. We show that every
$X\in\mathfrak d$ is nilpotent. Let $X=S+N$ be its Jordan decomposition,
with $S$ diagonalizable, $N$ nilpotent and $[S,N]=0$. Then the Jordan
decomposition of $\operatorname{ad}X$ on $\operatorname{End}(M)$ is
$\operatorname{ad}S+\operatorname{ad}N$, and Hermite interpolation on the
finitely many generalized eigenspaces of $\operatorname{ad}X$ gives a
polynomial $P$ with $P(0)=0$ such that

$$
\operatorname{ad}S=P(\operatorname{ad}X).
$$

Namely, for each eigenvalue $\delta$ of $\operatorname{ad}X$ we require
$P(t)\equiv\delta$ modulo the power of $(t-\delta)$ given by the size of
the largest Jordan block of $\operatorname{ad}X$ for $\delta$. Since $0$ is
an eigenvalue, this includes the condition $P(t)\equiv0$ at $\delta=0$. As
$\operatorname{ad}X$ maps $\mathfrak a$ into $\mathfrak d$, we conclude
that $[S,\mathfrak a]\subseteq\mathfrak d$.

Let $\lambda_1,\ldots,\lambda_e$ be the eigenvalues of $S$, with
multiplicity, and let $E\subseteq L$ be their $\mathbf Q$-span. For a
$\mathbf Q$-linear map $f\colon E\to L$, let $Z_f$ be the endomorphism of
$M$ that acts by $f(\lambda)$ on the $\lambda$-eigenspace of $S$. Choose a
polynomial $R_f$ that interpolates $f$ on the finite set of differences of
eigenvalues, that is,

$$
R_f(\lambda_i-\lambda_j)=f(\lambda_i-\lambda_j),
\qquad R_f(0)=0.
$$

Since $\operatorname{ad}S$ and $\operatorname{ad}Z_f$ act on the matrix
block for the pair $(\lambda_i,\lambda_j)$ by $\lambda_i-\lambda_j$ and
$f(\lambda_i-\lambda_j)$, this says that
$\operatorname{ad}Z_f=R_f(\operatorname{ad}S)$. Hence
$[Z_f,\mathfrak a]\subseteq\mathfrak d$. Writing $X=\sum_j[A_j,B_j]$ with
$A_j,B_j\in\mathfrak a$ and using the cyclicity of the trace and the
hypothesis, we find

$$
\operatorname{tr}(XZ_f)=\sum_j\operatorname{tr}([Z_f,A_j]B_j)=0.
$$

Since $N$ preserves the eigenspaces of $S$ and is nilpotent on each of
them, we have $\operatorname{tr}(NZ_f)=0$, and consequently

$$
\sum_{i=1}^e\lambda_i f(\lambda_i)=0.
$$

Choose a $\mathbf Q$-basis $e_1,\ldots,e_b$ of $E$, write
$\lambda_i=\sum_j a_{ij}e_j$, and take the coordinate functional
$f_j(e_k)=\delta_{jk}$. For $f=f_j$, the coefficient of $e_j$ in the last
identity is $\sum_i a_{ij}^2$, which therefore vanishes. Since a sum of
squares of rational numbers vanishes only when every summand is zero, all
$a_{ij}$ vanish. Hence all eigenvalues of $S$ vanish, and $X$ is
nilpotent. By Engel's theorem [sk-lem-walg-engel], the Lie algebra
$\mathfrak d$ is solvable. As $\mathfrak a/\mathfrak d$ is abelian, it
follows that $\mathfrak a$ is solvable.
