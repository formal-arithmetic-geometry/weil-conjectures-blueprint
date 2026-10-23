+++
kind = "proof"
of = "lem-weil-pbc-finite-purely-inseparable-scalar-descent"
uses = ["def-weil-finite-dimensional-subspace"]
+++
*Step 1.* Base change along a field extension preserves dimension: $\dim_KB=\dim_L(L\otimes_KB)$, which is finite and positive since $L\otimes_KB$ is a nonzero finite-dimensional $L$-vector space [def-weil-finite-dimensional-subspace]. Hence $B$ is a finite-dimensional $K$-algebra.

*Step 2.* Since $L$ is flat over the field $K$ and $K\to L$ is injective, $b\mapsto1\otimes b$ embeds $B$ into the field $L\otimes_KB$. So $B$ is a finite-dimensional $K$-algebra without zero divisors, hence a field.

*Step 3.* Choose a $K$-linear functional $\lambda:L\to K$ with $\lambda(1)=1$ ($L$ is a free $K$-module containing $1$ as a basis element of a suitable basis). Then $\pi=\lambda\otimes\mathrm{id}_B:L\otimes_KB\to B$ is $K$-linear with $\pi(l\otimes b)=\lambda(l)b$.

*Step 4.* Let $q$ be the exponential characteristic of $K$, which is also that of $L$. For $b\in B$, pure inseparability of $L\otimes_KB$ over $L$ gives $n$ and $l\in L$ with $(1\otimes b)^{q^n}=l\otimes1$, i.e. $1\otimes b^{q^n}=l\otimes1$. Applying $\pi$ gives $b^{q^n}=\lambda(l)\in K$. Hence $B$ is purely inseparable over $K$ (this covers characteristic zero, where $q=1$). Together with steps 1 and 2 this proves the claims.
