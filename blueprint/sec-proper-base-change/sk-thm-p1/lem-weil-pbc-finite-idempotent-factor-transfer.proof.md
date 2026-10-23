+++
kind = "proof"
of = "lem-weil-pbc-finite-idempotent-factor-transfer"
+++
Since $\alpha$ is a unit, $bd=\alpha d$ gives $d=b(\alpha^{-1}d)$, so $b$ divides $d$ in $D$; hence the bijection $D[1/b]\to B[1/b]$ induces a bijection $D[1/d]\to B[1/e]$. As $d$ is idempotent, $D\to D[1/d]$ is surjective (it is the projection onto the factor $dD$). Therefore $F:D\to B[1/e]$ is surjective, and integrality of the finite $A$-algebra $D$ passes to its quotient $B[1/e]$.

Let $\sigma:D\to A/I$ be the first coordinate of $\Phi$ composed with $D\to D/ID$. It is an $A$-algebra map with $\sigma(d)=1$, so it extends over $D[1/d]$ and, through the bijection above, gives an $A$-algebra map $\rho:B[1/e]\to A/I$. It kills $IB[1/e]$, so it induces a left inverse of $A/I\to B[1/e]/IB[1/e]$, proving injectivity.

For surjectivity, write an element of $B[1/e]/IB[1/e]$ as the class of $F(x)$ with $x\in D$. Lift the first coordinate of $\Phi(x\bmod ID)$ to $a\in A$. Then $\Phi(d(x-a)\bmod ID)=(1,0)\cdot(\Phi(x\bmod ID)-\Phi(a\bmod ID))=0$, so $d(x-a)\in ID$. Applying $F$, with $F(d)=1$, gives $F(x)-a\in IB[1/e]$, so the class of $F(x)$ is the image of $a\bmod I$.
