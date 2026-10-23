+++
kind = "proof"
of = "lem-weil-pbc-etale-section-lifting-radical-and-henselian"
+++
*Jacobson radical.* Let $x\in I$ and $y\in A$, and put $f=1+xy$. Its image in $A/I$ is $1$, a unit, so the quotient map $A\to A/I$ extends to an $A$-algebra homomorphism $\sigma:A_f\to A/I$. The localization $A_f$ is an étale $A$-algebra ($\operatorname{Spec}A_f\to\operatorname{Spec}A$ is an open immersion). Lift $\sigma$ to an $A$-algebra homomorphism $\tau:A_f\to A$. Since $f$ is a unit of $A_f$, $\tau(f)=f$ is a unit of $A$. As $1+xy$ is a unit for every $y\in A$, $x$ lies in the Jacobson radical.

*Henselian.* Let $f\in A[T]$ be monic and $a_0\in A$ with $f(a_0)\in I$ and $f'(a_0)$ invertible modulo $I$. The pair $(f,f')$ is a standard étale pair ($f'\cdot1+f\cdot0=f'^1$), so $P=A[T][Y]/(f,Yf'-1)$ is an étale $A$-algebra. The image $\bar a_0$ of $a_0$ in $A/I$ satisfies $f(\bar a_0)=0$ with $f'(\bar a_0)$ invertible, so there is an $A$-algebra homomorphism $\sigma:P\to A/I$ with $\sigma(T)=\bar a_0$. Lift it to $\tau:P\to A$ and put $a=\tau(T)$. Then $f(a)=\tau(f(T))=0$, and $a\equiv a_0\pmod I$ because $\tau$ followed by $A\to A/I$ is $\sigma$. Together with the first part this proves that $(A,I)$ is henselian. (If the hypothesis is only available for étale algebras of a larger size, apply it to a copy of $A_f$, resp. $P$, of that size and transport back along the isomorphism.)
