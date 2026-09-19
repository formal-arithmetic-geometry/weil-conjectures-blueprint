+++
id = "def-poincare-trace"
kind = "definition"
title = "Poincare trace"
order = 117
uses = ["def-all-coefficient-compact-support", "def-coefficient-twists", "def-cohomology-complexes", "def-derived-direct-image", "def-exceptional-inverse-image", "def-smooth-proper-datum", "def-weil-finite-coefficient-datum", "prop-proper-operation-comparison", "prop-smooth-purity", "thm-smooth-proper-structure-admissible"]
+++
Let $\mathscr X=(X_0,d,X)$ be a smooth-proper datum and let
$\ell\neq p$ be prime. Choose an algebraic closure $\Qlb/\Ql$.
Applying Theorem
[thm-smooth-proper-structure-admissible] to
the datum $(\ell,\Qlb;\Ql,\Zl,\ell)$ makes
$Ra_X^!$ available at $\Ql$-coefficients. Let

$$
\eta_{X,\ell}:Ra_X^!\Ql\xrightarrow{\sim}\Ql(d)[2d]
$$

be the canonical smooth-purity isomorphism. Separately, geometric
Frobenius acts on $\Ql(-d)$ by $q^d$. Let
$c_{X,\ell}:Ra_{X!}\xrightarrow{\sim}Ra_{X*}$ be the canonical proper
comparison. Define $\operatorname{tr}_{X,\ell}$ to be the composite

$$
H_c^{2d}(X,\Ql(d))
\xrightarrow{\,H^0(Ra_{X!}(\eta_{X,\ell}^{-1}))\,}
H^0(Ra_{X!}Ra_X^!\Ql)
\xrightarrow{\,H^0(\epsilon_{a_X})\,}\Ql,
$$

where $\epsilon_{a_X}$ is the exceptional adjunction counit. Define

$$
\operatorname{tr}^{(-d)}_{X,\ell}:
H^{2d}(X,\Ql)
\xrightarrow{\ H^{2d}(c_{X,\ell})^{-1}\ }
H_c^{2d}(X,\Ql)
\xrightarrow{\sim}
H_c^{2d}(X,\Ql(d))\otimes_{\Ql}\Ql(-d)
\xrightarrow{\ \operatorname{tr}_{X,\ell}\otimes1\ }
\Ql(-d).
$$
