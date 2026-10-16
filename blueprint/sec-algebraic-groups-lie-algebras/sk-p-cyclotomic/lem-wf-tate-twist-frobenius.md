+++
id = "lem-wf-tate-twist-frobenius"
kind = "lemma"
title = "Frobenius on the stalk of a twist"
lean = ["AlgebraicGeometry.WeilSheaf.stalk_frobenius_tateTwistSheaf", "AlgebraicGeometry.WeilSheaf.two_mul_logb_norm_cyclotomicUnit_pow"]
order = 2917
uses = ["def-wf-internal-hom", "def-wf-tate-twist", "def-wf-tensor-product", "lem-wf-tate-twist-compatibility"]
+++
For every $m\in\mathbf Z$ and every closed point $x$ of $X_0$, the
geometric Frobenius $\varphi_{E(m)}$ on $E(m)_{\bar x}$ is
$Q_x^{-m}\mathrm{id}$, where $Q_x=|\kappa(x)|$.
