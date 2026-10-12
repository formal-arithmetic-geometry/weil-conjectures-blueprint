+++
kind  = "proof"
of    = "thm-trf-grothendieck-lefschetz-qbar"
+++
Apply [thm-trf-trace-formula-e] to
$K_E\in D^b_{c,\mathrm W}(X,E)$ with its Weil map $\varphi_E$; that
theorem needs no integral Weil presentation and only the finite-level
hypotheses assumed here. It gives finite-dimensional $E$-cohomology in
finitely many degrees, and the identity holds in $E$ for the
categorical traces and, by the supertrace law
[prop-trf-trace-formal-laws], for the alternating sums of the
traces on compact-support and stalk cohomology. The object $K$ is
represented by $K_E$, so the global cohomology and each local stalk
are the scalar extensions along $E\hookrightarrow\Qlb$ of the
$E$-level ones, and the traces are the images of the $E$-traces, by
the scalar-extension law of [prop-trf-trace-formal-laws] applied
to the summand traces of [def-trf-karoubi-trace] (at the identity
idempotent the summand trace is the ordinary categorical trace); hence
applying the summand trace to both sides of the $E$-identity gives
the displayed identity after scalar extension $E\hookrightarrow\Qlb$.
Independence is [prop-trf-karoubi-independence].
