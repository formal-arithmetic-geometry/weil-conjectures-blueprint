+++
kind = "proof"
of = "det-tf-restriction-zero-trace-descent"
uses = ["det-tf-restriction-zero-localization", "det-tf-restriction-zero-covers"]
+++
Let $\pi:T'\to T$ be the finite map of [det-tf-restriction-zero-covers]; it has degree
$d^2$ and is étale away from $H\cup V$, and $\pi:B'-y'\to B-y$ is finite étale of degree
$d^2$. The square formed by the downstairs and upstairs restriction maps, with vertical
maps the pullbacks along $\pi$, commutes by functoriality of ordinary pullback and
extension by zero. It is formed after the Künneth rewriting of
[det-tf-restriction-zero-localization], on the complement of the axes, where only étale
pullbacks occur. Compose the downstairs restriction with the pullback to $B'-y'$ and then
with the finite étale trace $R\Gamma(B'-y',\pi^*M)\to R\Gamma(B-y,M)$ for
$M=(N\boxtimes Q)|_{B-y}$. Trace after pullback is multiplication by $d^2$, so $d^2$ times
the downstairs restriction factors through the upstairs restriction, which is zero. Since
$d$ is prime to $\ell$, $d^2$ is a unit of $A$, so the downstairs restriction is zero in
$D(A)$. By [det-tf-restriction-zero-localization] (iii), $\rho_{a,b}=0$.
