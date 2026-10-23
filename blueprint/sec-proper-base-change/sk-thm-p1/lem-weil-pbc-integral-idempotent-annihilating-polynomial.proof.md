+++
kind = "proof"
of = "lem-weil-pbc-integral-idempotent-annihilating-polynomial"
+++
*$z=b^2-b$ lies in $IB$.* The kernel of the quotient map $B\to B/IB$ is $IB$. The image $\bar b$ of $b$ is idempotent, so the image of $z=b^2-b$ is $\bar b^2-\bar b=0$, i.e. $z\in IB$.

Since $z\in IB$ is integral over $A$, it satisfies an integral equation whose non-leading coefficients lie in $I$: there is a monic $g\in A[x]$ with $g(z)=0$ and all non-leading coefficients of $g$ in $I$ (the standard lemma for elements of $IB$ in an integral extension). Reducing coefficientwise, $g\equiv x^{m}$ modulo $I$ with $m=\deg g$. Set $h=x\,g$ and $d=m+1$; then $d\ge1$, $h$ is monic, $h(z)=0$, and $h\equiv x^d$ modulo $I$. Multiplying by $x$ also handles the case $\deg g=0$ without a separate argument.

Suppose $A\neq0$. Put $q=x(x-1)$ and $f=h(q)=h\circ q$. Since $q$ is monic of positive degree and $h$ is monic, $f$ is monic. As $q(b)=b^2-b=z$, $f(b)=h(z)=0$. Reduction modulo $I$ commutes with composition, so $f\equiv q^d=x^d(x-1)^d$ modulo $I$. If $A$ is the zero ring, then $B$ is the zero ring too (it is an $A$-algebra); take $d=1$ and $f=1$, and all required equalities hold trivially.
