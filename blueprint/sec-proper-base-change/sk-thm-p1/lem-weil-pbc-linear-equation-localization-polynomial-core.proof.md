+++
kind = "proof"
of = "lem-weil-pbc-linear-equation-localization-polynomial-core"
+++
Let $\varphi$ be the $A_{f_i}$-algebra homomorphism with $\varphi(Y_j)=x_j$ for $j\ne i$. For
the inverse, let $\psi_0\colon A[X_1,\dots,X_r]\to A_{f_i}[Y_j : j\ne i]$ be the $A$-algebra
homomorphism with $\psi_0(X_i)=f_i^{-1}\bigl(1-\sum_{j\ne i}f_jY_j\bigr)$ and
$\psi_0(X_j)=Y_j$ for $j\ne i$. It sends $\sum_jf_jX_j-1$ to $0$, so it factors through $B$,
and since $f_i$ maps to a unit it extends to $\psi\colon B_{f_i}\to A_{f_i}[Y_j : j\ne i]$.
By the universal property of localization, $\psi$ is $A_{f_i}$-linear. The two composites
$\psi\circ\varphi$ and $\varphi\circ\psi$ fix all generators (for $x_i$ use the relation
$f_ix_i=1-\sum_{j\ne i}f_jx_j$ in $B_{f_i}$). An algebra homomorphism out of a polynomial
ring, a quotient of it, or a localization of such a quotient is determined by its values on
the generators, so both composites are identities. Hence $\varphi$ is an isomorphism with
inverse $\psi$, and $\varphi^{-1}(x_j)=\psi(x_j)=Y_j$ for $j\ne i$.
