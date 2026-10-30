+++
kind = "proof"
of = "sk-lem-wrp-l2-growth"
+++
The assertion on the radius is the Cauchy–Hadamard formula. For the
equivalent description of $\nu$ in Definition [sk-def-wrp-l2-definition],
put $c=\limsup_n n^{-1}\log_q S_n$, so that $\nu=c-1$. If $a+1>c$,
choose $u$ with $c<u<a+1$. Then $S_n\le q^{nu}$ for all large $n$, and
so $S_n/q^{n(a+1)}\to0$. If $a+1<c$, choose $v$ with $a+1<v<c$. Then
$S_n\ge q^{nv}$ for infinitely many $n$, and so
$\limsup_nS_n/q^{n(a+1)}=\infty$. This proves the description, also
when $c$ is infinite. The remaining assertions follow from bounds for
$S_n$, which we now give.

For a lisse sheaf of rank $r$, punctually of weights $\le a$, the
trace at each point of $X_0(k_n)$ has absolute value at most
$rq^{na/2}$, and so $S_n\le Dr^2q^{n(a+1)}$ by
Lemma [sk-lem-wrp-point-count]. For a complex with finite support, both
the number of geometric points and the sum of the ranks of the
cohomology sheaves are bounded independently of $n$, and the same
estimate gives $S_n\le Cq^{na}$. Since the trace of $\mathcal B_b$ at a
$k_n$-point is $b^n$, tensoring by $\mathcal B_b$ multiplies $S_n$ by
$|\iota(b)|^{2n}=q^{n\lambda_\iota(b)}$, and hence adds
$\lambda_\iota(b)$ to $\nu$.

Finally, the inequality $|z+u|^2\le2|z|^2+2|u|^2$, applied to
$t_{L,n}$ and the difference $t_{K,n}-t_{L,n}$, shows that
$\nu(K)\le\max(\nu(L),a-1)$. Interchanging the two complexes, we get
$\nu(L)\le\max(\nu(K),a-1)$. If one of $\nu(K)$, $\nu(L)$ exceeds
$a-1$, these two inequalities force equality.
