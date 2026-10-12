+++
kind  = "proof"
of    = "lem-sfb-torsion-triangulated"
+++
$1\cdot\mathrm{id}_0=0$. If $m\cdot\mathrm{id}_X=0$, then
$m\cdot\mathrm{id}_{X[n]}=(m\cdot\mathrm{id}_X)[n]=0$, since the shift functors are linear.
For the triangle, write $u\colon X_1\to X_2$ and $v\colon X_2\to X_3$. Since
$v\circ(m_3\cdot\mathrm{id}_{X_2})=(m_3\cdot\mathrm{id}_{X_3})\circ v=0$, the long exact
sequence of $\Hom(X_2,-)$ gives $b\colon X_2\to X_1$ with
$m_3\cdot\mathrm{id}_{X_2}=u\circ b$. Then
$$
(m_1m_3)\cdot\mathrm{id}_{X_2}=m_1\cdot(u\circ b)=((m_1\cdot\mathrm{id}_{X_2})\circ u)\circ b
=(u\circ(m_1\cdot\mathrm{id}_{X_1}))\circ b=0 .
$$
Since $M$ is a submonoid, $m_1m_3\in M$.
