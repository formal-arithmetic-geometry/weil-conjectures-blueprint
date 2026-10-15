+++
kind = "proof"
of = "det-sp-tower-classes"
+++
(1) Exactness in towers is levelwise. At level $n$ the sequence is the Kummer
sequence $0\to\mu_{\ell^n}\to\mathbb G_m\xrightarrow{\ell^n}\mathbb G_m\to0$, exact
on $S_{\mathrm{proét}}$ since $\ell$ is invertible. The maps commute with the
transitions: on $\mathbb G_m$, $(x^\ell)^{\ell^n}=x^{\ell^{n+1}}$, so raising to the
$\ell^{n+1}$-th power at level $n+1$ followed by the identity transition equals
the $\ell$-power transition followed by raising to the $\ell^n$-th power; and
the inclusion of $\mu_{\ell^{n+1}}$ intertwines the $\ell$-power transitions.

(2) A short exact sequence in an abelian category gives a boundary map on Ext
groups, here $\operatorname{Ext}^1(\mathbf Z,(\mathbb G_m,\mathrm{id}))\to
\operatorname{Ext}^2(\mathbf Z,(\mu_{\ell^n})_n)$ in towers of abelian sheaves; the
class of $L$ in $H^1(S,\mathbb G_m)$ gives an element of the source (the constant
tower with identity transitions). Since $(\mu_{\ell^n})_n$ is a
$(\mathbf Z/\ell^n)_n$-module, the boundary class is a morphism
$(\mathbf Z/\ell^n)_n\to(\mu_{\ell^n})_n[2]$ in the derived category of
$(\mathbf Z/\ell^n)_n$-modules. Extension of scalars along
$(\mathbf Z/\ell^n)_n\to\mathcal O_{E,S}/\ell^\bullet$ (exact on these flat rank-one
objects) and $(\mu_{\ell^n})_n\otimes\mathcal O_{E,S}/\ell^\bullet=(\mathcal O_{E,S}/\ell^\bullet)(1)$
give $c_1(L)$. Evaluation at $n$ is exact and carries the boundary map of the
tower sequence to the boundary map of the level-$n$ sequence, so level $n$ of
$c_1(L)$ is the finite class.

(3) Same argument with the Kummer sequence with supports: the canonical
section of $\mathcal O(\Delta)$ gives a class in $H^1_\Delta$ of
$(\mathbb G_m,\mathrm{id})$, whose boundary is the class
$\Delta_*(\mathbf Z/\ell^n)_n\to(\mu_{\ell^n})_n[2]$; levelwise it is the finite
diagonal class.

(4) By [det-sp-tower-shriek-levels] (the tower direct image is computed
levelwise), the displayed map evaluates at level $n$ to the finite splitting
of $Rq_*$ of the constant sheaf on $\mathbf P^1$, which is an isomorphism; a
map of towers which is an isomorphism at every level is an isomorphism.
