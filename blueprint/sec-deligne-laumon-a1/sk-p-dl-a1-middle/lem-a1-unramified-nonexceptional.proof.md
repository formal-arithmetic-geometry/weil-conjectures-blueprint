+++
kind  = "proof"
of    = "lem-a1-unramified-nonexceptional"
+++
Let $V=\mathcal M_{\bar\eta}$, let $W=W(U_0,\bar\eta)$ be the Weil group,
and let $G=\pi_1(U,\bar\eta)\triangleleft W$ be the geometric fundamental
group, as in [def-wf-fundamental-representation]. Since $\mathcal M$ is
irreducible, $V$ is a simple $W$-module. By
[lem-mg-normal-restriction-semisimple], $V|_G$ is semisimple. Hence
every geometric irreducible constituent of $\mathcal M$ is a
$G$-stable direct summand of $V$.

*Case $a\ne0$.* Suppose $\mathcal L_{\psi(ax)}|_U$ were a direct
summand of $V|_G$. The inertia group at
$\infty\in\mathbf P^1_k$ maps into $G$. Restricting from
$\mathbf A^1$ to $U$ does not change the local field at $\infty$. The
inertia group acts trivially on $V$ because $\mathcal M$ is unramified
at infinity, so it acts trivially on every summand. But
$\mathcal L_{\psi(ax)}$ is ramified at infinity by
[lem-a1-artin-schreier-ramified-infinity]. This is a
contradiction.

*Case $a=0$.* Suppose the trivial rank-one representation were a
geometric constituent. Then, being a direct summand, it gives
$V^G\neq0$. The subspace $V^G$ is $W$-stable because $G$ is normal: for
$w\in W$, $g\in G$ and $v\in V^G$,

$$
g\,(wv)=w\,(w^{-1}gw)\,v=wv .
$$

Since $V$ is a simple $W$-module, $V^G=V$. So $G$ acts trivially and
$\mathcal M$ is geometrically constant, contrary to hypothesis.

So no geometric constituent is of the form $\mathcal L_{\psi(ax)}|_U$
with $a\in k$.
