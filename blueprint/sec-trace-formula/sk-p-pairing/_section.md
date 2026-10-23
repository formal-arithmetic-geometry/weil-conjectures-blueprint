+++
id = "sk-p-pairing"
kind = "lemma"
title = "Local terms on the point"
order = 3479
uses = ["sk-d-corr", "sk-d-pairing", "sk-d-setup", "sk-d-six", "sk-d-trace", "sk-d-trace-class", "sk-p-trace", "sk-thm-sf-kunneth-verdier", "sk-thm-sf-package"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.integral_traceClass_eq_trace"]
tags = ["sketch"]
+++
Let $P\in\operatorname{Perf}(A)$, viewed as an object of $\Dctf(s,A)$, and let
$u:P\to P$ be a cohomological correspondence on $(s,P)$ for the identity
correspondence of $s$, whose fixed locus is $s$. Then

$$
\operatorname{LT}_s(u)=\operatorname{tr}_A(u\mid P).
$$

*Complement.* The trace class of $u$ is the supported pairing
$\langle u,1_P\rangle_{\mathrm{LV}}$ of [sk-d-pairing], so that

$$
\int_s\Tr_{\mathrm{id}}(u)=\int_s\langle u,1_P\rangle_{\mathrm{LV}}=\tr_A(u\mid P).
$$

On any $X$, for an endocorrespondence $(C,c,u)$ on $(X,K)$ with
$f:\Fix(c)\to X$, the exceptional adjoint of the trace class $\Tr_c(u)$ is

$$
Rf_!A_{\Fix(c)}\simeq\Delta^*Rc_!A_C
\xrightarrow{\Delta^*\widetilde u}K\otimes D_XK
\xrightarrow{\mathrm{ev}\circ\mathrm{sym}}\omega_X.
$$
