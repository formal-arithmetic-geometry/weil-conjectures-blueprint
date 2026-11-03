+++
kind = "proof"
of = "det-proper-unbounded-window-bounded-below"
+++
Since $K$ is bounded below, the hypercohomology (Cartan–Eilenberg) spectral sequence

$$
E_2^{u,v}=R^up_*\mathcal H^v(K)\Longrightarrow\mathcal H^{u+v}(Rp_*K)
$$

lies in the region $u\geq0$, $v\geq a$ and converges. By [sk-lem-proper-heart-bound],
$E_2^{u,v}=0$ for $u>2d+1$ and $E_2^{u,v}\in\IndCons(Y,\Lambda)$. Hence only the columns $0\leq u\leq2d+1$
are nonzero, the differentials $d_r$ vanish for $r>2d+2$, and $E_\infty=E_{2d+3}$. Each $E_r^{u,v}$ is a
subquotient (kernel of a map modulo the image of a map) of objects of $\IndCons(Y,\Lambda)$, and the
differentials are maps in that category; by part (2) of [sk-prop-ind-heart] (closure under kernels and
cokernels) every $E_r^{u,v}$, in particular $E_\infty^{u,v}$, lies in $\IndCons(Y,\Lambda)$. The abutment
$\mathcal H^n(Rp_*K)$ has a finite filtration (at most $2d+2$ steps) with graded pieces $E_\infty^{u,n-u}$,
so it is an iterated extension of objects of $\IndCons(Y,\Lambda)$ and lies in it by closure under
extensions.

*Amplitude.* If $\mathcal H^v(K)=0$ for $v<a$, then $E_2^{u,v}=0$ for $u+v<a$, so $\mathcal H^n(Rp_*K)=0$ for
$n<a$. If $\mathcal H^v(K)=0$ for $v>b$, then $E_2^{u,v}=0$ for $u+v>b+2d+1$, so $\mathcal H^n(Rp_*K)=0$ for
$n>b+2d+1$.
