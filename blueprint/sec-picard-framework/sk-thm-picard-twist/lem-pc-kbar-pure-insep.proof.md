+++
kind  = "proof"
of    = "lem-pc-kbar-pure-insep"
+++
If $p=1$ every algebraic element is separable, so $n=0$ works, and
$K=k$ by [lem-pc-sepclosed-finite-sep-trivial]; assume
$\operatorname{char}k=p>0$. Let $\alpha\in K$ and $E=k(\alpha)$ (finite over
$k$). Let $L$ be the separable closure of $k$ inside $E$, i.e. the maximal
separable subextension (standard: among the subextensions
$k\subseteq k'\subseteq E$ with $k'/k$ finite separable there is a maximal
one, obtained by compositum). Then $E/L$ is purely inseparable: for a
finite extension in characteristic $p$ this is the standard fact that a
finite extension is the compositum of a separable and a purely
inseparable subextension (for $\beta\in E$ the minimal polynomial over $L$
is $T^{p^f}-c$, a purely inseparable polynomial: this is the classical
normal-separable devissage; we use it as standard field theory). Let
$[E:L]=p^e$. For every $\beta\in E$, $\beta^{p^e}\in L$: indeed the
minimal polynomial $T^{p^f}-c$ of $\beta$ over $L$ has $f\le e$, and
$\beta^{p^e}=c^{p^{e-f}}\in L$.
Apply this to $\beta=\alpha$: $\alpha^{p^e}\in L$, which is separable
over $k$; take $n=e$. The last assertion: $\alpha^{p^n}$ is separable
algebraic over $k$, so it lies in $k$ by
[lem-pc-sepclosed-finite-sep-trivial] (applied to $k(\alpha^{p^n})/k$).
Thus every element of $K$ lies in $k$ after taking a $p^n$-th power,
i.e. $K/k$ is purely inseparable.
