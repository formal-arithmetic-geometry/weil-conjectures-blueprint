+++
kind  = "proof"
of    = "sk-prop-av-prime-p-etale"
+++
Base change to an algebraic closure $\bar k$ does not change the order
($\dim_{\bar k}(\cO_G\otimes_k\bar k)=\dim_k\cO_G$) or the
characteristic, and $G$ is étale over $k$ iff $G_{\bar k}$ is étale over
$\bar k$, because $\Omega_{G_{\bar k}/\bar k}=\Omega_{G/k}\otimes_k\bar k$
and $\bar k$ is faithfully flat over $k$. So we may assume $k$
algebraically closed.

Over the algebraically closed $k$, a finite scheme is étale iff it is
reduced: writing the coordinate ring as a product of finite local
$k$-algebras $B_i$, one has $\Omega_{B/k}=0$ iff every $B_i$ is a
finite separable field extension of $k$, i.e. $k$ itself. Write
$G=G^0\sqcup G^{\mathrm{et}}$ with $G^0$ the identity component, a
closed subgroup scheme (the multiplication maps the connected
$G^0\times_kG^0$ into $G^0$). If $p>0$ and
$G^0\ne\Spec k$, then $\lvert G^0\rvert$ is a positive power of $p$ by
[sk-prop-av-connected-order], and $\lvert G^0\rvert$ divides
$\lvert G\rvert=m$, contradicting $p\nmid m$. Hence $G^0=\Spec k$ and
$G$ is reduced, hence étale. For $p=0$ this is Cartier's theorem
(`047N`): every finite group scheme over a field of
characteristic zero is smooth, and a finite smooth group scheme is
étale.
