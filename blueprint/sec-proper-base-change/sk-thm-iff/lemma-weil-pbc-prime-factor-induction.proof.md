+++
kind  = "proof"
of    = "lemma-weil-pbc-prime-factor-induction"
+++
Induct on $\nu(n)=\sum_\ell v_\ell(n)$, the number of prime factors of $n$. If
$n=1$ then $F=0$ is killed by any prime. Otherwise choose a prime $\ell\mid n$
and use the short exact sequence
$0\to F[\ell]\to F\xrightarrow{\ell}\ell F\to0$.
The kernel is killed by $\ell$, while $\ell F$ is killed by $n/\ell$ and
therefore has fewer prime factors in its exponent. Let
$C(E)=\operatorname{Cone}(\operatorname{Ex}_{\square,E})$, so that
$\Ex^q_{\square,E}$ is an isomorphism for every $q$ exactly when $C(E)$ is
acyclic, and use the cohomological cone convention
$d_{C}(y,x)=(d_Yy+u(x),-d_Xx)$. Applying the two derived functors to the
short exact sequence gives a morphism of distinguished triangles given by the
exchange maps and, by the octahedral axiom, a triangle

$$
C(F[\ell])\longrightarrow C(F)\longrightarrow
C(\ell F)\xrightarrow{+1}C(F[\ell])[1].
$$

The connecting map is the class of $(y,x)\mapsto y$ in the above cone
convention; the sign in the last arrow is forced by $d_C^2=0$. The cone
$C(F[\ell])$ is acyclic by hypothesis and $C(\ell F)$ by induction, so the long
exact cohomology sequence of this triangle makes $C(F)$ acyclic. The base
$\nu(n)=1$ is the prime-torsion hypothesis.
