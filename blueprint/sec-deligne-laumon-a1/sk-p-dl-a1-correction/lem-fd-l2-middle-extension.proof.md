+++
kind  = "proof"
of    = "lem-fd-l2-middle-extension"
+++
The rigidity [lem-wf-l2-purity-rigidity] gives
$\|\mathcal M\|=w$ directly. For the comparison, the two sums agree
on $U_0(k_m)$, so

$$
\|f_{j_*\mathcal M}\|_m^2=\|f_{\mathcal M}\|_m^2+E_m,
\qquad
E_m=\sum_{y\in S_0(k_m)}\bigl|t_{j_*\mathcal M}(y)\bigr|^2\ge0 .
$$

Since $S_0$ is finite, $\#S_0(k_m)\le D:=\sum_{s\in S_0}d(s)$ for
every $m$; and at $y\in S_0(k_m)$ lying above the closed point
$s\in S_0$, the local Frobenius $F_y$ has the eigenvalues
$\alpha^{m/d(s)}$ for $\alpha$ running over the eigenvalues of
$F_s$ on the boundary stalk of the middle extension, which by the
boundary semicontinuity [lem-wf-boundary-semicontinuity] — applied
to $\mathcal M$ with $\beta=w$, the punctual purity of
[def-weil-punctual-weights] exhibiting $\mathcal M$ as punctually
mixed of weights at most $w$ — satisfy
$|\iota(\alpha)|^2\le q_s^{w}=q^{d(s)w}$. Hence
$|\iota(\alpha^{m/d(s)})|^2\le q^{mw}$ and

$$
E_m\le D\,r^2q^{mw}=C\,q^{mw}
$$

for every $m$, with the constant $C:=D\,r^2$.

Now $\|f_{\mathcal M}\|_m^2\le\|f_{j_*\mathcal M}\|_m^2$ for every
$m$, so every parameter with a positive limit superior for
$\mathcal M$ has one for $j_*\mathcal M$ as well: this gives
$\|j_*\mathcal M\|\ge\|\mathcal M\|$. Conversely, for $\beta>w$ the
ratio of [def-wf-l2-norm] for $j_*\mathcal M$ is bounded by the
ratio for $\mathcal M$, which has limit superior $0$ because
$\beta>\|\mathcal M\|$, plus $Cq^{m(w-\beta-1)}$, which also has
limit superior $0$ because $\beta+1>w$. No $\beta>w$ therefore has
a positive limit superior, so $\|j_*\mathcal M\|\le w$, and the two
parameters agree and equal $w$.
