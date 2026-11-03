+++
kind  = "proof"
of    = "lem-trf-simple-constructible"
+++
Let $F$ be simple, and let $\eta$ be the generic point of an irreducible
component $V$ of the closure of the support of $F$. Choose an open
$U\subset V$ containing $\eta$, disjoint from the other components, on
which $F|_U$ is locally constant and nonzero, and an open $W\subset X$ with
$W\cap\overline{\operatorname{supp}F}=U$. Extension by zero gives a nonzero
subsheaf $j_{W!}(F|_W)\subset F$, so it equals $F$ and
$\operatorname{supp}F\subset U$. If $U\neq\{\eta\}$, pick a point
$y\in U$ closed in $U$, $y\neq\eta$, and put
$W'=W\setminus\overline{\{y\}}$; then $j_{W'!}(F|_{W'})$ is a nonzero
subsheaf of $F$ (it is nonzero at $\eta$) with zero stalk at $y$, where $F$
is nonzero, contradicting simplicity. Hence $U=\{\eta\}$, so $\{\eta\}$ is
locally closed and $F=i_{\eta!}M$ with $M=i_\eta^*F$. Subsheaves of
$i_{\eta!}M$ are supported in $\{\eta\}$, hence of the form $i_{\eta!}N$ for
a Galois-stable submodule $N\subset M$, so $M$ is simple. Conversely each
such $i_{x!}M$ is simple by the same correspondence. On a scheme of finite
type over a field a locally closed point is closed (Jacobson property). For
the last assertion: a finite extension of punctual sheaves has finite
support, while a nonzero lisse sheaf on a positive-dimensional scheme does
not.
