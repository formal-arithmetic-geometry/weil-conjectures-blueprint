+++
id = "prose-01-06"
kind = "hidden"
title = "Coefficients"
order = 13
+++
The trace formula and duality are easiest to prove with torsion
coefficients $\mathbf Z/\ell^n$, where the classical theory of
SGA 4 [sga4] applies, but the eigenvalues of Frobenius live in
characteristic zero. One therefore needs the six operations for
$\Zl$, $\Ql$ and $\overline{\mathbf Q}_\ell$ as well, compatibly with reduction modulo
$\ell^n$. Classically an $\ell$-adic sheaf is a compatible system
$(F_n)$ of sheaves of $\mathbf Z/\ell^n$-modules; this works well for
sheaves, but on the level of derived categories one has to construct the
$\ell$-adic theory by hand, as Ekedahl did [ekedahl90].

We avoid this by working on the pro-étale site of Bhatt and
Scholze [bhatt-scholze15]. There $\Zl$ is a sheaf of rings, an $\ell$-adic sheaf
is a sheaf of modules over it, and the derived category is the ordinary
one. All coefficient rings are obtained in one way, by pulling back a
*condensed ring* (a sheaf of rings on the category of profinite
sets; a topological ring $R$ such as $\Zl$ gives one,
$S\mapsto C(S,R)$) to every scheme (Section [sec-n-coefficients]), so a
single construction of $f^!$ applies to all of them at once. The
classical descriptions by completion, by inverting $\ell$ and by
colimits become comparison theorems (Section [sec-n-change]), and the
geometric arguments are needed only with torsion coefficients, where
they are classical.

Throughout, $\Lambda$ is one of the *admissible* coefficient rings

$$
A,\quad\Zl,\quad\mathcal O_E,\quad\Ql,\quad E,\quad \overline{\mathbf Q}_\ell,
$$

where $A$ is a finite commutative ring killed by a power of $\ell$ and
$E$ is a finite extension of $\Ql$ with ring of integers $\mathcal O_E$.
We allow $E=\Ql$, so that $\Zl$ and $\Ql$ are among the rings
$\mathcal O_E$ and $E$.
The operations act on the category $D^b_{\mathrm{ctf}}(X,\Lambda)$ of bounded
constructible complexes of finite Tor amplitude
(Section [sec-n-constructible]). For integral and rational coefficients this is
just the category $\Dbc(X,\Lambda)$ of bounded constructible complexes;
for a finite ring such as $\mathbf Z/\ell^2$ the Tor condition is needed
so that changing coefficients preserves boundedness.
