+++
kind  = "proof"
of    = "sk-lem-wrp-l2-growth"
+++
The assertion on the radius is the Cauchy–Hadamard formula
([lem-wf-l2-radius]). For the equivalent description of $\nu$, put
$c=\limsup_n n^{-1}\log_q S_n$. For every $u>c$ we have
$S_n\le q^{nu}$ for all large $n$, and for every $u<c$ there is a $v$
with $u<v<c$ such that $S_n\ge q^{nv}$ for infinitely many $n$. These
inequalities prove the description, also when $c$ is infinite.

For a lisse sheaf of rank $r$ with a punctual bound at most $a$, the
trace at each point of $X_0(k_n)$ has absolute value at most
$rq^{na/2}$, and so $S_n\le Dr^2q^{n(a+1)}$ by
[sk-lem-wrp-point-count] ([lem-wf-l2-upper]). For a complex with finite
support, both the number of geometric points and the sum of the ranks of the
cohomology sheaves are bounded independently of $n$, and the same
estimate gives $S_n\le Cq^{na}$. Since the trace of $\mathcal B_b$ at a
$k_n$-point is $b^n$ ([sk-r-real-linear]), the assertion on twists follows.

Finally, the inequality $|z+u|^2\le2|z|^2+2|u|^2$ gives
$\nu(K)\le\max(\nu(L),a-1)$ and, interchanging the two complexes,
$\nu(L)\le\max(\nu(K),a-1)$. If one of $\nu(K)$, $\nu(L)$ exceeds
$a-1$, these two inequalities force equality. Note that the argument
only uses the difference of the trace functions, which need not be
the trace function of a complex.
