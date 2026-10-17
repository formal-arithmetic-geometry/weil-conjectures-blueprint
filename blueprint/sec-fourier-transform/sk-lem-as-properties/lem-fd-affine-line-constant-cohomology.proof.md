+++
kind  = "proof"
of    = "lem-fd-affine-line-constant-cohomology"
uses = ["sbc-thm-cohomological-dimension-of-an-affine-curve", "thm-sc-affine-cohomology", "lem-sc-pic-affine", "sk-prop-sfb-qlbar-colimit-x", "sk-prop-pe-continuous-cohomology", "sk-prop-scalar-six"]
+++
Write $X=\mathbf A^1_{\bar k}$ and $a:X\to\operatorname{Spec}\bar k$.

*Torsion coefficients.* For every $n\ge1$, $H^q(X,\mathbf Z/\ell^n)$ is
$\mathbf Z/\ell^n$ for $q=0$, since $X$ is connected, and $0$ for $q>0$: the
vanishing for $q>1$ is the cohomological dimension of an affine curve of
[sbc-thm-cohomological-dimension-of-an-affine-curve], and
$H^1(X,\mathbf Z/\ell^n)\cong\operatorname{Pic}(X)[\ell^n]=0$ by
[thm-sc-affine-cohomology], the Picard group being trivial by
[lem-sc-pic-affine] (the compactification is $\mathbf P^1$ of genus $0$,
whose Jacobian is trivial, so the quotient of [lem-sc-pic-affine] is
$\operatorname{Pic}(\mathbf A^1)=0$). These are étale cohomology groups of
torsion sheaves, equal to the pro-étale ones.

*Integral coefficients.* By [sk-prop-sfb-qlbar-colimit-x],
$\mathbf Z_{\ell,X}\simeq\varprojlim_n(\mathbf Z/\ell^n)_X$, a limit of
classical sheaves with epimorphic transition maps, so
[sk-prop-pe-continuous-cohomology] gives exact sequences
$$
0\to\varprojlim\nolimits^1_nH^{q-1}(X,\mathbf Z/\ell^n)\to H^q(X,\mathbf Z_{\ell})
\to\varprojlim_nH^q(X,\mathbf Z/\ell^n)\to0 .
$$
The groups $H^{q-1}(X,\mathbf Z/\ell^n)$ are finite, so the $\varprojlim^1$
term vanishes, and $H^0(X,\mathbf Z_\ell)=\mathbf Z_\ell$, $H^q(X,\mathbf Z_\ell)=0$
for $q>0$. Thus $Ra_*\mathbf Z_{\ell,X}\simeq\mathbf Z_\ell$ in degree $0$.

*Coefficients $\overline{\mathbf Q}_\ell$.* The composite
$\mathbf Z_\ell\to\mathbf Q_\ell\to\overline{\mathbf Q}_\ell$ is a coefficient
map of [sk-prop-scalar-six], so the coefficient comparison for $Ra_*$ gives
$Ra_*\overline{\mathbf Q}_{\ell,X}\simeq\overline{\mathbf Q}_\ell\otimes^{\mathbf L}_{\mathbf Z_\ell}Ra_*\mathbf Z_{\ell,X}
\simeq\overline{\mathbf Q}_\ell$ in degree $0$. Hence
$H^0(X,\overline{\mathbf Q}_\ell)=\overline{\mathbf Q}_\ell$ and
$H^q(X,\overline{\mathbf Q}_\ell)=0$ for $q>0$.
