+++
id = "thm-zl-lefschetz-weil-identity"
kind = "theorem"
title = "Trace-to-determinant identity"
order = 3222
uses = ["cor-trf-point-counting", "def-weil-algebraically-closed-coefficients", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-point-counts-zeta", "def-weil-smooth-proper-cohomological-family", "def-weil-weil-sheaf-complex", "lem-zl-log-det-identity"]
+++
Fix the finite-field datum
$(p,a,q,k_0,k)$, where $q=p^a$, and a prime $\ell\neq p$; write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$,
and interpret the $\Qlb$-objects in the
algebraically closed
coefficient category. Let $X_0/k_0$ be
smooth, proper, geometrically
connected of pure dimension $d\in\mathbf Z_{\geq0}$, put
$X=X_0\times_{k_0}k$, and let $(\Qlb)_X$ be the constant
Weil sheaf with its canonical Weil
structure. Let $F$ be the
global geometric Frobenius
on the ordinary and
compact-support cohomology of $(\Qlb)_X$, in the
geometric-Frobenius convention. For every
$0\leq i\leq2d$, put

$$
V_i=H^i(X,\Qlb),\qquad F_i=F\vert_{V_i},\qquad
P_{i,\ell}(T)=\det(1-TF_i\mid V_i)\in\Qlb[T],
$$

the data obtained from the
smooth-proper
cohomological family by scalar extension. Let $Z(X_0,T)$ be the
point-count zeta series, and assume
the point-counting trace formula
[cor-trf-point-counting] of the trace-formula chapter for the constant Weil
sheaf. Then

$$
\boxed{
Z(X_0,T)=\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}}
\quad\text{in }\Qlb[[T]].
$$
