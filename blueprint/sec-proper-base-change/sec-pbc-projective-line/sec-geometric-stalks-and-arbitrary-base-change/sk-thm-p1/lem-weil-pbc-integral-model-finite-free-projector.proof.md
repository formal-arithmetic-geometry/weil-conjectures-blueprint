+++
kind = "proof"
of = "lem-weil-pbc-integral-model-finite-free-projector"
+++
Lift the entries of the matrix $M$ of $\bar p$ to a matrix $X\in\operatorname{Mat}_n(A)$, using surjectivity of $A\to A/I$. Set $f=\chi_X$, the characteristic polynomial of $X$, and $B=A[x]/(f)$. Since $f$ is monic of degree $n$, $B$ is a finite free $A$-module, hence integral over $A$. By Cayley–Hamilton $f(X)=0$, so the evaluation $A[x]\to\operatorname{Mat}_n(A)$, $x\mapsto X$, factors through an $A$-algebra map $\psi:B\to\operatorname{Mat}_n(A)$ with $\psi(x)=X$.

In matrices over $(A/I)[t]$, write $S=t\cdot1$ and $N$ for $M$ viewed as a constant matrix. Since $N^2=N$ and $SN=NS$, expansion gives $(S-N)(1-S-N)=(t-t^2)\cdot1$. Taking determinants, $\chi_M\cdot\det(1-S-N)=(t-t^2)^n$, so $\chi_M$ divides $(t-t^2)^n$. This holds over every commutative ring, including the zero ring.

The quotient map $A/I\to B/IB$ is well defined. The characteristic polynomial commutes with base change, so $f\bmod I=\chi_M$. Evaluation at the class $\bar x$ of $x$ in $B/IB$ sends $f\bmod I$ to zero because $f(x)=0$ in $B$. The divisibility of the preceding step therefore gives $(\bar x-\bar x^2)^{n+1}=0$; using the exponent $n+1$ instead of $n$ avoids a separate case for $n=0$.

Put $y=1-(1-x^{n+1})^{n+1}$ in $B$. Since $\bar x-\bar x^2$ is nilpotent with $(\bar x-\bar x^2)^{n+1}=0$, the class of $y$ is idempotent. This formula follows by the geometric-sum identity: (z-z²)^N divides e-e² for e=1-(1-z^N)^N. Under the composite B → Mat_n(A) → Mat_n(A/I), x goes to M. Since M and 1-M equal every positive power of themselves, y goes to 1-(1-M)=M. This proves all the claims; no residue field or prime-spectrum lemmas occur.
