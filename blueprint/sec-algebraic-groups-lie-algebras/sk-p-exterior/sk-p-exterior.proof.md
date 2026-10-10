+++
kind  = "proof"
of    = "sk-p-exterior"
uses = ["sk-d-monodromy", "sk-p-central", "sk-p-linear-filtration", "sk-p-readout"]
+++
*Reduction to a degree datum.* If $\deg$ is trivial, then $W=P$ and every
representation with finite geometric determinant has weight $0$: its
determinant takes finitely many values on $W$, so $\delta(\gamma)$ has
finite order and $\lambda$ kills it ([sk-d-weights]). Since $\bigwedge^sV$
has the nonzero constituent $Q$, we have $s\le r$, and any $s$ indices give
$\dw_\lambda(Q)=0=a_{i_1}+\cdots+a_{i_s}$. Otherwise
$\deg(W)=a\mathbf Z$ with $a>0$; then $\deg_0=\deg/a:W\to\mathbf Z$ is
surjective with the same kernel $P$, so finiteness of geometric
determinants is the same for $\deg$ and $\deg_0$. Choose $\gamma_0$ with
$\deg_0(\gamma_0)=1$ and write $\gamma=u\gamma_0^m$ with $u\in P$ and
$m=\deg_0(\gamma)$. For every representation $Q'$ with finite geometric
determinant, $\lambda(\delta_{Q'}(u))=0$ as above, so
$\dw_\lambda(Q')$ at $\gamma$ is $m$ times $\dw_\lambda(Q')$ at
$\gamma_0$. Multiplying the formula for $(\deg_0,\gamma_0)$ by $m$ gives
it for $(\deg,\gamma)$, with the weight list multiplied by $m$. So we may
assume that $(W,\deg,\gamma)$ is a degree datum ([sk-d-monodromy]).

*The degree-datum case.* Let $\rho:W\to\GL(V)$ be the representation,
semisimple by hypothesis. Choose a positive central pair $(N,z)$ for it by
[sk-p-central], and a basis of $V$ adapted to the decomposition, with a
basis within each simple summand. Each $V_j$ is a simple subquotient of
the defining representation with finite geometric determinant, so by
[sk-p-readout] $z$ acts on it by a scalar $c_j$ with
$\lambda(c_j)=N\dw_\lambda(V_j)$. Thus $z$ is diagonal in the adapted basis
with entries $c_i$ satisfying $\lambda(c_i)=Na_i$, where repetitions follow
[sk-d-weights]. Its exterior power $\bigwedge^sz$ is diagonal with entries
the products $c_{i_1}\cdots c_{i_s}$, $i_1<\cdots<i_s$, by
[sk-p-linear-spectra].

Now consider the represented datum $\bigwedge^s\rho$ on $\bigwedge^sV$.
The map $\bigwedge^s:\GL(V)\to\GL(\bigwedge^sV)$ is a regular homomorphism
([sk-d-linear]), so by continuity it maps the Zariski closures $G\supseteq H$
of $\rho(W)\supseteq\rho(P)$ into the Zariski closures $G'\supseteq H'$ of
$\bigwedge^s\rho(W)\supseteq\bigwedge^s\rho(P)$. Hence $\bigwedge^sz\in
H'(\bigwedge^s F)^N$; and $\bigwedge^sz$ commutes with the dense subgroup
$\bigwedge^s\rho(W)$ of $G'$, hence with $G'$, since centralizers are
closed. So $(N,\bigwedge^sz)$ is a positive central pair for
$\bigwedge^s\rho$ ([sk-d-central]). The constituent $Q$ is a simple
subquotient of its defining representation with finite geometric
determinant, so $\bigwedge^sz$ acts on $Q$ by a scalar $c_Q$ and
$\dw_\lambda(Q)=\lambda(c_Q)/N$ by [sk-p-readout]. By
[sk-p-linear-filtration], a scalar by which $\bigwedge^sz$ acts on a
subquotient is an eigenvalue of $\bigwedge^sz$ on $\bigwedge^sV$, so
$c_Q=c_{i_1}\cdots c_{i_s}$ for some $i_1<\cdots<i_s$. Additivity of
$\lambda$ gives
$\dw_\lambda(Q)=\sum_t\lambda(c_{i_t})/N=a_{i_1}+\cdots+a_{i_s}$.
