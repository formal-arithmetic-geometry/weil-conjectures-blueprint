+++
id = "sk-p-pairing"
kind = "proposition"
title = "Pairing and its point normalization"
order = 2657
uses = ["sk-d-corr", "sk-d-pairing", "sk-d-setup", "sk-d-six", "sk-d-trace", "sk-d-trace-class", "sk-p-trace", "sk-thm-sf-kunneth-verdier", "sk-thm-sf-package"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.integral_traceClass_eq_trace"]
tags = ["sketch"]
+++
Let $s$ be the spectrum of a field. For a perfect (dualizable)
$P\in D^b_{ctf}(s,A)$ and an endomorphism $v:P\to P$, regard $v$ as the
endocorrespondence with support $s$, identity legs and coefficient map $v$;
its fixed scheme is $s$. Its trace class, the supported pairing
$\langle v,1_P\rangle_{\mathrm{LV}}$, integrates to the ordinary categorical trace:

$$
\int_s\Tr_{\mathrm{id}}(v)=\int_s\langle v,1_P\rangle_{\mathrm{LV}}=\tr_A(v\mid P).
$$
