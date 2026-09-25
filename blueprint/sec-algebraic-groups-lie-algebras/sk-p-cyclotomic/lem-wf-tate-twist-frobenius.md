+++
id = "lem-wf-tate-twist-frobenius"
kind = "lemma"
title = "Frobenius on the stalk of a twist"
order = 2729
uses = ["def-wf-internal-hom", "def-wf-tate-twist", "def-wf-tensor-product"]
+++
For every $m\in\mathbf Z$ and every closed point $x$ of $X_0$, the
geometric Frobenius $\varphi_{E(m)}$ on $E(m)_{\bar x}$ is
$Q_x^{-m}\mathrm{id}$, where $Q_x=|\kappa(x)|$.

## Proof

On $\mu_{\ell^n}$ the geometric Frobenius acts by raising to the
inverse $q$-th power, hence on
$\mathbf Z_\ell(1)=\varprojlim_n\mu_{\ell^n}$ it is multiplication by
$Q_x^{-1}$ on the stalk at $\bar x$; the $E$-twist and the
tensor/internal-Hom constructions of [def-wf-tate-twist] then give
$Q_x^{-m}$ for $E(m)_{\bar x}$.
